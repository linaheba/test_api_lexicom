import dotenv
import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.logger import logging
from src.api.routers import router
from src.api.schemas import DefaultResponse

dotenv.load_dotenv()

app = FastAPI(
    debug=True,
    title='a',
    version='1',
)


@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    """Обработчик внезапных исключений."""
    try:
        return await call_next(request)
    except Exception as exc:
        logging.error(f"Unexpected error on {request.url}: {exc}", exc_info=exc)
        return JSONResponse(
            DefaultResponse(error=True, message=str(exc), payload=None).dict(), status_code=200)


app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'], )

app.include_router(router)
