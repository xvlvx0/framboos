#!/usr/bin/python
import sys

try:
	import wx
except:
	print("wxPython is not installed. This program requires wxPython to run.")
	if sys.version_info.major >= 3:
		print("""As you are currently running python3, this is most likely because wxPython is not yet available for python3. You should try running with python2 instead.""")
		sys.exit(-1)
	else:
		raise

