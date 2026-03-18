import sys
import os

# Add the Django project to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'mywebsite'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
