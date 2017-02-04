from itertools import count, cycle, repeat, chain, compress, \
    dropwhile, islice, starmap, takewhile, tee, groupby, \
    product, permutations, combinations, combinations_with_replacement

print count(10, 1)
print cycle('asdf')
print list(repeat(10, 3))
print '='*60

# print accumulate([1,2,3,4,5]) //python3.5

mm = chain([1,2,3,4], (3,4,5,6))
mm = chain({1:2,3:4}, {3:4,5:6})
print list(mm)
print '='*60

mm = chain.from_iterable(['asd', 'bcd'])
print list(mm)
print '='*60

mm = compress('asdcd', [1,0,1,0.1])
print list(mm)
print '='*60


mm = dropwhile(lambda x: x<5, [1,4,6,1])
print list(mm)
print '='*60

# print filterflase(lambda x: x%2, range(10)) //python3.5

mm = islice([1,2,34,4,5,5], 2, 4, 1)
nn = [1,2,34,4,5,5]
print list(mm), nn[2:4:1]
print '='*60

mm = starmap(pow, [[2,3],[3,3]])
nn = map(pow, [2,3], [3,3])
print list(mm), nn
print '='*60

mm = takewhile(lambda x: x<5, [1,4,8,4,1])
print list(mm)
print '='*60

mm = tee([1,2,3,4,5], 3)
for i in mm:
    print list(i)
print '='*60

# mm = zip_longest([1,2,3], [4,5,6])
# print list(mm)

def test(m):
    if m < 10:
        return "low"
    elif m < 20:
        return "middle"
    else:
        return "high"

mm = groupby(sorted([1,11,35,14,50,100]), key = test)
for m, n in mm:
    print m
    print list(n)
print '='*60

mm = product('asdf', 'hjkl', repeat = 1)
print len(list(mm))
print '='*60

mm = permutations('asdf', 3)
# print list(mm)
print len(list(mm))
print '='*60

mm = combinations('asdf', 2)
# print list(mm)
print len(list(mm))
print '='*60

mm = combinations_with_replacement('asdf', 2)
print list(mm)
print len(list(mm))
print '='*60
















