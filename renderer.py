import math
import pygame
import numpy as np
from engine.vector2 import Vector2
from player import Player

RAYLENGTH = 128
RAYCOUNT = 4

class Renderer:
    def __init__(self, screen, world, player):
        self.screen = screen
        self.map = world
        self.pos = player.position
        self.dir = player.direction
    
    def render(self):
        self.raycast()

    def raycast(self):
        rays = 0
        for t in np.linspace(self.dir.angle() - math.radians(60), self.dir.angle() + math.radians(60), RAYCOUNT):
            target = Vector2(RAYLENGTH*math.cos(t) + self.pos.x, -RAYLENGTH*math.sin(t) + self.pos.y)

            # the following algorithm is supposed to be dda but it's like the fucked up twisted version from my deep psyche
            # viewer discretion advised >:)

            dx = target.x - self.pos.x
            dy = target.y - self.pos.y

            ddx = dx / abs(dy)
            ddy = -(dy / abs(dx)) # don't ask me why this is negative, found through trial and error

            mapx = int(self.pos.x / 128)
            mapy = int(self.pos.y / 128)

            sx = None
            sy = None

            sdx = None
            sdy = None

            if ddx < 0:
                sx = -1
                sdx = (self.pos.x - mapx*128) * ddx
            else:
                sx = 1
                sdx = ((mapx + 1)*128 - self.pos.x) * ddx

            if ddy < 0:
                sy = -1
                sdy = (self.pos.y - mapy*128) * ddy
            else:
                sy = 1
                sdy = ((mapy + 1)*128 - self.pos.y) * ddy

            hit = False

            while !hit:
                if sdx < sdy:
                    sdx += ddx
                    mapx += sx
                    side = 0
                else:
                    sdy += ddy
                    mapy += sy
                    side = 1

                if self.map[][] > 0:
                    hit = True
    
            pygame.draw.line(self.screen, 'red', self.pos.tuplify(), target.tuplify())

