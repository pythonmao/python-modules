import eventlet

eventlet.monkey_patch()

from eventlet.green import urllib2
import time

urls = ["http://www.tudou.com",
        "http://www.baid.com"
        ]


def test_1(url):
    try:
        print "open tudou"
        time.sleep(100)
        urllib2.urlopen(url).read()
        print "done open tudou"
    except urllib2.HTTPError:
        return


def test_2(url):
    try:
        print "open baidu"
        urllib2.urlopen(url).read()
        print "done open baidu"
    except urllib2.HTTPError:
        return


pool = eventlet.GreenPool(100)
pool.spawn(test_1, urls[0])
pool.spawn(test_2, urls[1])
pool.waitall()
