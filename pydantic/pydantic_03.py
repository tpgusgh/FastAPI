#pydantic_03.py

from pydantic import BaseModel, ValidationError, ConfigDict, Field, Strict
from typing import List, Annotated

class Address(BaseModel):
    street: str
    city: str
    country: str

class User(BaseModel):
    id: int
    name: str
    email: str
    addresses: List[Address]
    age: int | None = None # Optional[int] = None

try:
    user = User(
        id="123",
        name="John Doe",
        email="john.doe@example.com",
        addresses=[{"street": "123 Main St", "city": "Hometown", "country": "USA"}],
        age="29"
    )
    print(user)
except ValidationError as e:
    print("validation error happened")
    print(e)
