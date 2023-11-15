class RectangleRootChangeError(Exception):

    def __str__(self):
        return "Haven't root premission"



class Rectangle:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    @property
    def height(self):
        return self.height()

    @height.setter
    def height(self, value):
        if not isinstance(value, str):
            raise TypeError()
        if not len(value):
            raise ValueError()
        raise RectangleRootChangeError()


x = Rectangle(31, 54)
print(x.height)