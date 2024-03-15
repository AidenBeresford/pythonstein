import math
import pygame
import numpy as np
from engine.vector2 import Vector2
from player import Player

FOV = 90
RAYLENGTH = 1
WINDOW_RESOLUTION = (1280, 720)
TILE_SIZE = 64

class Renderer:
    def __init__(self, screen, world, player):
        self.screen = screen
        self.map = world
        self.pos = player.position
        self.dir = player.direction
    
    def render(self):
        self.raycast()

    def raycast(self):
        line = 0
        for t in np.linspace(self.dir.angle() - math.radians(FOV/2), self.dir.angle() + math.radians(FOV/2), WINDOW_RESOLUTION[0]):
            target = Vector2(RAYLENGTH*math.cos(t) + self.pos.x, -RAYLENGTH*math.sin(t) + self.pos.y)

            # the following algorithm is supposed to be dda but it's like the fucked up twisted version from my deep psyche
            # viewer discretion advised >:)

            dx = target.x - self.pos.x
            dy = target.y - self.pos.y

            ddx = abs(1 / dx) * TILE_SIZE
            ddy = abs(1 / dy) * TILE_SIZE

            mapx = math.floor(self.pos.x / TILE_SIZE)
            mapy = math.floor(self.pos.y / TILE_SIZE) 
          
            sx = None
            sy = None

            sdx = None
            sdy = None

            if dx < 0:
                sx = -1
                sdx = (self.pos.x - mapx*TILE_SIZE) * (ddx/TILE_SIZE)
            else:
                sx = 1
                sdx = ((mapx + 1)*TILE_SIZE - self.pos.x) * (ddx/TILE_SIZE)

            if dy < 0:
                sy = -1
                sdy = (self.pos.y - mapy*TILE_SIZE) * (ddy/TILE_SIZE)
            else:
                sy = 1
                sdy = ((mapy + 1)*TILE_SIZE - self.pos.y) * (ddy/TILE_SIZE)

            hit = False

            while hit == False:
                if sdx < sdy:
                    sdx += ddx
                    mapx += sx
                    side = 0
                else:
                    sdy += ddy
                    mapy += sy
                    side = 1
                
                if self.map[mapy][mapx] > 0:
                    hit = True
    
            if side == 0:
                pdist = sdx - ddx
            else:
                pdist = sdy - ddy

            pdist = 0.00001 if pdist == 0 else pdist

            h = WINDOW_RESOLUTION[1] / pdist * (TILE_SIZE/4)

            top = -h/2 + WINDOW_RESOLUTION[1]/pdist
            if top < -128:
                top = -127

            bottom = h/2 + WINDOW_RESOLUTION[1]/pdist
            if bottom >= h+128:
                bottom = h+127

            color = (255,255,255)

            if (side == 0):
                color = (color[0]/2, color[1]/2, color[2]/2)

            pygame.draw.line(self.screen, color, (line, top+128), (line, bottom+128))
            line += 1

