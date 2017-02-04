#!--coding:utf-8--
from pickle import *

"""
# 经常遇到在Python程序运行中得到了一些字符串、列表、字典等数据，想要长久的保存下来，
# 方便以后使用，而不是简单的放入内存中关机断电就丢失数据。
# 它是一个将任意复杂的对象转成对象的文本或二进制表示的过程。同样，必须能够将对象经过序列化后的形式恢复到原有的对象。
# marshal和pickle的区别在于Marshal只能处理简单的Python对象
"""

from copyreg import *

import copyreg, copy, pickle
class C(object):
     def __init__(self, a):
         self.a = a

def pickle_c(c):
     print("pickling a C instance...")
     return C, (c.a,)

copyreg.pickle(C, pickle_c)
c = C(1)
d = copy.copy(c)
p = pickle.dumps(c)