#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cgi, cgitb
import os
from subprocess import Popen, PIPE
	
def main():

    cgitb.enable()

    print "Content-Type: text/html"
    print "\n\r"

    form = cgi.FieldStorage()

    selected_modules = form.getlist("selected_modules")
    device = form.getfirst("device")

    os.chdir("../riotam-backend/")
    proc = Popen(["python", "build.py", arguments], stdout=PIPE)
    output = proc.communicate()[0]
    print output
	
if __name__ == "__main__":
    
    main()