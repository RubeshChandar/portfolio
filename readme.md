# Django Portfolio Web Application

A modern and responsive portfolio web application built with Django, showcasing projects, skills, and accomplishments. This application is designed to provide a professional online presence, ideal for developers and freelancers.

## Features

- **Dynamic Portfolio Sections**: Easily manage and display your skills, projects, and work experience through the Django admin interface.
- **Interactive Contact Form**: Allows visitors to send messages directly from the site.
- **Responsive Design**: Fully responsive layout optimized for all devices.
- **SEO Optimized**: Includes meta tags and content structuring for better search engine visibility.
- **Extensible Codebase**: Modular and scalable architecture for easy updates and new feature integration.
- **Admin Dashboard**: Manage content like projects, skills, and personal details with a user-friendly admin panel.

---

## Tech Stack

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default) or PostgreSQL (for production)
- **Styling Framework**: Bootstrap or Tailwind CSS (optional)
- **Hosting**: Compatible with services like Heroku, AWS, or PythonAnywhere Optionally Raspberry pi with dynamic DNS
- **Version Control**: Git and GitHub

---

## Installation

### Prerequisites

- Python 3.8+
- Django 4.x
- Pip (Python package installer)
- Git

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourportfolio.git
   cd yourportfolio
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver

   ```

### Configuration

Customization

- Update your personal details in the Django admin interface.
- Add projects, skills, and contact details through the admin dashboard.

Environment Variables
Create a .env file in the root directory for sensitive configurations:

```bash
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

**### Folder Structure**

```bash
portfolio/
│
├── portfolio/                # Main Django app folder
│   ├── settings.py           # Django settings file
│   ├── urls.py               # URL configurations
│   ├── wsgi.py               # WSGI entry point
│
├── static/                   # Static files (CSS, JS, Images)
├── templates/                # HTML templates
│   ├── base.html             # Base template
│   ├── index.html            # Home/Portfolio page
│   ├── contact.html          # Contact page
│
├── projects/                 # App for handling projects
│   ├── models.py             # Project database models
│   ├── views.py              # Views for the projects
│   ├── templates/            # Templates for project-related pages
│
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── manage.py                 # Django management script
```

###Contact

Feel free to reach out for collaborations or feedback:

- Email: rubeshchandar@gmail.com
- GitHub: @RubeshChandar
- LinkedIn: [linkedin.com/in/rubeshchandar](https://www.linkedin.com/in/rubeshchandar/)
