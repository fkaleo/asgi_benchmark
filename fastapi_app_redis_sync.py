import redis
from fastapi import FastAPI

app = FastAPI()

r = redis.Redis()

@app.get("/")
def root():
    r.set('hello', 'world')
    value = r.get('hello')
    return value
