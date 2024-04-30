# uvicorn main:app --reload # was 실행

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from backend.routes import kakao

app = FastAPI()
templates = Jinja2Templates(directory="templates/") # Jinja2를 사용할 것이고 HTML파일은 templates 하위에 있다
app.mount("/static", StaticFiles(directory="static"), name="static") # app을 실행할 때 정적인 파일은 static에서 mount한다

app.include_router(kakao.router, prefix="/kakao")

@app.get("/")   # http://127.0.0.1:8000/
async def welcome(request : Request):
    return templates.TemplateResponse("index.html", {"request": request})   # client가 uvicorn에게 request한다 이때 Templates를 전달

