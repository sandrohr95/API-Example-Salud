import uvicorn
from fastapi import FastAPI
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response

from API import __version__
from API.config import settings
from API.logger import logger
from API.routes.patient import router as patient_router

app = FastAPI(
    title="API",
    docs_url="/api/docs",
    openapi_prefix=settings.ROOT_PATH,
    description="",
    version=__version__,
)

# cors

origins = ["*"]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

# routes
app.include_router(patient_router, prefix="/api/v2/patient")


def run_server():
    logger.info(f"🚀 Deploying server at http://{settings.API_HOST}:{settings.API_PORT}")
    uvicorn.run(
        app, host=settings.API_HOST, port=settings.API_PORT, root_path=settings.ROOT_PATH, log_level="info",
    )


run_server()