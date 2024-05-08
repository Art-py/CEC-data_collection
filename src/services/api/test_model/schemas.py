from pydantic import BaseModel


class TestModelCreateSchema(BaseModel):
    name: str


class TestModelListSchema(BaseModel):
    id: int
    name: str
