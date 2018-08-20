from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print('Refillin candy...')
    try:
        candytray.release()
    except ValueError:
        print('full, skipping')
    else:
        print('ok')
    lock.release()

def buy():
    lock.acquire()
    print('Buying candy...')
    if candytray.acquire(False):
        print('ok')
    else:
        print('empty ,skipping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print('starting at:',ctime())
    nloops = randrange(2,6)
    print('The Candy Machine (full with %d bars)!'%MAX)
    Thread(target=consumer,args=(randrange(
        nloops,nloops+MAX+2),)).start()   #买家
    Thread(target=producer, args=(
        nloops,)).start() #卖家


'''
这个函数（这里使用   了装饰器的方式）会在Python 解释器中注册一个退出函数，也就是说，它会在脚本退出
之前请求调用这个特殊函数。（ 如果不使用装饰器的方式， 也可以直接使用
register(_atexit())）。
'''
@register
def _atexit():   
    print('all done at',ctime())

if __name__ == '__main__':
    _main()
