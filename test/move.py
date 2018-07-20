# -*- coding:utf-8 -*-
# def move(n,a,b,c):
# 	if n == 1:
# 	    print(a, '-->', c)
# 	    return
# 	move(n - 1,a,c,b)
# 	print(a, '-->', c)
# 	move(n - 1,b,a,c)

# move(4,'a','b','c')    
# def max_min(nums):
# 	if len(nums)<1:
# 		return (None,None)
# 	min = max = nums[0]
# 	for num in nums:
# 		if min>num :
# 			min = num
# 		if max <num :
# 			max = num
# 	return (min,max)
# nums=[10,2,8,4,25,1,-2,6,9,7]
# print(max_min([7,1,3,5,9,4.12]))				
# def triangles():
# 	L = [1]
# 	while True:
# 	    yield L
# 	    L = [x+y for x,y in zip( [0]+L, L+[0] )]
			
# a=triangles()
# print(next(a))
# print(next(a))
# def normalize(name):
# 	l = name.lower()
# 	return l[0].upper()+l[1:]
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
from functools import reduce
import re
# def prod(L):
# 	return 	reduce(j,L)
# def j(x,y):
# 	return x*y
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')		
# def str2float(s):
# 	l = s.find('.')
# 	return reduce(num2float,map(str2num,s[:l]+s[l+1:]))/10**(len(s)-l-1)
# def str2num(s):
# 	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# 	return digits[s]
# def num2float(x,y):
# 	return x*10+y
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')
# def is_palindrome(n):
# 	n = str(n)
# 	u = n[::-1]
# 	return n == u
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')    
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]    
L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score,reverse=True)
print(L2)
print(L3)