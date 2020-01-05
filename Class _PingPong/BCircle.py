import pygame

pygame.init()

class Ball():
    def __inti__(self, filename):
        self.x = 345
        self.y = 255
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y))
