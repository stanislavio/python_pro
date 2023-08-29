
from fastapi import FastAPI, Body, Depends, Query

app = FastAPI()


@app.get('/hello')
async def hello():
    return 'Hello, world!'


@app.get('/some_endpoint')
async def some_func(some_value: str = Query()):
    return {
        'sd': 'adf',
        'result': some_value
    }

