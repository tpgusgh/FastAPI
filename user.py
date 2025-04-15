from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()

# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="templates")

# 요청 데이터 모델
class User(BaseModel):
    username: str
    age: int

@app.post("/users/", response_class=HTMLResponse)
async def create_user(request: Request, user: User):
    user_dict = user.model_dump()

    return templates.TemplateResponse(
        name="user_details.html",
        context={"request": request, "user": user, "user_dict": user_dict}
    )
