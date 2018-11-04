#!/usr/bin/python3
import os
import re
_replace_re = re.compile("com.mydomain.mypackage")
for dirpath, dirnames, filenames in os.walk("../../myprojectfolder/"):
    for file in filenames:
        file = os.path.join(dirpath, file)
        tempfile = file + ".temp"
        with open(tempfile, "w") as target:
            with open(file) as source:
                for line in source:
                    line = _replace_re.sub("com.mydomain.mynewpackage", line)
                    target.write(line)
        os.rename(tempfile, file)
