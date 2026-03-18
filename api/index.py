import sys
import os
import shutil

# Add the Django project to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'mywebsite'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

# Vercel workaround: Copy SQLite DB to /tmp/ since the root is read-only
# This is necessary because Django/SQLite needs write access to open the DB
db_src = os.path.join(os.path.dirname(__file__), '..', 'mywebsite', 'db.sqlite3')
db_dest = '/tmp/db.sqlite3'

if os.path.exists(db_src) and not os.path.exists(db_dest):
    shutil.copy2(db_src, db_dest)

os.environ['SQLITE_DB_PATH'] = db_dest

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
