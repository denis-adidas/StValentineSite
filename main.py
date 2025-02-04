from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Настройка Jinja2
env = Environment(loader=FileSystemLoader("templates"))

@app.get("/")
async def read_root(request: Request):
    template = env.get_template("index.html")
    return template.render(request=request, title="Выбери свидание!")
    # return "Hello world!"

@app.get("/date/{option}", response_class=HTMLResponse)
async def read_option(request: Request, option: str):
    template = env.get_template("date.html")
    return template.render(request=request, title="Ваш выбор", option=option)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
