#!/usr/bin/python

import sys

if len(sys.argv) > 1:
	for i in sys.argv[1:]: print(i.strip("b/"))
else:
	print("No documents were added with this commit")