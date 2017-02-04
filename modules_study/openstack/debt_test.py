from debtcollector import moves
import warnings
warnings.simplefilter('always')
class Dog(object):
   @property
   @moves.moved_property('bark')
   def burk(self):
     return self.bark
   @property
   def bark(self):
     return 'woof'

d = Dog()
print(d.bark)
print(d.burk)
