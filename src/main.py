import fastapi
import uvicorn
import os
from dotenv import load_dotenv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dev", help="Run in development mode", action="store_true")
args = parser.parse_args()

app = fastapi.FastAPI()

if __name__ == "__main__":
    if args.dev:
        load_dotenv()
    APP_HOST = os.environ.get("APP_HOST")
    APP_PORT = os.environ.get("APP_PORT")

    uvicorn.run(
        app,
        host=APP_HOST,
        port=int(APP_PORT),
    )
