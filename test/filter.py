# -*- coding : utf-8 -*-
def _odd_iter():
	n = 1
	while True :
		n = n+2
		yield n
def _not_divisible(n):
	return lambda x : x % n > 0
def primes(end = 100):
	yield 2
	it = _odd_iter()
	flag = True	
	while flag:
		n = next(it)
		if n > end:
			flag =False
		yield n
		it = filter(_not_divisible(n), it)
def divisible(num):
	 return lambda x : num % x == 0
def Rational(num):
	def ans(x):
		y = int(num /x) 
		return (x,y)
	return ans
def checkNum(num):	
	if num in primes(num):
		print('yes')
	else:
		print('no')
		answerFilter = filter(divisible(num), range(2,num))
		answer = map(Rational(num),answerFilter)
		answerList = list(answer)
		l = int((len(answerList)+1)/2)
		answerList = answerList[:l]
		for x,y in answerList:
			print(x,'*',y,'=',num)
num = 6977
checkNum(num)			