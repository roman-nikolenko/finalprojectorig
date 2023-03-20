import pygame
from main import W, H

class Meteor:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.px = x
        self.py = y
        self.image = pygame.image.load('meteor.jpg')
        self.target_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.px, self.py(0, W - 30), -100
        self.speed = 3
        targets.append(self)

    def update(self):
        self.py += self.speed
        self.rect.y = self.py
        if self.rect.top > H:
            targets.remove(self)

    def draw(self):
        self.screen.blit(self.image, self.target_rect)


targets = []