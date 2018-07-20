def reverse(text):
	return text[::-1]
def check(text):
	if text == True:
		print('yes')
		return True	
	if text == reverse(text):
		print('yes')
		return True
	else:
		print('no')
		return False
fh=(',','.','?','/','\\','`','~','+','-','*','!','^',' ')
flag=True
while flag :
	text=input("Enter: ")
	def delFh(text):
		if len(text) != 1:
			for i in range(0,len(text)) :
				if text[i] in fh:
					text = text[:i]+text[(i+1):] 
					return delFh(text)
			else:
				return text		
		else:
			return True					 	
	if check(delFh(text.lower())):
		flag = False
print('over')		
