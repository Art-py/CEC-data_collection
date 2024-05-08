from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.test_app.models import test_model_model
from config import get_async_session
from services.api.test_model.schemas import TestModelCreateSchema, TestModelListSchema

test_model_router = APIRouter(
    prefix="/test-model",
    tags=["Test Model"],
)


@test_model_router.post("/create")
async def test_model_create(
    new_model: TestModelCreateSchema,
    session: AsyncSession = Depends(get_async_session),
):
    stats = insert(test_model_model).values(**new_model.dict())
    await session.execute(stats)
    await session.commit()


@test_model_router.get("/list", response_model=List[TestModelListSchema])
async def test_model_list(session: AsyncSession = Depends(get_async_session)):
    query = select(test_model_model)
    result = await session.execute(query)
    return result.mappings().all()
