from fastapi import Depends
from models.player_model import Player

from repositories.players_repository import PlayerRepository


class PlayerService:
    player_repository: PlayerRepository

    def __init__(
        self,
        player_repository: PlayerRepository = Depends(),
    ) -> None:
        self.player_repository = player_repository

    def get(self, player_id: int) -> Player:
        return self.player_repository.get(Player(id=player_id))

    def get_with_filters(self, filters: dict) -> Player:
        return self.player_repository.get_with_filters(filters)
