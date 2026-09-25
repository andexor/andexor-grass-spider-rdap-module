# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

from fastapi import APIRouter, FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles

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
        title="Andexor Grass Spider RDAP Module",
        version="1.0.0",
        summary="Andexor Grass Spider RDAP Module",
        description="OpenAPI Documentation",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Configure OpenAPI documentation.
app.openapi = custom_openapi

# Health Check
@app.get("/health")
async def health():
    """
    Health Check.

    Returns OK.
    """
    return {"status": "OK"}

# Create a router for REST APIs.
api_router = APIRouter(prefix="/api/v1")
app.include_router(api_router)

# Mount the documentation directory.
app.mount("/", StaticFiles(directory="doc", html=True), name="doc")

#######
# API #
#######

@api_router.get("/items/{item_id}")
async def read_item(item_id: int, q: str = ""):
    return {
        "item_id": str(item_id),
        "query_param": q
    }
