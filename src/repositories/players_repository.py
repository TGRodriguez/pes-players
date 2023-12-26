from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from configs.db import (
    get_db_connection,
)
from models.player_model import Player


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
        return self.db.get(
            Player, player.id, options=[lazyload(Player.registered_position_relationship)]
        )
