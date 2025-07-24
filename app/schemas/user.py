from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password : str
    pass

class UserResponse(UserBase):
    id: int

    model_config = {'from_attributes': True}
