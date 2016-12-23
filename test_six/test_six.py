import sys
import six
import abc

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
PY34 = sys.version_info[0:2] >= (3, 4)

if sys.platform.startswith('linux'):
    print 'linux'

if six.PY2:
    print 'The version of the python is 2'

@six.add_metaclass(abc.ABCMeta)
class test(object):
    def __init__(self):
        print 'test metaclass'

sub_test = test()
print type(test)
print type(sub_test)
# print issubclass(sub_test, test)