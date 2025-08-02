from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)

    current_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
  
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        for asteroid in asteroids:
            if current_player.collides(asteroid):
                print("Game over!")
                return
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
