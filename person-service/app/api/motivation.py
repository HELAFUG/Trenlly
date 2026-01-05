from fastapi import APIRouter
from service.motivation import get_random_motivation

motivation_router = APIRouter(prefix="/daily-motivation", tags=["Motivation"])


@motivation_router.get("/", response_model=str)
async def get_daily_motivation():
    return await get_random_motivation()
