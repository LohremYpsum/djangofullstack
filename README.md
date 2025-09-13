# Django Music Ads

This is a Django project for a simple music ad marketplace. Users can create, browse, and manage ads for various music-related items like vinyl records and CDs. The project includes a custom management command to quickly populate the database with sample data for development and testing.

---

## Getting Started

### Prerequisites

To get started, make sure you have **Python** installed on your system. It's also highly recommended to use a virtual environment to isolate your project's dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

Install dependencies:

```bash
pip install -r requirements.txt
```

(Note: You'll need to create a requirements.txt file by running `pip freeze > requirements.txt` after installing all your project's libraries, such as Django and djangorestframework.)

---

## Essential Commands

These commands are crucial for setting up your database and running the project for the first time.

### 1. Database Migrations

Apply the database migrations to create the necessary tables for your models, ensuring your database schema is up to date.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Populate the Database

Use the custom management command to quickly add a test user, categories, and a sample music ad to your database. This is perfect for local development and testing.

```bash
python manage.py populate_data
```

### 3. Run the Development Server

Start the Django development server to view your project in a web browser.

```bash
python manage.py runserver
```

Once the server is running, you can access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the test user created by the `populate_data` command (**Username:** testuser, **Password:** testpass123).

---

## Project Structure

A brief overview of the key directories:

- **djangofullstack/**: The main project's settings and URL configurations.
- **backend/**: The core application containing models, views, and custom management commands.
- **backend/management/commands/**: The location for custom management commands, like `populate_data.py`.
