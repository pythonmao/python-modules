import shelve

d = shelve.open('./test.dat', writeback=True)
d['x'] = ['a', 'b', 'c']
print d
d.sync()
d['x'].append('d')
print d
d.close()

d = shelve.open('./test.dat')
for i in d.items():
    print i
d.close()

"""
dbm
# 在一些python小型应用程序中，不需要关系型数据库时，
# 可以方便的用持久字典来存储名称/值对，它与python的字典非常类似，
# 主要区别在于数据是在磁盘读取和写入的。另一个区别在于dbm的键和值必须是字符串类型。

    python中的shelve模块，可以提供一些简单的数据操作
    他和python中的dbm很相似。

    区别如下：
    都是以键值对的形式保存数据，不过在shelve模块中，
    key必须为字符串，而值可以是python所支持的数据
    类型。在dbm模块中，键值对都必须为字符串类型。
"""