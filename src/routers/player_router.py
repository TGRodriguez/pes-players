from fastapi import APIRouter, Depends


from services.player_service import PlayerService

from schemas.player_schemas import GetPlayerRequestSchema

PlayerRouter = APIRouter(prefix="/v1/players", tags=["players"])


@PlayerRouter.get("/{id}")
def get(id: int, player_service: PlayerService = Depends()):
    return player_service.get(id).normalize()
    # return player_service.get(id)


@PlayerRouter.get("/")
def get_players(
    player_service: PlayerService = Depends(), model: GetPlayerRequestSchema = Depends()
):
    # normalize every player in the list
    return [
        player.normalize()
        for player in player_service.get_with_filters(model.model_dump())
    ]
    # return player_service.get_with_filters(model.model_dump())
