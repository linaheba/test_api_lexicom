# Схемы для апи
from typing import Optional, Any
from pydantic import BaseModel


class DefaultResponse(BaseModel):
    """Стандартный ответ от API."""
    error: bool
    message: Optional[str]
    payload: Optional[Any]


class PhoneAddress(BaseModel):
    """Модель для текущей задачи, содержащая номер телефонра и адрес."""
    phone: str
    address: str
