from fastapi import APIRouter

router = APIRouter()
@router.get("/users")
async def read_users():
    return {"message": "유저 목록입니다"}

# 파라미터가 있는 GET API 정의 (예: /users/123)
@router.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"message": f"{user_id}번 유저 정보입니다"}



@router.get("/")
async def read_users():
    return [{"username": "Rickie"}, {"username": "Martin"}]
@router.get("/me")
async def read_user_me():
    return {"username": "currentuser"}


@router.get("/{username)", tags=["users"])
async def read_user(username: str):
    return {"username": username}