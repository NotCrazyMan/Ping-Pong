import pygame

pygame.init()

class R_L():
    def __init__(self, y1, filename):
        self.x = 20
        self.y1 = y1
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y1))

class R_R():
    def __init__(self, y2, filename):
        self.x = 20
        self.y2 = y2
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y2))
