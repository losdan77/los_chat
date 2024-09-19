from pydantic import BaseModel, EmailStr
from typing import Optional

class SUserRegistr(BaseModel):
    email: EmailStr
    username: str


class SUserLogin(BaseModel):
    email: EmailStr
    password: str