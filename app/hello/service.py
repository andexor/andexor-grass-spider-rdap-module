# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

from pydantic import ValidationError
from app.hello.model import HelloException, HelloResponse

async def hello(who: str = "") -> HelloResponse:

    """
    Says hello to someone.

    Args:
        who (str): who to say hello to

    Returns:
        a HelloResponse that says hello to someone

    Raises:
        HelloException if there is a data validation error
    """

    try:
        return HelloResponse(msg=who)
    except ValidationError as e:
        raise HelloException(e)
