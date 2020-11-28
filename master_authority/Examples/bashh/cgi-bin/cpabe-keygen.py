#!/usr/bin/env python
import sys
import json
import cgi

def main():
    fs = cgi.FieldStorage()

    sys.stdout.write("Content-Type: application/json")

    sys.stdout.write("\n")
    sys.stdout.write("\n")

    result = {}
    result['success'] = True
    result['message'] = "The command Completed Successfully"
    result['keys'] = ",".join(fs.keys())
    print(fs)
    print(fs['0'].value)
    d = {}
    for k in fs.keys():
        d[k] = fs.getvalue(k)

    result['data'] = d

    sys.stdout.write(json.dumps(result,indent=1))
    sys.stdout.write("\n")
    sys.stdout.close()  

main()