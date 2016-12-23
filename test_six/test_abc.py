import six
import abc

@six.add_metaclass(abc.ABCMeta)
class test(object):
    @abc.abstractmethod
    def func(self):
        pass

class sub_test(test):
    def __init__(self):
        print 'aaaa'
    def func(self):
        print 'success'

mm = sub_test()