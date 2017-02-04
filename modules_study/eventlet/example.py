import eventlet
from eventlet.green import urllib2
import time
import pdb

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
]

def fetch(url):
    print "open ", url
    result = urllib2.urlopen(url).read()
    print "end ", url
    return result

pool = eventlet.GreenPool(1)

pdb.set_trace()
start = time.time()
for body in pool.imap(fetch, urls):
    print "get body", len(body)
print "cost:", time.time() - start
