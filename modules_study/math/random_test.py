import random

print random.random()

print random.uniform(1,10)

print random.randrange(100)

print random.randrange(1,100,98)

print random.choice('asdfgds')

items = [1,2,3,4,5]
random.shuffle(items)
print items

print random.sample([1,2,3,4,4,5,6],4)