import math

class Vector2:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
            
    def add(self, vec): # only use this and sub() for vector or tuple addition
        self.x += vec.x
        self.y += vec.y
    
    def sub(self, vec):
        self.x -= vec.x
        self.y -= vec.y
    
    def scale(self, magnitude):
        self.x *= magnitude
        self.y *= magnitude
    
    def rotate(self, delta):
        theta = self.angle()
        theta += delta
        self.x = math.cos(theta)
        self.y = math.sin(theta)

    # non-void methods
    def magnitude(self):
        return math.hypot(*(self.tuplify()))

    def angle(self):
        theta = math.atan2(self.y, self.x)
        return round(theta, 9) # rounded to prevent tiny inaccuracies

    def tuplify(self): # returns vector as tuple
        return (self.x, self.y)

Vector2.ZERO = Vector2(0,0)
Vector2.ONE = Vector2(1,1)
Vector2.X_AXIS = Vector2(1,0)
Vector2.Y_AXIS = Vector2(0,1)

