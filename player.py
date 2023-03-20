import pygame
import pygame as pg

class Player:
    def __init__(self, screen):
        """инициализация"""
        self.screen = screen
        self.image = pygame.image.load('New project.png')
        self.player_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.player_rect.centerx = self.screen_rect.centerx
        self.player_rect.bottom = self.screen_rect.bottom

    def draw(self):
        """отрисовка"""
        self.screen.blit(self.image, self.player_rect)
