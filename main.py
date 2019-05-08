#!/usr/bin/env python
import subprocess

uname, diskspace = "uname", "df"
uname_arg, diskspace_arg = "-a", "-h"
print("Gathering system information with %s command:" % uname)
subprocess.call([uname, uname_arg])
print("Gathering system information with %s diskspace:" % diskspace)
subprocess.call([diskspace, diskspace_arg])

