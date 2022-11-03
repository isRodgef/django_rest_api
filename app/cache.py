from redis import StrictRedis
from redis_cache import RedisCache

client = StrictRedis(host="127.0.0.1", decode_responses=True)
function_cache = RedisCache(redis_client=client)
