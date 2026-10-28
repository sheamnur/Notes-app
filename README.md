# Notes Management API

A RESTful Notes Management API built with Python, FastAPI, and PostgreSQL.

This project was developed for educational purposes as part of my journey in backend development. It demonstrates practical experience with REST API development, PostgreSQL integration, request validation, and database operations using FastAPI.

## Features

- Create new notes
- Retrieve all notes
- Search notes by ID
- Search notes by title
- Update existing notes
- Delete notes
- View deleted-note history
- View note-update history
- Store and manage notes using PostgreSQL
- Validate request data using Pydantic

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Database Driver:** Psycopg
- **Data Validation:** Pydantic
- **Environment Variables:** python-dotenv
- **ASGI Server:** Uvicorn

## Project Structure

```text
Note app/
├── app.py
├── database.py
├── note.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites

Before running this project, make sure you have installed:

- Python
- PostgreSQL
- pip

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory and configure your PostgreSQL connection details.

Example:

```env
host=localhost
dbname=notesystem
user=YOUR_POSTGRESQL_USERNAME
password=YOUR_POSTGRESQL_PASSWORD
```

Replace the example values with your own database configuration. The variable names must match those used in `database.py`.

**Security note:** Never commit your `.env` file or expose your database credentials on GitHub.

### 5. Set Up the Database

Create a PostgreSQL database named `notesystem`.

Ensure that the tables required by the application have been created using the appropriate SQL statements.

### 6. Run the Application

Start the FastAPI development server:

```bash
uvicorn app:app --reload
```

The application will be available at:

`http://127.0.0.1:8000`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/notes` | Create a new note |
| GET | `/notes` | Retrieve all notes |
| GET | `/notes/id/{note_id}` | Retrieve a note by ID |
| GET | `/notes/title/{title}` | Search for a note by title |
| PATCH | `/notes/{note_id}` | Update an existing note |
| DELETE | `/notes/{note_id}` | Delete a note |
| GET | `/notes/deleted` | Retrieve deleted-note history |
| GET | `/notes/updated` | Retrieve note-update history |

## API Documentation

FastAPI automatically generates interactive API documentation.

After starting the server, open either of these URLs in your browser:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Use these interfaces to explore the available endpoints and test HTTP requests.

## Learning Objectives

Through this project, I practiced:

- Developing RESTful APIs with FastAPI
- Working with HTTP methods and endpoints
- Validating request data with Pydantic
- Connecting Python applications to PostgreSQL
- Performing database CRUD operations
- Managing environment variables
- Maintaining note-update and deletion history

## Future Improvements

- Add automated tests using pytest
- Implement authentication and authorization
- Introduce pagination and filtering
- Improve API response consistency and error handling
- Deploy the API to a hosting platform

## Author

**Sheam Nur**

GitHub: [@sheamnur](https://github.com/sheamnur)
