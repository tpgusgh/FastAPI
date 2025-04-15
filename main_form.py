#main_form.py
from pydantic import BaseModel
from typing import Optional, Annotated

from fastapi import FastAPI, Form

app = FastAPI()

# 개별 Form data 값을 Form()에서 처리하여 수행함수 적용.
# Form()은 form data값이 반드시 입력되어야 함. Form(None)과 Annotated[str, Form()] = None은 Optional
@app.post("/login")
async def login(username: str = Form(),
                email: str = Form(),
                country: Annotated[str, Form()] = None):
    return {"username": username,
            "email": email,
            "country": country}


#main_form.py
# path, query parameter와 함께
@app.post("/login_pq/{login_gubun}")
async def login(login_gubun: int, q: str | None = None,
                username: str = Form(),
                email: str = Form(),
                country: Annotated[str, Form()] = None):
    return {"login_gubun": login_gubun,
            "q": q,
            "username": username,
            "email": email,
            "country": country}