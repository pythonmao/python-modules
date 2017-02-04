class ring(object):

    def __init__(self, l):
        if not l:
            print "ring must at lest has a element."
        self._data = l

    def __repr__(self):
        print repr(self._data)

    def __str__(self):
        return str(self._data)

    # def __len__(self):
    #     return len(self._data)

    def __getitem__(self, i):
        return self._data[i]

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[1]

    def turn(self):
        return self._data.insert(0, self._data.pop(-1))


test = [1,2,3,4]
mm = ring(test)
mm

mm.turn()
mm