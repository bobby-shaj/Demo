import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()

# app.mount("/build", StaticFiles(directory="build", html=True), name="build")


@app.get("/")
async def home():
    # return {"text": "Babak!"}
    return RedirectResponse(url="/index.html")

app.mount("/", StaticFiles(directory="build/", html=True), name="build")
