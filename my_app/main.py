from typing import Optional
from uuid import uuid4

from contextlogger import CLogVar
from fastapi import FastAPI, Request

from my_app import clogger
from my_app import another_module


app = FastAPI()

clogger.clogvars = [
    # Define a request_id context variable that takes the value of a uuid
    CLogVar(name='request_id', setter=lambda: str(uuid4())),
]


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # Set the request_id value
    clogger.setvar('request_id')

    response = await call_next(request)
    return response


@app.get("/")
async def read_root():
    # Log something
    clogger.info(f"Hello from {read_root.__name__}")

    # Invoke a function from another module that logs something else
    another_module.another_func()

    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    # Log something
    clogger.info(f"Hello from {read_item.__name__}")

    return {"item_id": item_id, "q": q}
