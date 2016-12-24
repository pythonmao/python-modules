import abc
import six


@six.add_metaclass(abc.ABCMeta)
class FormatterBase(object):
    """Base class for example plugin used in the tutorial.
    """

    def __init__(self, max_width=60):
        self.max_width = max_width

    @abc.abstractmethod
    def format(self, data):
        pass