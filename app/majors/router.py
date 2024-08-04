from fastapi import APIRouter
from app.majors.dao import MajorsDAO
from app.majors.schemas import SMajorsAdd, SMajorsUpdDesc

router = APIRouter(prefix='/majors', tags=['Work with majors'])

@router.post("/add/")
async def add_major(major: SMajorsAdd) -> dict:
    check = await MajorsDAO.add(**major.dict())
    if check:
        return {"message": "Major added successfully!", "major": major}
    else:
        return {"message": "Error adding major!"}

@router.put("/update_description/")
async def update_major_description(major: SMajorsUpdDesc) -> dict:
    check = await MajorsDAO.update(filter_by={'major_name': major.major_name},
                                   major_description=major.major_description)
    if check:
        return {"message": "Major description updated successfully!", "major": major}
    else:
        return {"message": "Error updating major description!"}


@router.delete("/delete/{major_id}")
async def delete_major(major_id: int) -> dict:
    check = await MajorsDAO.delete(id=major_id)
    if check:
        return {"message": f"Major with ID {major_id} deleted successfully!"}
    else:
        return {"message": "Error deleting major!"}