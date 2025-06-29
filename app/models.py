# Modelos de datos, definicion de clases y relaciones.

from Pydantic import BaseModel 
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
 

class UserCreate(UserBase):
    username: str
    password: str

class User(UserBase)
    id: int

    class Config:
        form_atributes = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    