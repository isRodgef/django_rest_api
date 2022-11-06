from redis import StrictRedis
from redis_cache import RedisCache
from app.settings import REDIS_HOST


client = StrictRedis(host=REDIS_HOST, decode_responses=True)
function_cache = RedisCache(redis_client=client)
