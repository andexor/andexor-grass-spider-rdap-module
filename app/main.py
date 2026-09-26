# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

from dataclasses import dataclass

from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from app.hello import rest

# Initialize FastAPI.
app = FastAPI(
    title="Andexor Grass Spider RDAP Module",
    summary="Andexor Grass Spider RDAP Module",
    description="OpenAPI Documentation",
    version="1.0.0",
    terms_of_service="https://andexor.net/tos",
    contact={
        "name": "Ed Jenkins",
        "url": "https://andexor.net/",
        "email": "ed@andexor.net",
    },
    license_info={
        "name": "Apache License 2.0",
        "identifier": "Apache-2.0",
    },
    docs_url=None,
    redoc_url=None,
)

# Configures OpenAPI to use our branded favicon.
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """
        Configures OpenAPI to use our branded favicon.
    """
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        swagger_favicon_url="/favicon.ico",
        title=app.title + " - Swagger UI",
    )

# Configures OpenAPI documentation.
# This can not be declared as async.
def custom_openapi():
    """
        Configures OpenAPI documentation.

        Returns
        -------
        An OpenAPI schema
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        summary=app.summary,
        description=app.description,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Configure OpenAPI documentation.
app.openapi = custom_openapi

# Health check response.
@dataclass
class HealthResponse(dict[str, str]):
    status: str

# Version-independent health check
@app.get(
    path="/health",
    tags=["Health"]
)
async def health() -> HealthResponse:
    """
    Health Check.

    Returns OK.
    """
    return HealthResponse("UP")

# Add the REST API router first.
app.include_router(rest.api)

# Mount the documentation directory last.
app.mount("/", StaticFiles(directory="doc", html=True), name="doc")
