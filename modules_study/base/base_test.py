import os

# help(os)

class test(object):
    pass

mm = test()
setattr(mm, 'a', 1)
print dir(mm)
print hasattr(mm, 'a')

print '1+2'
print eval('1+2')


print vars(mm)
print hash('a')

#  memoryview()

print bytes('a')
print bytes(1)
print bytes("mm")

print bytearray('123')