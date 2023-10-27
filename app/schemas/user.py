from pydantic import BaseModel, Field, EmailStr, validator

from app.schemas.model import GeneralResponse


class UserBase(BaseModel):
    email: EmailStr
    names: str | None
    last_names: str | None
    identification: str
    age: int | None
    is_superuser: bool


class UserCreate(UserBase):
    password: str | None

    @validator("password", pre=True, always=True)
    def get_password(cls, v, values):
        return v if v else values["identification"]


class UserUpdate(BaseModel):
    email: str | None
    names: str | None
    last_names: str | None
    identification: str | None
    age: int | None


class UserCreateInDB(UserBase):
    hashed_password: str


class UserInDB(GeneralResponse, UserBase):
    active: bool


class UserSearch(BaseModel):
    names__icontains: str | None = Field(None, alias="names")
    email__icontains: str | None = Field(None, alias="email")

    class Config:
        allow_population_by_field_name = True
