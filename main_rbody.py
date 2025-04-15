from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


# Pydantic 모델 정의
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str


class UpdateRequest(BaseModel):
    item: Item
    user: User



@app.post("/items")
async def create_item(item: Item):
    print("###### item type:", type(item))
    print("###### item:", item)
    return item



@app.post("/items_tax/")
async def create_item_tax(item: Item):
    item_dict = item.model_dump()
    print("#### item_dict:", item_dict)
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict



@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    request: UpdateRequest = Body(...)
):
    result = {
        "item_id": item_id,
        "item": request.item.model_dump(),
        "user": request.user.model_dump(),
    }
    print("#### result:", result)
    return result
