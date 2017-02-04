#*--coding:utf-8--*
import codecs
import sys

print sys.maxunicode

mm = codecs.encode('hello world', 'gb2312')
print codecs.decode(mm, 'gb2312')

print "风卷残云"
a = u"风卷残云"

print codecs.encode(a, 'utf-8')
print a.encode("utf-8")

look = codecs.lookup('gd2312')
print look.decode(b)


bfile = codecs.open("ddd.txt", 'r', 'bib5')
ss = bfile.read()
bfile.close()