import fastapi
import uvicorn
import os

from dotenv import load_dotenv

load_dotenv()

APP_HOST = os.environ.get("APP_HOST")
APP_PORT = os.environ.get("APP_PORT")

app = fastapi.FastAPI()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=APP_HOST,
        port=int(APP_PORT),
    )
