from engine.vector2 import Vector2

class Player:
    def __init__(self, pos):
        self.position = pos
        self.direction = Vector2.Y_AXIS

    def __getattr__(self, attr):
        if attr == 'x':
            return self.position.x
        if attr == 'y':
            return self.position.y
        raise(AttributeError)

    def __setattr__(self, attr, val): # you're not usually supposed to override this but it makes the code cleaner so whatevs
        if attr == 'x':
            self.position.x = val # might change to use dict for optimization later
        if attr == 'y':
            self.position.y = val
        else:
            self.__dict__[attr] = val

