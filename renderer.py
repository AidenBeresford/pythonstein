import math
import pygame
import numpy as np
from engine.vector2 import Vector2
from player import Player

RAYLENGTH = 1280
RAYCOUNT = 20

class Renderer:
    def __init__(self, screen, world, player):
        self.screen = screen
        self.map = world
        self.pos = player.position
        self.dir = player.direction
    
    def render(self):
        self.raycast()

    def raycast(self):
        for t in np.linspace(self.dir.angle() - math.radians(60), self.dir.angle() + math.radians(60), RAYCOUNT):
            if round(t, 5) != round(self.dir.angle(), 5):
                target = Vector2(RAYLENGTH * math.cos(t) + self.pos.x, -RAYLENGTH*math.sin(t) + self.pos.y)
                pygame.draw.line(self.screen, 'red', self.pos.tuplify(), target.tuplify())


