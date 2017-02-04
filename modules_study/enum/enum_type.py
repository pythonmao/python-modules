from enum import Enum

class color(Enum):
    red = 1
    green = 2
    blue = 2

color.red
color.green


mm = color(1)
mm = color(2)

color['red']
mm = color['green']
mm.name
nn.value

@unique
class color(Enum):
    red = 1
    green = 2
    blue = 2

list(color)


for name, member in Shape.__members__.items():
     name, member

('square', <Shape.square: 2>)
('diamond', <Shape.diamond: 1>)
('circle', <Shape.circle: 3>)
('alias_for_square', <Shape.square: 2>)

Color.red is Color.red
Color.red is not Color.red
Color.red == Color.red

Note :Subclassing an enumeration is allowed only if the enumeration does not define any members

Animal = Enum('Animal', 'ant bee cat dog')


class Shape(IntEnum):
     circle = 1
     square = 2

