FastAPI Task API

This is a simple RESTful Task Management API built with FastAPI. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks. It uses Pydantic for data validation and FastAPI for the web framework.

Features:

* GET /tasks - Get a list of all tasks
* GET /tasks/{task_id} - Get a specific task by its ID
* POST /tasks - Create a new task
* PUT /tasks/{task_id} - Update a task by ID
* DELETE /tasks/{task_id} - Delete a task by ID

Requirements:

* Python 3.7 or later
* FastAPI
* Uvicorn (ASGI server)
* Pydantic for data validation

Installation:

Step 1: Clone the repository

Clone this repository to your local machine:

git clone https://github.com/your-username/rest_api.git

Step 2: Install dependencies

Navigate to the project directory and install the required dependencies:

cd fastapi-task-api pip install -r requirements.txt

Step 3: Run the application

Run the FastAPI app using Uvicorn:

uvicorn app.main:app --reload

The application will be accessible at http://127.0.0.1:8000.

Step 4: Access API Documentation

FastAPI provides an interactive API documentation via Swagger UI. You can access it at:

http://127.0.0.1:8000/docs

You can also explore the OpenAPI schema at:

http://127.0.0.1:8000/openapi.json

Endpoints:

1. GET /tasks
   
Get a list of all tasks.

Response:

{ "tasks": [ { "id": 1, "title": "Learn FastAPI", "status": "pending" }, { "id": 2, "title": "Build REST API", "status": "in progress" } ] }

2. GET /tasks/{task_id}
   
Get a specific task by ID.

Example:

GET http://127.0.0.1:8000/tasks/1

Response:

{ "task": { "id": 1, "title": "Learn FastAPI", "status": "pending" } }

3. POST /tasks

Create a new task. You must provide a title, and the status is optional (defaults to “pending”).

Request:

POST http://127.0.0.1:8000/tasks Content-Type: application/json

{ "title": "New Task", "status": "in progress" }

Response: { "message": "Task added", "task": { "id": 3, "title": "New Task", "status": "in progress" } }

4. PUT /tasks/{task_id}

Update a task by its ID. You must provide the new title and status.

Request:

PUT http://127.0.0.1:8000/tasks/1 Content-Type: application/json

{ "title": "Updated Task", "status": "completed" }

Response:

{ "message": "Task updated", "task": { "id": 1, "title": "Updated Task", "status": "completed" } }

6. DELETE /tasks/{task_id}
   
Delete a task by its ID.

Request:

DELETE http://127.0.0.1:8000/tasks/1

Response:

{ "message": "Task deleted" }

Example Requests:

You can test these endpoints using tools like Postman, curl, or directly via FastAPI’s interactive docs.
Create a Task
curl -X POST "http://127.0.0.1:8000/tasks" -H "Content-Type: application/json" -d '{"title": "Learn FastAPI", "status": "in progress"}'
Update a Task
curl -X PUT "http://127.0.0.1:8000/tasks/1" -H "Content-Type: application/json" -d '{"title": "Learn FastAPI", "status": "completed"}'
Delete a Task
curl -X DELETE "http://127.0.0.1:8000/tasks/1"
