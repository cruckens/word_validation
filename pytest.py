#!/usr/bin/python

import sys

if len(sys.argv) == 2:
	docs = sys.argv[1].split('\n')
	for i in docs: print(i.strip("+++ b/"))
else:
	print("No documents were added with this commit")