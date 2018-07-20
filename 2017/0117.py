# number = 18
# running = True
# i = 0
# while running:
# 	guess = int(input("enter an integer :"))
# 	if guess>number:
# 		print('大了')
# 	elif guess<number:
# 		print('小了')
# 	else:
# 		print('对了')
# 		running = False
# 	i += 1	
# 	print('第{0}次'.format(i))
# else:
# 	print('一共猜了{0}次'.format(i))
# s = '1'		
# for i in range(5,15):
# 	print(i)
# else:
# 	for i in range(0,len(s)):
# 		print(s[i],end='')
# 		if i == 8:
# 			break;
# 	else :
# 		print('\ns变量结束')
# a =	list(range(1,5))	
# print(len(s))		
def oneFunc(a,b,c=5):
	'''这么神奇吗？

	确实挺生气的'''
	if a == b:
		print('一样')
	else:
		print(a,'!=',b)	
	"""就是这么神奇"""	
oneFunc(True,b='Ture')
print(oneFunc.__doc__)
print(help(oneFunc))

	
					

