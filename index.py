#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

print "Content-Type: text/html"
print "\n\r"

print "<!DOCTYPE html>"
print "<html>"
print "<head>"
print "<title>RIOT OS App Market</title>"
print "<link rel=""stylesheet"" href=""styles.css"">"
print "<!-- Origin Trial Token, feature = WebUSB (For Chrome M57+), origin = https://www.vanappsteer.de, expires = 2017-08-23 -->"
print "<meta http-equiv=""origin-trial"" data-feature=""WebUSB (For Chrome M57+)"" data-expires=""2017-08-23"" content=""AuMsLNMamUdtrJmHYTJ+0qNNi3rEKeAfbeQcVT8ZvAcdz9QJHhHk9l4kHIAPaHsMEkOGLGBYsfDOCL8BBkocHgEAAABTeyJvcmlnaW4iOiJodHRwczovL3d3dy52YW5hcHBzdGVlci5kZTo0NDMiLCJmZWF0dXJlIjoiV2ViVVNCMiIsImV4cGlyeSI6MTUwMzUxNzQxMX0="">"
print "</head>"
print
print "<body>"

print "<button type=""button"" id=""selectButton"" onclick=""selectDevice()"">Select Device</button>"

print "<p><div id=""deviceInfo"" style=""white-space: pre""></div></p>"

print "<div id=""downloadSection"" style=""visibility: hidden;"">"
print "<form><p>Select an application:</p><fieldset><input type=""radio"" id=""r1"" name=""component"" value=""bindist"" checked=""checked""><label for=""r1""> bindist</label><br> <input type=""radio"" id=""r2"" name=""component"" value=""gnrc_minimal""><label for=""r2""> gnrc_minimal</label><br> <input type=""radio"" id=""r3"" name=""component"" value=""timer_periodic_wakeup""><label for=""r3""> timer_periodic_wakeup</label></fieldset></form>"

print "<br><button type=""button"" id=""downloadButton"" onclick=""download()"">Download your personal RIOT OS</button></div><script src=""main.js""></script>"

print "</body>"
print "</html>"