#!/usr/bin/python3

print("Content-Type: text/html")
print()

import os
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

cmd = form.getvalue("c")

os.system("python /home/voidwalker/gprr/r.py")


