import pygame

pygame.init()

class Background():
    def __init__(self, filename):
        self.x = 0
        self.y = 0
        self.filename = pygame.image.load("Поле пинг-понг.png")
    def render(self):
        screen.blit(self.filename,(self.x,self.y))
