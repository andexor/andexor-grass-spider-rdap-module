# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

from pydantic import BaseModel, Field, ValidationError

class HelloRequest(BaseModel):

    """
    Example request.

    Attributes:
        who (str): who to say hello to
    """

    who: str

class HelloResponse(BaseModel):

    """
    Example request.

    Attributes:
        msg (str): the hello message
    """

    msg: str | None = Field(max_length=10)

class HelloError(BaseModel):

    """
    Example request.

    Attributes:
        err (str): error message
    """

    err: str | None = Field()

class HelloException(Exception):

    """
    Example request.

    Attributes:
        err (str): error message
    """

    err: str | None = None

    def __init__(self, e: ValidationError):
        """
        Constructor.

        Args:
            e (ValidationError): a validation exception
        """
        self.err = "".join([error["msg"] for error in e.errors()])
