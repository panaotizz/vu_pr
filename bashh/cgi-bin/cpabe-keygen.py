#!/usr/bin/env python
import sys
import json
import cgi

def main():
    fs = cgi.FieldStorage()
    print 'Content-type: text/html\n'
    return json.dumps(fs.keys())


main()