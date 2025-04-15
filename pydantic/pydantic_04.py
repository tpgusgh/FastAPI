# pydantic_04.py

from pydantic import BaseModel, EmailStr, Field


class UserEmail(BaseModel):
    email: EmailStr  # 문자열 Email 검증.
    # email: EmailStr = Field(..., max_length=40) #Field와 함께 사용.
    # email: EmailStr = Field(None, max_length=40, pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


try:
    user_email = UserEmail(email="user@examples.com")
    print(user_email)
except ValueError as e:
    print(e)

from pydantic import HttpUrl, AnyUrl, AnyHttpUrl, FileUrl


class UserResource(BaseModel):
    http_url: HttpUrl
    any_url: AnyUrl
    any_http_url: AnyHttpUrl
    file_url: FileUrl


try:
    user_resource = UserResource(
        http_url="https://www.example.com",
        any_url="ftp://example.com",
        any_http_url="http://www.example.com",
        file_url="file:///path/to/file.txt"
    )

    print(user_resource, user_resource.http_url)
except ValueError as e:
    print(f"Validation error: {e}")

from pydantic import IPvAnyAddress, IPvAnyNetwork, IPvAnyInterface


class Device(BaseModel):
    ip_address: IPvAnyAddress
    network: IPvAnyNetwork
    interface: IPvAnyInterface


# Example usage
try:
    device = Device(
        ip_address="192.168.1.1",
        network="192.168.1.0/24",
        interface="192.168.1.0/24")
    print(device)
except ValueError as e:
    print(e)

# pip install pydantic-extra-types pycountry
from pydantic_extra_types.country import CountryAlpha3


class Product(BaseModel):
    made_in: CountryAlpha3


product = Product(made_in="USA")
print(product)