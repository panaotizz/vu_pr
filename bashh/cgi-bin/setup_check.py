#!/usr/bin/env python
import subprocess
import requests
import cgi, cgitb # Not used, but will be needed later.
import sys
import os 
sys.path.insert(0, "/usr/home/joe/lib/python")
sys.path.insert(0, "/usr/local/lib/python")
#cgitb.enable()
print("Content-type: text/html\n\n")
print('')

print '<html>'
print '<head>'
print '<title>Master Authority</title>'
print '</head>'
print '<body>'
if (os.path.exists('master_key') and os.path.exists('pub_key')):
	print '<a> Master Authority is set up</a> <br>'
	print '<a href="../pub_key">Click here to download pub_key</a>'
else:
	print '<h1> Welcome to the Master Authority key generation </h1> <br> Keys are not generated <br> '
	print '<a href="script.sh"> Click here to generate Secret key and Public key </a>'	
print '</body>'
print '</html>'
