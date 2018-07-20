# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# fs = count()    
# print(list(fs))
# def is_odd(n):
#     return n % 2 == 1
# L = list(filter(lambda n : n % 2 == 1, range(1, 20)))
# print(L)
import time,functools
# def metric(fn):
# 	@functools.wraps(fn)
# 	def wrapper(*args,**kw):
# 		starttime = time.time()
# 		func=fn(*args,**kw)
# 		endtime = time.time()
# 		print('%s executed in %s ms' % (fn.__name__, endtime-starttime))
# 		return func
# 	return wrapper	
# @metric
# def fast(x, y):
#     time.sleep(1.0012)
#     return x + y;

# @metric
# def slow(x, y, z):
#     time.sleep(2.1234)
#     return x * y * z;

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')    
# print(time.gmtime())
# print(time.clock())
# print(time.daylight)
# print(time.gmtime())
# print(time.time())
# def log(text):
#     if isinstance(text, str):
#         def decorator(func):
#             @functools.wraps(func)
#             def wrapper(*args, **kw):
#                 print('begin call', text)
#                 fn = func(*args, **kw)
#                 print('end call', text)
#                 return fn
#             return wrapper
#         return decorator
#     else:
#         @functools.wraps(text)
#         def wrapper(*args, **kw):
#             print('begin call')
#             fn = text(*args, **kw)
#             print('end call', text.__name__)
#             return fn
#         return wrapper

# @log
# def funcc():
#     print('%s()' % funcc.__name__)
#     time.sleep(1.1234)
# @log('ggggg')
# def funccc():
#     print('函数')
# funcc()

# def text():
# 	return 123
# print('begin call')
# fn = text()
# print('end call', text.__name__)
# print(fn)

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#     def get_gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         if gender not in ['male','female']:
#             raise ValueError('bad gender')
#         else :
#             self.__gender=gender    
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
# bart.__gender = 'fle'        
# print(bart.__gender)        
# print(bart.get_gender()) 
       
# class Student(object):
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         self.__autoCount()
#     def __autoCount(self):
#         Student.count = Student.count +1    
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('lisa')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')        

# from types import MethodType
# class Teacher(object):
#     __slots__ = ('name','age','printStr')

# #函数的定义
# def printStr(self):
#     print("好好学习")
# t = Teacher()
# t.printStr = MethodType(printStr, t)
# t.printStr()
#t.ttt = 132

# class Screen(object):
#     """docstring for Screen"""
#     @property
#     def width(self):
#         return self._width
#     @width.setter
#     def width(self,num):
#         if not isinstance(num,int):
#             raise ValueError('the parameter must is int')
#         self._width = num    
#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self,num):
#         if not isinstance(num,int):
#             raise ValueError('the parameter must is int')                
#         self._height = num   
#     @property
#     def resolution(self):
#         return self.width*self.height         
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')        
# from enum import Enum, unique
# class Gender(Enum):
#     Male = 0
#     Female = 1

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')        
from functools import reduce
def str2num(s):
    return float(s)
def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)
def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)
try:
    main()
except Exception as e:
    print(e)
else:
    print('NoError')
finally:
    print('over')
print('end')