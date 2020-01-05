import pygame

class Rocket1:
    def __init__(self, y1, filename): #убрал х из подачи
#    "Перемешение по х и у ракетки"
        self.x = 20
        self.y1 = y1 #255
        self.bitmap=pygame.image.load(filename)

    def r_ender(self, screen):
        screen.blit(self.bitmap(self.x, self.y1))

    def control(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y1s = -3
            elif event.key == pygame.K_s:
                y1s = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key ==pygame.K_s:
                y1s = 0
#y1 = y1 + y1s

#    if y1 > 450:
#        y1 -= 3
#    if y1 < 0:
#        y1 += 3
#Столкновение с шариком
# Лево-верхнего
# Лево-нижнего
