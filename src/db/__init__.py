import redis

redis_ = redis.StrictRedis(
    host='redis',
    port=6379,
    charset="utf-8",
    decode_responses=True
)
