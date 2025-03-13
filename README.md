# To-Do Web App
A modern task management application built with Django featuring a beautiful pastel UI with light/dark theme and user authentication.

![To-Do Web App](https://github.com/arceuzvx/To-Do-Web-App/raw/main/static/img/screenshot.png)

## Features
- User authentication (login/signup/logout)
- Create, read, update, and delete tasks
- Mark tasks as complete/incomplete with animated checkboxes
- Light and dark theme toggle with persistent preferences
- Modern UI with pastel colors and SVG icons
- Responsive design for mobile and desktop
- Interactive animations and transitions

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation
1. Clone the repository
   ```bash
   git clone https://github.com/arceuzvx/To-Do-Web-App.git
   cd To-Do-Web-App
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables (optional but recommended)
   - Create a `.env` file in the project root
   - Add the following line:
     ```
     DJANGO_SECRET_KEY=your_secret_key_here
     ```
   - If not set, a random key will be generated for development

6. Run migrations
   ```bash
   python manage.py migrate
   ```

7. Create a superuser (admin account)
   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server
   ```bash
   python manage.py runserver
   ```

9. Access the application at http://127.0.0.1:8000/

## Usage Guide

### User Authentication
1. **Sign Up**: Create a new account by clicking "Sign Up" in the navigation bar
2. **Login**: Access your tasks by logging in with your credentials
3. **Logout**: End your session by clicking "Logout" in the navigation bar

### Managing Tasks
1. **View Tasks**: All your tasks are displayed on the home page after login
2. **Add Task**: 
   - Click "Add Task" button at the top of the page
   - Fill in the title and optional description
   - Click "Save" to create the task

3. **Complete Task**: 
   - Click the circle checkbox next to a task to mark it as complete
   - The task will be visually marked with a strikethrough
   - Click again to mark as incomplete

4. **Edit Task**:
   - Click the pencil icon on any task
   - Update the title or description
   - Click "Save" to update the task

5. **Delete Task**:
   - Click the trash icon on any task
   - Confirm deletion on the confirmation page

### Theme Toggle
- Click the "Light Mode" or "Dark Mode" button in the navigation bar to switch themes
- Your preference will be remembered for future sessions

## Customization

### Changing Colors
The application uses a pastel color scheme defined in `static/css/style.css`. You can modify the color variables in the `:root` selector:

```css
:root {
    /* Pastel color palette */
    --pastel-primary: #a5d8ff;
    --pastel-secondary: #d0bfff;
    --pastel-success: #b2f2bb;
    --pastel-danger: #ffc9c9;
    /* Add or modify colors as needed */
}
```

### Adding New Features
The application follows Django's MVT (Model-View-Template) architecture:
- Models are defined in `todo_app/models.py`
- Views are defined in `todo_app/views.py`
- Templates are in the `templates/` directory
- URLs are configured in `todo_app/urls.py`

## Deployment
For production deployment:
1. Set `DEBUG = False` in `todo_project/settings.py`
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up a production database (PostgreSQL recommended)
4. Use a proper web server (Nginx, Apache) with WSGI
5. Set environment variables securely

## Technologies Used
- Django 5.1.7
- HTML5/CSS3/JavaScript
- Bootstrap 5.3
- SQLite (default database)
- SVG icons

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- Bootstrap for the responsive framework
- SVG icons for the modern UI elements
- Django community for the excellent documentation
