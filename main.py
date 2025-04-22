# FastAPI import
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from routers import user
from routers import item

import asyncio
import time
# FastAPI instance 생성.
app = FastAPI()
app.include_router(user.router)
app.include_router(item.router)
@app.get("/", summary="간단한 API", tags=["simple"])
def root():
    '''
    간단한 API
    - 인자값 1은 ~
    - 인자값 2는 ~
    '''
    return {"message": "Hello World"}
@app.get("/home")
def home():
    '''
        간단한
    '''
    return "dd"

@app.get("/data")
def data():
    test = "gang gang gang"
    ppt(test)
    return "dd"

@app.get("/home/ppt")
def ppt(t):
    print(t)
    return "t"

# http://localhost:8081/items/3
# decorator에 path값으로 들어오는 문자열중에
# format string { }로 지정된 변수가 path parameter
@app.get("/{item_id}")
# 수행 함수 인자로 path parameter가 입력됨.
# 함수 인자의 타입을 지정하여 path parameter 타입 지정.
def read_item(item_id: int):
    return {"item_id": item_id}

# Path parameter값과 특정 지정 Path가 충돌되지 않도록 endpoint 작성 코드 위치에 주의
@app.get("/items/all")
# 수행 함수 인자로 path parameter가 입력됨. 함수 인자의 타입을 지정하여 path parameter 타입 지정.
def read_all_items():
    return {"message": "all items"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# http://localhost:8081/items?skip=0&limit=2
@app.get("/items")
# 함수에 개별 인자값이 들어가 있는 경우 path parameter가 아닌 모든 인자는 query parameter
# query parameter의 타입과 default값을 함수인자로 설정할 수 있음.
async def read_item(skip: int = 0, limit: int = 2):
    return fake_items_db[skip: skip + limit]


templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    name: str
    price: float


@app.get("/ad/items/{id}", response_class=HTMLResponse)
# template engine을 사용할 경우 반드시 Request 객체가 인자로 입력되어야 함.
async def read_item(request: Request, id: str, q: str | None = None):
    # 내부에서 pydantic 객체 생성.
    item = Item(name="test_item", price=10)
    # pydantic model값을 dict 변환.
    item_dict = item.model_dump()

    return templates.TemplateResponse(
        request=request,
        name="item.html",
        context={"id": id, "q_str": q, "item": item, "item_dict": item_dict}
)



@app.get("/item_gubun")
async def read_item_by_gubun(request: Request, gubun: str):
    item = Item(name="test_item_02", price=4.0)

    return templates.TemplateResponse(
        request=request,
        name="item-gubun.html",
        context={"gubun": gubun, "item": item}
    )

@app.get("/read_safe", response_class=HTMLResponse)
async def read_safe(request: Request):
    html_str = '''
    <ul>
    <li>튼튼</li>
    <li>저렴</li>
    </ul>
    '''
    return templates.TemplateResponse(
        request=request,
        name="read_safe.html",
        context={"html_str": html_str}
    )


# long-running I/O-bound 작업 시뮬레이션
async def long_running_task():
    # 특정 초동안 수행 시뮬레이션
    await asyncio.sleep(20)
    return {"status": "long_running task completed"}


# @app.get("/task")
# async def run_task():
#     result = await long_running_task()
#     return result


# @app.get("/quick")
# async def quick_response():
#     return {"status": "quick response"}
#
#
@app.get("/task")
async def run_task():
    time.sleep(20)
    return {"status": "long_running task completed"}


@app.get("/quick")
async def quick_response():
    return {"status": "quick response"}
