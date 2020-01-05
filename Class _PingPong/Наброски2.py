import pygame

class Menu():
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.bitmap = pygame.image.load(filename)
    def menu(self):
        done = True


        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False



            screen.blit(self.bitmap, (self.x, self.y))
            pygame.display.flip()

plunt = Menu(0,0,"Наброс_гл_меню.png" )
plunt.menu()
