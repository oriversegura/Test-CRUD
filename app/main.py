from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# Define html templating
templates = Jinja2Templates(directory="templates")

# instance app
app = FastAPI()

# Mount Static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/user", response_class=HTMLResponse)
async def read_user(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
