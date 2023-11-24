import uvicorn
from fastapi import FastAPI
from cbtw_process_api.router import router
from cbtw_process_api.db import Repository
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    Repository.startup()
    yield
    Repository.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8081)