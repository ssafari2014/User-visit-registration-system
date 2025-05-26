import redis.asyncio as redis

redis_Client = redis.StrictRedis(host="localhost", port=6379, decode_responses=True, db=0)
