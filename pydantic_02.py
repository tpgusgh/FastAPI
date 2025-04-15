# pydantic_02.py

from pydantic import BaseModel, ValidationError
from typing import List, Optional
import json


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # Optional[int] = None


class UserClass:
    def __init__(self, id: int, name: str, email: str, age: int):
        self.id = id
        self.name = name
        self.email = email
        self.age = age

    def get_info(self):
        return f"id: {self.id}, name: {self.name}"

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, email: {self.email}, age: {self.age}"


userobj = UserClass(10, 'test_name', 'tname@example.com', 40)
print("userobj:", userobj, userobj.id)

user = User(id=10, name="test_name", email="tname@example.com", age=40)
print("user:", user, user.id)

user_from_dict = User(**{"id": 10, "name": "test_name", "email": "tname@example.com", "age": 40})
print("user_from_dict:", user_from_dict, user_from_dict.id)

json_string = '{"id": 10, "name": "test_name", "email": "tname@example.com", "age": 40}'
json_dict = json.loads(json_string)
user_from_json = User(**json_dict)
print("user_from_json:", user_from_json, user_from_json.id)


class AdvancedUser(User):
    advanced_level: int


adv_user = AdvancedUser(id=10, name="test_name", email="tname@example.com", age=40, advanced_level=9)
print("adv_user:", adv_user)


class Address(BaseModel):
    street: str
    city: str


class UserNested(BaseModel):
    name: str
    age: int
    address: Address


json_string_nested = '{"name": "John Doe", "age": 30, "address": {"street": "123 Main St", "city": "Anytown"}}'
json_dict_nested = json.loads(json_string_nested)

user_nested_01 = UserNested(**json_dict_nested)
print("user_nested_01:", user_nested_01, user_nested_01.address, user_nested_01.address.city)

user_nested_02 = UserNested(
    name="test_name", age=40, address={"street": "123 Main St", "city": "Anytown"}
)
print("user_nested_02:", user_nested_02, user_nested_02.address, user_nested_02.address.city)

user_dump_01 = user.model_dump()
print(user_dump_01, type(user_dump_01))

user_dump_02 = user.model_dump_json()
print(user_dump_02, type(user_dump_02))