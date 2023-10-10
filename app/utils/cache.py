import redis

class Cache:
    def __init__(self):
        self.client = None

    def connect(self):
        self.client = redis.Redis(host='localhost', port=6379, db=0)

    def exists(self, key):
        return self.client.exists(key)

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value):
        self.client.set(key, value)
