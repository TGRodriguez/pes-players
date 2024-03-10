from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from configs.db import (
    get_db_connection,
)
from models.player_model import Player
from models.position_model import Position
from models.player_face_model import PlayerFace
from models.player_body_model import PlayerBody
from models.player_teams_model import PlayerTeams
from models.player_stats_model import PlayerStats
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.expression import func


class PlayerRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Player]:
        query = self.db.query(Player)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()

    def get(self, player: Player) -> Player:
        return self.db.get(Player, player.id)

    def get_with_filters(self, filters: dict) -> Player:
        query = self.db.query(Player)
        if not filters["allow_classic_players"]:
            query = query.join(PlayerTeams).options(
                joinedload(Player.player_teams_relationship)
            )
            query = query.filter(PlayerTeams.national_team.notlike("%Classic%"))

        if "min_height" in filters or "max_height" in filters:
            query = query.join(PlayerBody).options(
                joinedload(Player.player_body_relationship)
            )

        for attr, value in filters.items():
            if value is None or attr == "quantity" or attr == "allow_classic_players":
                continue
            if attr == "min_age":
                attr = "age"
                query = query.filter(getattr(Player, attr) >= value)
            elif attr == "max_age":
                attr = "age"
                query = query.filter(getattr(Player, attr) <= value)
            elif attr == "skin_colour":
                query = (
                    query.join(PlayerFace)
                    .options(joinedload(Player.player_face_relationship))
                    .filter(getattr(PlayerFace, attr) == value)
                )
            elif attr == "min_height":
                attr = "height"
                query = query.filter(getattr(PlayerBody, attr) >= value)
            elif attr == "max_height":
                attr = "height"
                query = query.filter(getattr(PlayerBody, attr) <= value)
            elif attr == "min_average":
                attr = "average_stats"
                query = (
                    query.join(PlayerStats)
                    .options(joinedload(Player.player_stats_relationship))
                    .filter(getattr(PlayerStats, attr) >= value)
                )

            elif attr == "positions":
                # Verificamos que el jugador tenga al menos todas
                # las posiciones especificadas
                for position_name in value:
                    query = query.filter(
                        Player.favoured_positions.any(
                            Position.position_name == position_name
                        )
                    )

            else:
                query = query.filter(getattr(Player, attr) == value)

        # Ordenar de manera aleatoria y limitar la cantidad de resultados
        query = query.order_by(func.random()).limit(filters["quantity"])

        results = query.all()
        return results
