import os
docs = [i for i in os.listdir(".") if i.__contains__(".doc")] # returns list of docs in dir
for i in docs: print(i + '\n')
