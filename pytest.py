#!/usr/bin/python

import sys
from docx import Document

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        print("File name: " + str(i))
        document = Document(i)
        fullText = []
        [fullText.append(p.text) for p in document.paragraphs]
        print('\nContents:\n' + '\n'.join(fullText) + "\n----EOF----\n")
else:
	print("No documents were added with this commit")
