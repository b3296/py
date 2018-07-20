#encoding = utf-8
import os
import time
text="""
	第一行
	第二行
	第三行
"""
file_name = time.strftime("%Y-%m-%d_%H_%M_%S")
if not os.path.exists('./tmp'):
	os.mkdir('./tmp')
f=open("out_%s.html" % file_name, "w")
f.write(text)
f.close()
f=open('./tmp/tmp.txt','r')
while  True:
	r = f.readline()
	print(r)
	if len(r) == 0:
		break
else:
	print('可不是咋的')
f.close()	
print('over')			
# import pickle
# f=open('list.data','wb')
# lists=('a','b','c')
# pickle.dump(lists,f)
# f.close()
# del lists
# f=open('list.data','rb')
# nowLists=pickle.load(f)
# f.close()
# print(nowLists)