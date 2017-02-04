from multiprocessing.dummy import Pool as threadPool
import time
import urllib2

import eventlet
from eventlet.green import urllib2

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
]

start = time.time()
results = map(urllib2.urlopen, urls)
print 'normal:', time.time()-start


start2 = time.time()
pool = threadPool(8)
results = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()
print 'Thread2 cost:', time.time() - start2

start3 = time.time()
pool = eventlet.GreenPool()
for body in pool.imap(urllib2.urlopen, urls):
    pass
print 'thread3 cost:', time.time() - start3