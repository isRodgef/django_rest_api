How to scale the service to work with large file inputs 

I currently use redis to cache api calls so I do not have to fetch the results for exchange rates as often.

I could also used redis as a task or message queue where all the validated data goes into  a redis streams and is read by some listener like rq or a python script/job which uses a library like [redis-streams] (https://pypi.org/project/redis-streams/) por something like celery to create a pub/sub or producer/consumer like system which listens on redis gets value from stream and places into the db without forcing the user of the api to wait for a db query to complete