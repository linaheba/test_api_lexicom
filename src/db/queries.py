# Взаимодействие с Redis
from src.db import redis_ as redis
from src.logger import logging


async def set_data(name: str, value: str):
    """
    Добавление данных в redis
    :param name: ключ (номер телефона)
    :param value: значение (адрес)
    """
    logging.info(f"set data {name}: {value}.")
    redis.set(name, value)
    logging.info("set data - success!")


async def update_data(name: str, value: str):
    """
    Обновление данных в redis
    :param name: ключ (номер телефона)
    :param value: значение (адрес)
    """
    logging.info(f"update data {name}: {value}.")
    redis.set(name, value)
    logging.info("update data - success!")


async def get_data(name: str):
    """
    Получение данных из redis
    :param name: ключ (номер телефона)
    """
    logging.info(f"get data for key {name}.")
    data = redis.get(name)
    logging.info("get data - success!")
    return data
