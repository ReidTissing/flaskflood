activate_this = '/var/www/FlaskApp/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
import sys
import logging
import os
#import forms

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp")
#sys.path.insert(1, '/var/www/FlaskApp/FlaskApp')
sys.path.append("/var/www/FlaskApp/FlaskApp/dias")
#sys.path.append('/var/www/FlaskApp/FlaskApp/dias/dias/dias/core')
#sys.path.append('/var/www/FlaskApp/FlaskApp/dias/dias/dias/storage')
#sys.path.append('/var/www/FlaskApp/FlaskApp/dias/dias/dias/notebooks')
#sys.path.append('/var/www/FlaskApp/FlaskApp/dias/dias/dias/scripts')
#sys.path.append(os.path.expanduser("~/.local/lib/python3.5/site-packages"))
#from dias import run_test
#from dias import *
#from dias import *
from FlaskApp import app as application
application.secret_key = 'peaches'
