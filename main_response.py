#main_response.py

from fastapi import FastAPI, Form, status
from fastapi.responses import (
    JSONResponse,
    HTMLResponse,
    RedirectResponse
)

from pydantic import BaseModel

app = FastAPI()

#response_class는 default가 JSONResponse. response_class가 HTMLResponse일 경우 아래 코드는?
@app.get("/resp_json/{item_id}", response_class=JSONResponse)
async def response_json(item_id: int, q: str | None = None):
    return JSONResponse(content={"message": "Hello World",
                                 "item_id": item_id,
                                 "q": q}, status_code=status.HTTP_200_OK)


#main_response.py

@app.get("/resp_html/{item_id}", response_class=HTMLResponse)
async def response_html(item_id: int, item_name: str | None = None):
    html_str = f'''
    <html>
    <body>
        <h2>HTML Response</h2>
        <p>item_id: {item_id}</p>
        <p>item_name: {item_name}</p>
    </body>
    </html>
    '''
    return HTMLResponse(html_str, status_code=status.HTTP_200_OK)


# main_response.py

# Redirect(Get -> Get)
@app.get("/redirect")
async def redirect_only(comment: str | None = None):
    print(f"redirect {comment}")

    return RedirectResponse(url=f"/resp_html/3?item_name={comment}")



#main_response

# Redirect(Post -> Get)
@app.get("/create_redirect")
async def create_item(item_id: int = Form(), item_name: str = Form()):
    print(f"item_id: {item_id} item name: {item_name}")

    return RedirectResponse(url=f"/resp_html/{item_id}?item_name={item_name}", status_code= 303)
# PRG 패턴 적용 ( 새로고침시 중복요청방지 ex) 계속 똑같은 송금요청)

#main_response.py

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float | None = None

class ItemResp(BaseModel):
    name: str
    description: str
    price_with_tax: float

@app.get("/")
def hello():
    return {hello}


@app.post("/item",response_model=ItemResp)
async def response_json(item_id: int, q: str | None = None):
    return JSONResponse(content={"message": "Hello World",})
