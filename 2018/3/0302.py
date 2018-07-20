# -*- coding: utf-8 -*-
# import unittest
# class Student(object):
# 	def __init__(self, name, score):
# 		self.name = name
		        
# 		self.score = score
# 	def get_grade(self):
# 		if self.score < 0 or self.score > 100:
# 			raise ValueError('score must between 0 and 100')		
# 		if self.score >= 60 and self.score<80:
# 		    return 'B'
# 		if self.score >= 80:
# 		    return 'A'
# 		return 'C'
# class TestStudent(unittest.TestCase):
# 	def setUp(self):
# 		print('test is start')
# 	def tearDown(self):
# 		print('this is over')	
# 	def test_80_to_100(self):
# 	    s1 = Student('Bart', 80)
# 	    s2 = Student('Lisa', 100)
# 	    self.assertEqual(s1.get_grade(), 'A')
# 	    self.assertEqual(s2.get_grade(), 'A')

# 	def test_60_to_80(self):
# 	    s1 = Student('Bart', 60)
# 	    s2 = Student('Lisa', 79)
# 	    self.assertEqual(s1.get_grade(), 'B')
# 	    self.assertEqual(s2.get_grade(), 'B')

# 	def test_0_to_60(self):
# 	    s1 = Student('Bart', 0)
# 	    s2 = Student('Lisa', 59)
# 	    self.assertEqual(s1.get_grade(), 'C')
# 	    self.assertEqual(s2.get_grade(), 'C')

# 	def test_invalid(self):
# 	    s1 = Student('Bart', -1)
# 	    s2 = Student('Lisa', 101)
# 	    with self.assertRaises(ValueError):
# 	        s1.get_grade()
# 	    with self.assertRaises(ValueError):
# 	        s2.get_grade()

# if __name__ == '__main__':
#     unittest.main()        


def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
      ...
    ValueError 
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)
if __name__ == '__main__':
    import doctest
    doctest.testmod()    