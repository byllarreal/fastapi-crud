from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
     id:Optional[int]
     email: Optional[str]
     password:Optional[str]
     is_active: Optional[bool]
     items: Optional[list[Item]] = []


class ItemUpdate(BaseModel):
    id: str 
    title: str 
    discription: str
    owner_id: int 