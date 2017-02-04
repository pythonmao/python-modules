class test(object):
    def __init__(self, value, name):
        self._value = value
        self._name = name
    @property
    def test_value(self):
        return self._value

    @test_value.setter
    def test_value(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    test_name = property(get_name, set_name)

obj = test(100, 'hello')
print obj.test_value
obj.test_value = 10
print obj.test_value

obj.set_value(1000)
print obj.test_value

print obj.test_name
obj.test_name = 'world'
print obj.test_name
