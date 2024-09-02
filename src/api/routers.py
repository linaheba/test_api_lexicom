from fastapi import APIRouter

from src.api.schemas import DefaultResponse
from src.db import redis_ as r
from src.logger import logging


router = APIRouter(tags=['api'])


@router.get("/check_data")
async def get_query(phone: str) -> DefaultResponse:
    """ Получение данных"""
    try:
        r.set('phone', phone)
        return DefaultResponse(error=False, message="ok", payload={'phone': r.get('phone')})
    except Exception as err:
        logging.error(err)
        return DefaultResponse(error=True, message=err, payload=None)



