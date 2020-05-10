# Ścieżka do wirtualengo środowiska
activate_this = '/root/.virtualenvs/JSON2XML/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys


# Install venv by `virtualenv --distribute venv`
# Then install depedencies: `source venv/bin/active`
# `pip install -r requirements.txt`

# Ścieżka do katalogu z projektem
sys.path.insert(0, "/root/projects/JSON_XML_API/")


# The application object is used by any WSGI server configured to use this file.
#
# Ensure there is an app.py script in the current folder
from xmlapi import app as application