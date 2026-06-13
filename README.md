# Asma Al-Garably — Portfolio Website

Personal portfolio built with Django, showcasing AI/ML projects and skills.

## Tech Stack
- **Backend:** Django 5.x, SQLite (dev) / PostgreSQL (prod)
- **Frontend:** Vanilla HTML/CSS/JS — no frameworks needed
- **Design:** Dark theme, Space Grotesk typography, animated neural network canvas

## Project Structure
```
portfolio/
├── core/
│   ├── models.py         # Project, Skill, ContactMessage
│   ├── views.py          # home view + CV download
│   ├── urls.py
│   ├── admin.py
│   └── templates/core/
│       └── index.html    # Full single-page portfolio
├── portfolio/
│   ├── settings.py
│   └── urls.py
├── media/
│   └── cv/               # Place your CV here: asma_algarably_cv.pdf
└── manage.py
```

## Setup & Run

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install django Pillow

# 3. Run migrations
python manage.py migrate

# 4. Create admin user
python manage.py createsuperuser

# 5. Add your CV
# Place your PDF at: media/cv/asma_algarably_cv.pdf

# 6. Run server
python manage.py runserver
```

Then open: http://127.0.0.1:8000

## Admin Panel
Go to http://127.0.0.1:8000/admin to add/edit:
- **Projects** — title, description, tech stack, GitHub URL, featured toggle
- **Skills** — name, category (AI/ML, Backend, Frontend, Tools), skill level %
- **Contact messages** — view messages sent via the contact form

## CV Download
Place your CV PDF at `media/cv/asma_algarably_cv.pdf`
The download button will serve it automatically.

## Deployment (GitHub Pages / Railway / Render)
For production, set in `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')
```

## Links to Update in index.html
- Email: `asmaalgarably@gmail.com`
- LinkedIn: `linkedin.com/in/asma-algarably`
- GitHub: `github.com/asmaalgarably`
