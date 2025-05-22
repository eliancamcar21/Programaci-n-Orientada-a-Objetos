from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
print(type(Season.SPRING))
print(repr(Season.SPRING))
print(list(Season))