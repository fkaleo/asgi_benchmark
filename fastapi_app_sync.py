import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    # time.sleep(1)
    return b'Hello, world!'
