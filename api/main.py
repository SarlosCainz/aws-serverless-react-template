from fastapi import FastAPI
from mangum import Mangum
from api.foo import router as foo_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(foo_router, tags=["foo"], prefix="/foo")
handler = Mangum(app)
