# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

from fastapi import APIRouter

# REST API router.
api = APIRouter(prefix="/api/v1")

@api.get("/items/{item_id}")
async def read_item(item_id: int, q: str = ""):
    return {
        "item_id": str(item_id),
        "query_param": q
    }
