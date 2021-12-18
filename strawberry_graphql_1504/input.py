import strawberry

import model


@strawberry.experimental.pydantic.input(model=model.A)
class AInput:
    a: strawberry.auto
    b: strawberry.auto


@strawberry.experimental.pydantic.input(model=model.B)
class BInput:
    b: strawberry.auto
    a_ref: strawberry.auto
