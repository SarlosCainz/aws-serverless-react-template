from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from api.auth import router as auth_router
from api.api_doc import router as doc_router
from api.config import settings


app = FastAPI()
if settings.allow_origin is not None:
    app.add_middleware(CORSMiddleware, allow_origins=settings.allow_origin, allow_methods=["*"],
                       allow_credentials=True, allow_headers=["*"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(auth_router, tags=["auth"], prefix="/auth")
app.include_router(doc_router, tags=["doc"], prefix="/doc")
handler = Mangum(app)
