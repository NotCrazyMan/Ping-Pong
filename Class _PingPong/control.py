import pygame

pygame.init()

class Control():
    def __init__(self):
        self.done = True
        self.y1s = 0
        self.y2s = 0

    def C_ontrol(self):
        # Основной цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            # --- Взаимодействия пользователей с дощечками
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y2s = -3
                elif event.key == pygame.K_DOWN:
                    y2s = 3

                elif event.key == pygame.K_w:
                    y1s = -3
                elif event.key == pygame.K_s:
                    y1s = 3

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y2s = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    y1s = 0
