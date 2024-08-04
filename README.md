# FastAPI 

Welcome to the FastAPI! This application provides a robust and flexible framework for managing student information, user authentication, and more.

## Features

- **User Authentication**: Secure registration and login functionality using JWT tokens.
- **CRUD Operations**: Create, read, update, and delete operations for managing student information.
- **Role-Based Access Control**: Different levels of access for users and administrators.
- **Swagger UI**: Auto-generated interactive API documentation.
- **Docker Support**: Easy setup and deployment using Docker and Docker Compose.
- **Database Migrations**: Version-controlled database schema changes using Alembic.


### Prerequisites

- Python 3.8+
- Docker (optional, for containerization)
  
### Steps

1. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. **Install the dependencies:**

    ```sh
    pip install -r req.txt
    ```

3. **Set up the database:**

    ```sh
    alembic upgrade head
    ```

4. **Run the application:**

    ```sh
    uvicorn app.main:app --reload
    ```

5. **(Optional) Using Docker:**

    ```sh
    docker-compose up --build
    ```

## Usage

- Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI for API documentation.
- Use the endpoints to register users, log in, and manage student records.

## API Endpoints

### Authentication

- **Register**: `POST /auth/register`
- **Login**: `POST /auth/login`
- **Logout**: `POST /auth/logout`

### Students

- **Get All Students**: `GET /students`
- **Get Student by ID**: `GET /students/{student_id}`
- **Create Student**: `POST /students`
- **Update Student**: `PUT /students/{student_id}`
- **Delete Student**: `DELETE /students/{student_id}`

### Majors

- **Get All Majors**: `GET /majors`
- **Get Major by ID**: `GET /majors/{major_id}`
- **Create Major**: `POST /majors`
- **Update Major**: `PUT /majors/{major_id}`
- **Delete Major**: `DELETE /majors/{major_id}`

## Database Configuration

To connect to a different database, update the `DATABASE_URL` in `app/config.py`:

```python
DATABASE_URL = "postgresql://user:password@localhost/dbname"
or DATABASE_URL = "mysql+pymysql://user:password@localhost/dbname"

Install the required driver for your database:

pip install psycopg2-binary  # For PostgreSQL
pip install pymysql  # For MySQL
Run migrations for the new database:


Copy code
alembic upgrade head








