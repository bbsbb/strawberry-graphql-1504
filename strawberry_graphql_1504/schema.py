from typing import Optional

import strawberry
from strawberry.field import StrawberryField

import response
import input  # <--  Import order is significant since 0.92
import model


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Query:
    bug: response.BResponse


def get_b() -> response.BResponse:
    b = model.B(b="bug", a_ref=model.A(a="buggy bug", b=3))
    return response.BResponse.from_pydantic(b)


def mutate_b(input: input.BInput) -> str:
    return "done"


@strawberry.type
class Query:
    bug: StrawberryField = strawberry.field(resolver=get_b)


@strawberry.type
class Mutation:
    set_bug: StrawberryField = strawberry.field(resolver=mutate_b)


schema = strawberry.Schema(Query, mutation=Mutation)
