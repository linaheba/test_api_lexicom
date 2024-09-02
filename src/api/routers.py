# Роуты
from fastapi import APIRouter

from src.logger import logging
from src.api.helpers import check_exist
from src.api.schemas import DefaultResponse, PhoneAddress
from src.db.queries import get_data, set_data, update_data


router = APIRouter(tags=['api'])


@router.get("/check_data")
async def get_query(phone: str) -> DefaultResponse:
    """
    Получение данных
    :param phone: номер телефона
    """
    try:
        logging.info(f"Check data for phone - {phone}.")
        address = await get_data(phone)
        if address is None:
            return DefaultResponse(error=True, message='Phone not find in redis.', payload=None)
        return DefaultResponse(error=False, message="ok", payload=PhoneAddress(phone=phone, address=address))
    except Exception as err:
        logging.error(err)
        return DefaultResponse(error=True, message=err, payload=None)


@router.post("/write_data")
async def get_query(data: PhoneAddress) -> DefaultResponse:
    """
    Добавление данных
    :param data: тело запроса, содержащее phone (номер телефона) и address (адрес)
    """
    try:
        logging.info(f"Write data - {data}.")
        if await check_exist(data.phone):
            return DefaultResponse(error=True, message='Phone already exists in redis.', payload=None)
        await set_data(data.phone, data.address)
        return DefaultResponse(error=False, message="ok", payload=None)
    except Exception as err:
        logging.error(err)
        return DefaultResponse(error=True, message=err, payload=None)


@router.patch("/write_data")
async def get_query(data: PhoneAddress) -> DefaultResponse:
    """
    Обновление данных
    :param data: тело запроса, содержащее phone (номер телефона) и address (адрес)
    """
    try:
        logging.info(f"Update data - {data}.")
        if not await check_exist(data.phone):
            return DefaultResponse(error=True, message='Phone not find in redis.', payload=None)
        await update_data(data.phone, data.address)
        return DefaultResponse(error=False, message="ok", payload=None)
    except Exception as err:
        logging.error(err)
        return DefaultResponse(error=True, message=err, payload=None)


