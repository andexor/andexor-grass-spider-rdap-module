# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.hello.model import HelloError, HelloException, HelloResponse
from . import service

# REST API router.
api = APIRouter(prefix="/api/v1")

@api.get(
    path="/hello/{who}",
    tags=["Hello"],
    responses={
        status.HTTP_200_OK: {"model": HelloResponse},
        status.HTTP_400_BAD_REQUEST: {"model": HelloError}
    }
)
async def hello(who: str = "") -> JSONResponse:

    """
    Says hello to someone.

    Args:
        who (str): who to say hello to

    Returns:
        a HelloResponse that says hello to someone
        or a HelloException if there is a data validation error
    """

    try:
        r: HelloResponse = await service.hello(who)
        return JSONResponse(content=r.model_dump(), status_code=status.HTTP_200_OK)
    except HelloException as ex:
        e: HelloError = HelloError(err=ex.err)
        return JSONResponse(content=e.model_dump(), status_code=status.HTTP_400_BAD_REQUEST)
