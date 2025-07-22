# Django Book Management System

This is a simple Django project for managing books and user accounts.

## Features

- User authentication (signup, login)
- Book listing
- Add, edit, and delete books

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd gemini-cli-tutorial
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You might need to create a `requirements.txt` file if it doesn't exist by running `pip freeze > requirements.txt`)*

4.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

## Project Structure

-   `accounts/`: Handles user authentication and authorization.
-   `books/`: Manages book-related functionalities.
-   `myproject/`: Main project settings and URL configurations.
-   `templates/`: Global HTML templates.

