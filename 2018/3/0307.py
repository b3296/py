# -*- coding : utf-8 -*-
import base64,hashlib,random,hmac,itertools
# def safe_base64_decode(s):
#     l = len(s)
#     num = l % 4
#     if num != 0:
#     	for i in range(num):
#     		s += b'='
#     return base64.b64decode(s) 
# # 测试:
# assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
# assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
# print('ok')    
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
# def login(user, password):
#     global db
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     md5password = md5.hexdigest()
#     #print(md5password)
#     if user in db.keys() and db[user] == md5password:
#     	return True
#     else :
#     	return False	 
# #测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')    
# salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
# print(salt)
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)    
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    user = db[username]
    return user.password == get_md5(password+user.salt)
# def hmac_md5(key, s):
#     return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

# class User(object):
#     def __init__(self, username, password):
#         self.username = username
#         self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
#         self.password = hmac_md5(self.key, password)

# db = {
#     'michael': User('michael', '123456'),
#     'bob': User('bob', 'abc999'),
#     'alice': User('alice', 'alice2008')
# }
# def login(username, password):
#     user = db[username]
#     return user.password == hmac_md5(user.key, password)
# # 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')    
def pi(N=10):
	' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
	natuals = itertools.count(1,2)
	oddIterator = itertools.takewhile(lambda x: x <= 2*N-1, natuals)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:
	# Divisor = 4
	# ret = 0
	# for i in oddIterator:
	# 	ret += Divisor /i
	# 	Divisor = -Divisor
	DivisorIterator= itertools.cycle([4,-4])
	piIterator = map(lambda x: next(DivisorIterator)/ x, oddIterator)	
	return sum(piIterator)
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')    
