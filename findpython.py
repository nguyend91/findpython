#!/usr/bin/env python2
"""This looks for python files and lint them"""
import os
import sys
import magic
from pylint.lint import Run

mime = magic.Magic(mime=True)
path = sys.argv[1]
output = []
for subdir, dirs, files in os.walk(path):
    current = []
    output.append(current)
    for f in files:
        filepath = subdir + os.sep + f
        mimefile = magic.from_file(filepath)
        if mimefile == "Python script, ASCII text executable":
            current.append(filepath)

for o in output:
    Run(['--rcfile=~/.pylintrc'] + o,)
