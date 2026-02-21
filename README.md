# Archival Platform - A platform to centralize and manage very easily your content, sources and images for EUSTORY 2026

This project is a Django-based web application designed to centralize and manage content, sources, and images for the EUSTORY 2026 initiative. It provides an API for handling various aspects of project management, including subthemes, sections, content blocks, and sources.

## Features

- **Subtheme Management**: Create and manage subthemes for different projects.
- **Section Management**: Organize content into sections within subthemes.
- **Content Block Management**: Create and manage content blocks that can be associated with sections.
- **Source Management**: Manage sources that can be linked to content blocks.
- **Authentication**: Secure API endpoints with JWT authentication.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/GdXcIi/archival.git
   cd archival
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv .venv
   ```

    - On Windows:

      ```powershell
      .venv\Scripts\activate
      ```

    - On Linux or MacOS:

      ```bash
      source .venv/bin/activate
      ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin interface:

    ```bash
    python manage.py createsuperuser
    ```

    Then follow the prompts to set up your admin user.

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application:
    - Frontend: `http://localhost:8000/`
    - API endpoints: `http://localhost:8000/api/`
    - Admin interface: `http://localhost:8000/admin/`