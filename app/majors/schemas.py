from pydantic import BaseModel, Field

class SMajorsAdd(BaseModel):
    major_name: str = Field(..., description="Name of the major")
    major_description: str = Field(None, description="Description of the major")
    count_students: int = Field(0, description="Number of students")


class SMajorsUpdDesc(BaseModel):
    major_name: str = Field(..., description="Name of the major")
    major_description: str = Field(None, description="New description of the major")