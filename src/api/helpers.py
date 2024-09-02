# Файл со вспомогательными функциями для апи
from src.logger import logging
from src.db.queries import get_data


async def check_exist(name: str):
    """
    Проверка существования записи в redis
    :param name: ключ (номер телефона)
    """
    check = await get_data(name)
    logging.info(f"Exists key {name} - {check}.")
    return True if check is not None else False
