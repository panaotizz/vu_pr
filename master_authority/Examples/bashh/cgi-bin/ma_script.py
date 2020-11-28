#!/usr/bin/env python
import subprocess

import cgi, cgitb # Not used, but will be needed later.
import sys
import os 
sys.path.insert(0, "/usr/local/lib/python")
cgitb.enable()
print("Content-type: text/html\n\n")
print('')

print("<H3>Generating Keys</H3>")


output = subprocess.check_output("~/Desktop/project/master_authority/graphene/Examples/bashh/script.sh", shell=True) #call C untrusted script that will call cpabe-setup inside enclave and create 2 keys. pub_key comes out of enclave
print (output)
print("Key generation complete! <br>")
