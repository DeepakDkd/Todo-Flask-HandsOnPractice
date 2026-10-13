# Flask Todo App

A simple Todo application built with Flask. It supports creating, viewing, updating, and deleting todo items.

## Features

- Add a todo with a title and description
- View all todos
- Update an existing todo
- Delete a todo
- Store data in a SQLite database

## Tools and technologies

- **Python** – programming language
- **Flask** – web framework
- **Flask-SQLAlchemy** – database integration and ORM
- **SQLite** – local database
- **Jinja2** – HTML templating through Flask
- **HTML and Bootstrap** – user interface
- **Git and GitHub** – version control and source-code hosting
- **Gunicorn** – production WSGI server
- **Render** – deployment platform

## Project structure

```text
todo/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── update.html
└── .gitignore
```

## Run locally

1. Create and activate a virtual environment.

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create the database tables once from a Python shell:

   ```python
   from app import app, db

   with app.app_context():
       db.create_all()
   ```

4. Start the Flask development server:

   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in a browser.

## Deployment on Render

Create a Render **Web Service** connected to this GitHub repository.

Use these settings:

```text
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

Render installs the packages in `requirements.txt` and runs the Flask application with Gunicorn.

## Database note

This project uses SQLite for learning and local development. For production use, a hosted database such as PostgreSQL is recommended.
