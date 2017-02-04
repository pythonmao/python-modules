import reprlib

a = [1,2,3,[1,2,3],6,7]
reprlib.aRepr.maxlevel = 2
reprlib.aRepr.maxlist = 3
print(reprlib.repr(a))
