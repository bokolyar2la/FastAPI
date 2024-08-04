from datetime import datetime, date
from typing import Optional
import re

from pydantic import BaseModel, Field, field_validator, EmailStr, ConfigDict
class SStudent(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    phone_number: str = Field(..., description="Phone number in international format, starting with '+'")
    first_name: str = Field(..., min_length=1, max_length=50, description="Student's first name, 1 to 50 characters")
    last_name: str = Field(..., min_length=1, max_length=50, description="Student's last name, 1 to 50 characters")
    date_of_birth: date = Field(..., description="Student's date of birth in YYYY-MM-DD format")
    email: EmailStr = Field(..., description="Student's email address")
    address: str = Field(..., min_length=10, max_length=200, description="Student's address, up to 200 characters")
    enrollment_year: int = Field(..., ge=2002, description="Year of enrollment, must be no less than 2002")
    major_id: int = Field(..., ge=1, description="Student's major ID")
    course: int = Field(..., ge=1, le=5, description="Course number, must be between 1 and 5")
    special_notes: Optional[str] = Field(None, max_length=500, description="Additional notes, up to 500 characters")
    photo: Optional[str] = Field(None, max_length=100, description="Student's photo")
    major: Optional[str] = Field(..., description="Major name")

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value: str) -> str:
        if not re.match(r'^\+\d{1,15}$', value):
            raise ValueError('Phone number must start with "+" and contain 1-15 digits')
        return value

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value: date):
        if value and value >= datetime.now().date():
            raise ValueError('Date of birth must be in the past')
        return value


class SStudentAdd(BaseModel):
    phone_number: str = Field(..., description="Phone number in international format starting with '+'")
    first_name: str = Field(..., min_length=1, max_length=50, description="First name, 1-50 characters")
    last_name: str = Field(..., min_length=1, max_length=50, description="Last name, 1-50 characters")
    date_of_birth: date = Field(..., description="Date of birth in YYYY-MM-DD format")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., min_length=10, max_length=200, description="Address, max 200 characters")
    enrollment_year: int = Field(..., ge=2002, description="Enrollment year, must be at least 2002")
    major_id: int = Field(..., ge=1, description="ID of the major")
    course: int = Field(..., ge=1, le=5, description="Course, 1-5")
    special_notes: Optional[str] = Field(None, max_length=500, description="Special notes, max 500 characters")

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value: str) -> str:
        if not re.match(r'^\+\d{1,15}$', value):
            raise ValueError('Phone number must start with "+" and contain 1-15 digits')
        return value

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value: date):
        if value and value >= datetime.now().date():
            raise ValueError('Date of birth must be in the past')
        return value


