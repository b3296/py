# -*- coding : utf-8 -*-
import os
path =os.path.abspath('.')
def dirCheckWord(path,word):
	fileList = []
	root = os.path.abspath(path)
	for i in os.listdir(path):
		dirOrfile = os.path.join(root,i)
		if os.path.isdir(dirOrfile):
			fileListchild = dirCheckWord(dirOrfile,word)
			if fileListchild != [] :
				fileList.extend(fileListchild)
		else :	
			if word in i:
				fileList.append(dirOrfile)	
	return fileList		
for i in dirCheckWord(path,'666'):
	print(i)
print('over')		