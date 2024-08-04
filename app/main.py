from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.students.router import router as router_students
from app.majors.router import router as router_majors
from app.users.router import router as router_users
from app.pages.router import router as router_pages

app = FastAPI()

app.mount('/static', StaticFiles(directory='app/static'), name='static')

@app.get("/")
def home_page():
    return {"message": "Hello!"}

app.include_router(router_users)
app.include_router(router_students)
app.include_router(router_majors)
app.include_router(router_pages)



