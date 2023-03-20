import pygame
import pygame as pg
from player import Player
from targets import Meteor

SIZE = W, H = 854, 480
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Итоговый проект')

player = Player(screen)
target = Meteor(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(BLACK)
    player.draw()
    target.draw()
    target.update()
    pygame.display.flip()
