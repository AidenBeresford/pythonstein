import pygame
import math
from player import Player
from renderer import Renderer
from engine.vector2 import Vector2 

DEFAULT_CLEAR_COLOR = pygame.Color(0, 0, 0, 255)
WINDOW_RESOLUTION = (1280,720)
FRAMES_PER_SECOND = 60
TILE_SIZE = 64

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_RESOLUTION)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0 # delta time
        self.player = Player(Vector2(8*64, 4*64))
        self.move_speed = 150

        self.map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1],
                    [1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
                    [1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
                    [1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1],
                    [1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,1],
                    [1,2,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
                    [1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]] 

        self.renderer = Renderer(self.screen, self.map, self.player)

    def __del__(self):
        self.quit()

    def loop(self):
        
        self.front = Vector2(self.player.x + self.player.direction.x*10, self.player.y - self.player.direction.y*10)
        self.back = Vector2(self.player.x - self.player.direction.x*10, self.player.y + self.player.direction.y*10)

        self.input_handler()
        
        self.screen.fill(DEFAULT_CLEAR_COLOR)

        self.renderer.render()
        pygame.display.flip()
        self.dt = self.clock.tick(FRAMES_PER_SECOND) / 1000
        
    def quit(self):
        pygame.quit()

    # user input methods
    def input_handler(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        self.movement_input(keys)

    def movement_input(self, keys):
        if keys[pygame.K_w]:
            if self.map[int(self.front.y/TILE_SIZE)][int(self.front.x/TILE_SIZE)] == 0:
                self.player.y -= self.move_speed * math.sin(self.player.direction.angle()) * self.dt
                self.player.x += self.move_speed * math.cos(self.player.direction.angle()) * self.dt
        if keys[pygame.K_s]:
            if self.map[int(self.back.y/TILE_SIZE)][int(self.back.x/TILE_SIZE)] == 0:
                self.player.y += self.move_speed * math.sin(self.player.direction.angle()) * self.dt
                self.player.x -= self.move_speed * math.cos(self.player.direction.angle()) * self.dt
        if keys[pygame.K_a]:
            self.player.direction.rotate(-.1)
        if keys[pygame.K_d]:
            self.player.direction.rotate(.1)
        if keys[pygame.K_LSHIFT]:
            self.move_speed = 300
        else:
            self.move_speed = 150

def main():
    game = Game()
    while game.running:
        game.loop()
    del game

if __name__ == '__main__':
    main()

