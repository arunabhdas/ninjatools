#!/usr/bin/python3
from string import Template
s = Template('$who likes $what')
s.substitute(who='Ceaser', what='Sandwich')
print(s)