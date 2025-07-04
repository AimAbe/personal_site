# Personal Site with Flask

A personal website built with Flask that includes a portfolio, blog, and contact form.

## Features

- Responsive design using Bootstrap
- Blog section with article management
- Portfolio section to showcase projects
- Contact form
- About page

## Installation

1. Clone the repository
```
git clone https://github.com/aimabe/personal_site.git
cd personal_site
```

2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up the database
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Run the application
```
python run.py
```

## Project Structure

```
project/
├── app/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── blog/
│   │   ├── portfolio/
│   │   ├── about.html
│   │   └── contact.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── routes/
│   ├── models.py
│   ├── forms.py
│   └── __init__.py
├── config.py
└── run.py
```

## Technologies Used

- Flask
- SQLAlchemy
- Flask-Login
- Bootstrap
- SQLite (development) / PostgreSQL (production)

## Deployment

This application can be deployed to platforms like Heroku, PythonAnywhere, or any other service that supports Python applications.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - [aimen.aberra@gmail.com](mailto:aimen.aberra@gmail.com)
Project Link: [https://github.com/aimabe/personal_site](https://github.com/aimabe/personal_site)
