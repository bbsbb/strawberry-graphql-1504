import strawberry

import model


@strawberry.experimental.pydantic.type(model=model.A)
class AResponse:
    a: strawberry.auto
    b: strawberry.auto


@strawberry.experimental.pydantic.type(model=model.B)
class BResponse:
    b: strawberry.auto
    a_ref: strawberry.auto
