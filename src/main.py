import fastapi
import uvicorn
import os

from configs.env_vars import load_env_vars

from routers import player_router

from configs.db import get_db_connection

load_env_vars()
get_db_connection()

app = fastapi.FastAPI()
app.include_router(player_router.PlayerRouter)

if __name__ == "__main__":
    APP_HOST = os.environ.get("APP_HOST")
    APP_PORT = os.environ.get("APP_PORT")

    uvicorn.run(
        app,
        host=APP_HOST,
        port=int(APP_PORT),
    )
