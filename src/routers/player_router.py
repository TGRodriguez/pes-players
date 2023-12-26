from fastapi import APIRouter, Depends


from services.player_service import PlayerService

PlayerRouter = APIRouter(prefix="/v1/players", tags=["players"])


@PlayerRouter.get("/{id}")
def get(id: int, player_service: PlayerService = Depends()):
    return player_service.get(id).normalize()
