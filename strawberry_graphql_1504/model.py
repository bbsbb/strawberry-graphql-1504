from typing import Optional

from pydantic import BaseModel


class A(BaseModel):
    a: str
    b: int


class B(BaseModel):
    b: str
    a_ref: Optional[A]
