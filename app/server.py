from fastapi import FastAPI
from app.endpoints import (
    connect,
    scan,
    configure
)
from fastapi.middleware.cors import CORSMiddleware


def create_server(repositories: None):
    server = FastAPI(debug=True)
    server.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    server.include_router(connect.router)
    server.include_router(scan.router)
    server.include_router(configure.router)

    server.repositories = repositories

    return server
