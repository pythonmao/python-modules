from multiprocessing import Process, Pipe, Queue, Lock, Value, Array, Pool, Manager,TimeoutError
import os, time

def fpool(x):
    return  x+100

def worker(num):
    print "I am worker!, %d" % num

def flock(lock, num):
    lock.acquire()
    print "I am worker!, %d" % num
    lock.release()

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):
        print 'parent process:', os.getppid()
    print'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name


def fpip(conn):
    conn.send([42, None, 'hello'])
    conn.close()

def fqueue(q):
    q.put([42, None, 'hello'])

def fshare(value, array):
    value.value = 199
    for i in range(len(array)):
        array[i] = 299

def fmanager(d, i):
    d[100] = 100
    for num in range(len(i)):
        i[num] = 299

if __name__ == "__main__":
    print '/n'
    print '***********************************************'
    p = Pool(5)
    print p.map(fpool, [1, 2, 3, 4, 5,6,7,8,9,0])

    # print same numbers in arbitrary order
    for i in p.imap_unordered(fpool, range(11, 20)):
        print i

    # evaluate "f(20)" asynchronously
    res = p.apply_async(fpool, (20,))# runs in *only* one process
    print res.get(timeout=1)  # prints "400"

    # evaluate "os.getpid()" asynchronously
    res = p.apply_async(os.getpid, ())  # runs in *only* one process
    print res.get(timeout=1)  # prints the PID of that process

    # launching multiple evaluations asynchronously *may* use more processes
    multiple_results = [p.apply_async(os.getpid, ()) for i in range(4)]
    print [res.get(timeout=1) for res in multiple_results]

    # make a single worker sleep for 10 secs
    res = p.apply_async(time.sleep, (10,))
    try:
        print res.get(timeout=1)
    except TimeoutError:
        print "We lacked patience and got a multiprocessing.TimeoutError"

    print '/n'
    print '***********************************************'
    jobs = []
    p1 = Process(target=worker, args=(100,))
    jobs.append(p1)
    p1.start()
    p1.join()

    print '/n'
    print '***********************************************'
    p2 = Process(target=f, args=('bob',))
    jobs.append(p2)
    p2.start()
    p2.join()

    
    print '/n'
    print '***********************************************'
    parent_conn, child_conn=Pipe()
    p3 = Process(target=fpip, args=(child_conn,))
    p3.start()
    print parent_conn.recv()
    p3.join()

    print '/n'
    print '***********************************************'
    q4 = Queue()
    p4 = Process(target=fqueue, args=(q4,))
    p4.start()
    print q4.get()
    p4.join()

    print '/n'
    print '***********************************************'
    lock = Lock()
    for num in range(5):
        Process(target=flock, args=(lock, num)).start()

    print '/n'
    print '***********************************************'
    value = Value('i', 99)
    array = Array('i', range(20))

    p5 = Process(target=fshare, args=(value, array))
    p5.start()
    p5.join()

    print value.value
    print array[:]

    print '/n'
    print '***********************************************'
    d = Manager().dict()
    i = Manager().list(range(10))

    p6 = Process(target=fmanager, args=(d, i))
    p6.start()
    p6.join()

    print d
    print i