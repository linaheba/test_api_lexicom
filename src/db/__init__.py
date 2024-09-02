# Подключение к Redis
import dotenv
import os
import redis

dotenv.load_dotenv()

redis_ = redis.StrictRedis(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    charset="utf-8",
    decode_responses=True
)
