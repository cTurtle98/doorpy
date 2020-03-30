#!/usr/bin/python3
"""
doorpy - raspberry pi message board for your door
Copyright (C) 2020  Ciaran Farley (ciaran@cturtle98.com)

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

--------

doorpy.wsgi
wsgi config file for apache2

"""

import sys
import logging

# log output to standard error
logging.basicConfig(stream=sys.stderr)

# set enviroment path
sys.path.insert(0,"/user/pi/doorpy/")

# import flask app
from doorpy import app as application
