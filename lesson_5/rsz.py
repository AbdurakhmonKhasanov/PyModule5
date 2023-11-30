import redis

cache = redis.Redis(host ='localhost', port = 6379, decode_responses=True)

# cache.set("key1", "value1")
# cache.get("key1")
# cache.hset("user1", mapping = {"name" : "Kamol", "age": 24})
# print(cache.hgetall("user1"))

# cache.hset("users: 1", mapping = {"name" : "Kamol", "age": 24})
# cache.hset("users: 2", mapping = {"name" : "Kamol", "age": 24})
# print(cache.hget("user1", "age"))
#
# cache.mset({"key1": 1 , "key2":2, "key3" : 3})
# print(cache.get("key3"))

# print(cache.keys())
# print(cache.hkeys('user1'))

# cache.delete(*cache.keys())
# print(cache.keys())

# cache.set("key1", 1, ex=10)
# print(cache.get("key1"))

# cache.set("key1" , 1, )
# while True:
#     fullnmae=input("Fullname: ")
#     username = input("Username: ")
#     password = input("Password: ")
#     if username and password cache da bor bolsa :
#         print(cache dagi malumot)
#     else:
#         data = database.select
#         cache.set(data, ex = 10)
#         print(data)
