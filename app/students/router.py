# students/router.py
from fastapi import APIRouter, Depends
from app.students.dao import StudentDAO
from app.students.rb import RBStudent
from app.students.schemas import SStudent, SStudentAdd



router = APIRouter(prefix='/students', tags=['Work with students'])

@router.get("/", summary="Get all students")
async def get_all_students(request_body: RBStudent = Depends()) -> list[SStudent]:
    return await StudentDAO.find_students(**request_body.to_dict())

@router.get("/{student_id}", summary="Get student by ID", response_model=SStudent | dict)
async def get_student_by_id(student_id: int) -> SStudent | dict:
    rez = await StudentDAO.find_full_data(student_id)
    if rez is None:
        return {'message': f'Student with ID {student_id} not found!'}
    return rez

@router.get("/by_filter", summary="Get student by filter", response_model=SStudent | dict)
async def get_student_by_filter(request_body: RBStudent = Depends()) -> SStudent | dict:
    rez = await StudentDAO.find_one_or_none(**request_body.to_dict())
    if rez is None:
        return {'message': f'Student with specified parameters not found!'}
    return rez


@router.post("/add/")
async def add_student(student: SStudentAdd) -> dict:
    check = await StudentDAO.add_student(**student.dict())
    if check:
        return {"message": "Student added successfully!", "student": student}
    else:
        return {"message": "Error adding student!"}

@router.delete("/delete/{student_id}")
async def delete_student_by_id(student_id: int) -> dict:
    check = await StudentDAO.delete_student_by_id(student_id=student_id)
    if check:
        return {"message": f"Student with ID {student_id} deleted successfully!"}
    else:
        return {"message": "Error deleting student!"}