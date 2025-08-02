from constants import *
import player
import pygame

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    current_player = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        current_player.update(dt)
        screen.fill("black")
        current_player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
