import re

from pydantic import BaseModel, EmailStr, Field, field_validator
class SUserRegister(BaseModel):
    email: EmailStr = Field(..., description="Email")
    password: str = Field(..., min_length=5, max_length=50, description="Password, 5 to 50 characters")
    phone_number: str = Field(..., description="Phone number in international format starting with '+'")
    first_name: str = Field(..., min_length=3, max_length=50, description="First name, 3 to 50 characters")
    last_name: str = Field(..., min_length=3, max_length=50, description="Last name, 3 to 50 characters")

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value: str) -> str:
        if not re.match(r'^\+\d{5,15}$', value):
            raise ValueError('Phone number must start with "+" and contain 5 to 15 digits')
        return value



class SUserAuth(BaseModel):
    email: EmailStr = Field(..., description="Email")
    password: str = Field(..., min_length=5, max_length=50, description="Password, 5 to 50 characters")