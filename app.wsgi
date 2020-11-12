#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/portfolio')
 
from app import app as application