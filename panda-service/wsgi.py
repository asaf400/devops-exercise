# -*- coding: utf-8 -*-
#Gunicorn WSGI compatible Service

import os
import sys

path = os.getcwd()
sys.path.append(path)

from bigservice import app as application
