import uvicorn
from fastapi import FastAPI
from router import router
from db import Repository
from contextlib import asynccontextmanager
import logging
from fastapi.logger import logger as fastapi_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    Repository.startup()
    yield
    Repository.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(router)

gunicorn_logger = logging.getLogger("gunicorn")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8081)
else:
    logging.info("------------------ Application Started -------------------")
    fastapi_logger.setLevel(gunicorn_logger.level)