from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
import os
from .models import Project, Skill, ContactMessage

DEFAULT_SKILLS = {
    'ai': [
        {'name': 'PyTorch', 'level': 88},
        {'name': 'TensorFlow', 'level': 82},
        {'name': 'Scikit-learn', 'level': 85},
        {'name': 'Computer Vision', 'level': 85},
        {'name': 'NLP / Transformers', 'level': 83},
        {'name': 'RAG Systems', 'level': 80},
    ],
    'backend': [
        {'name': 'Python', 'level': 92},
        {'name': 'Django / DRF', 'level': 88},
        {'name': 'PostgreSQL', 'level': 80},
        {'name': 'REST APIs', 'level': 85},
    ],
    'frontend': [
        {'name': 'HTML5 / CSS3', 'level': 82},
        {'name': 'JavaScript', 'level': 75},
        {'name': 'Bootstrap', 'level': 80},
        {'name': 'Leaflet.js', 'level': 70},
    ],
    'tools': [
        {'name': 'Git / GitHub', 'level': 88},
        {'name': 'Docker', 'level': 72},
        {'name': 'UiPath', 'level': 75},
        {'name': 'Gemini API', 'level': 82},
    ],
}


def home(request):
    projects = Project.objects.filter(featured=True)[:6]
    skills = Skill.objects.all()

    skill_groups = {}
    for skill in skills:
        cat = skill.get_category_display()
        if cat not in skill_groups:
            skill_groups[cat] = []
        skill_groups[cat].append(skill)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message_text = request.POST.get('message', '').strip()
        if name and email and message_text:
            ContactMessage.objects.create(name=name, email=email, message=message_text)
            send_mail(
                subject=f'Portfolio Message from {name}',
                message=f'Name: {name}\nEmail: {email}\n\n{message_text}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['asmaalgarably@gmail.com'],
                fail_silently=True,
            )
            messages.success(request, 'Message sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please fill all fields.')

    context = {
        'projects': projects,
        'skill_groups': skill_groups,
        'default_ai_skills': DEFAULT_SKILLS['ai'],
        'default_backend_skills': DEFAULT_SKILLS['backend'],
        'default_frontend_skills': DEFAULT_SKILLS['frontend'],
        'default_tools_skills': DEFAULT_SKILLS['tools'],
    }
    return render(request, 'core/index.html', context)


def download_cv(request):
    cv_path = os.path.join(settings.MEDIA_ROOT, 'cv', 'AsmaAlgarably-CV.pdf')
    if os.path.exists(cv_path):
        return FileResponse(open(cv_path, 'rb'), as_attachment=True, filename='Asma_AlGarably-CV.pdf')
    raise Http404("CV not found")