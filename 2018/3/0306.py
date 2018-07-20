# -*- coding : utf-8 -*-
import os,time,random,threading,re
from multiprocessing import Process
from multiprocessing import Pool,Queue
from datetime import datetime,timedelta,timezone
# def runproc(name):
# 	print('Run child process %s (%s)...'%(name,os.getpid()))
# if __name__ == '__main__':
# 		print('parent process %s'%(os.getpid()))	
# 		p = Process(target=runproc,args=('test',))
# 		print('child process start')
# 		p.start()
# 		#p.join()
# 		print('child process end')
# 		print('last process %s'%(os.getpid()))
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')		
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        #time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
	print('Process to read: %s' % os.getpid())
	flag = 0
	while flag<3:
		if not q.empty():
			flag +=1
			value = q.get(True)
			print('Get {0} from queue.'.format(value))
			#time.sleep(random.random())

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    pr.join()
    #pr进程里是死循环，无法等待其结束，只能强行终止:
    time.sleep(2)
    pr.terminate()    
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)    
# print("=============")
# m = re.match("(\d*)", '010-12345345')
# print(m)
# print( m.group(0) )
# print( m.groups() )
# now =datetime.now()
# dt = datetime(2015, 4, 19,12,20,1)
# t = now.timestamp()
# ti = datetime.fromtimestamp(t)
# print(ti)
# print(datetime.utcfromtimestamp(t))
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# #print(cday)
# timestr = now.strftime('%c')
# #print(timestr)
# e = now + timedelta(hours=2,days=26)
# print(e)
# def to_timestamp(dt_str, tz_str):
#     dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
#     utc = re.match(r'^UTC([\+\-]\d{0,2})(:00)$',tz_str).groups()[0]
#     utc = int(utc)
#     tz_utc = timezone(timedelta(hours=utc))
#     dt = dt.replace(tzinfo=tz_utc)
#     ret = dt.timestamp()
#     print(datetime.fromtimestamp(ret).replace(tzinfo=tz_utc))
#     return ret
# # 测试:
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1

# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# assert t2 == 1433121030.0, t2

# print('ok')    