import pygame
import random
import sys
BLACK = (0, 0, 0)
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ping-Pong_CLass")
# Шрифт
font = pygame.font.Font(None, 40)
# Счётчик голов
score1 = 0
score2 = 0
# ------ Создаём класс фона ------

class BackG():
    def __init__(self, xpos, ypos, filename):
        self.xpos = 0
        self.ypos = 0
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap, (self.xpos, self.ypos))

background = BackG(0,0,"pictures/Поле пинг-понг.png")
# ------ Создаём класс ракеток ------
y1 = 225
y1s = 0
y2 = 225
y2s = 0

class Rockets():
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

RLeft = Rockets(20, y1, "pictures/Ракетка левая.png")
RRight = Rockets(660, y2, "pictures/Ракетка правая.png")
# ------ Создаём класс шарика ------
class BCircle():
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

ball = BCircle(345,250,"pictures/Мяч пин-понг.png")

class Menu():
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.bitmap = pygame.image.load(filename)
    def menu(self):
        done = True
        # Позиция кнопки Start
        start_pos = (250,150)
        s_p_x = start_pos[0]
        s_p_y = start_pos[1]
        start_pos1 = (450,200)
        s_p1_x = start_pos1[0]
        s_p1_y = start_pos1[1]
        # Позиция кнопки Quit
        quit_pos = (250, 239)
        q_p_x = quit_pos[0]
        q_p_y = quit_pos[1]
        quit_pos1 = (450, 289)
        q_p1_x = quit_pos1[0]
        q_p1_y = quit_pos1[1]
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    posx = pos[0]
                    posy = pos[1]
                    if s_p_x < posx < s_p1_x and s_p_y < posy < s_p1_y:
                        done = False
                    elif q_p_x < posx < q_p1_x and q_p_y < posy < q_p1_y:
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()


            screen.blit(self.bitmap, (self.x, self.y))

            pygame.display.flip()

plunt = Menu(0,0,"pictures/Набросок_гл_меню.png" )
plunt.menu()


# Рандомайзер для направления мячика с начала игры
xh = 0
yh = 0
# скорость мячика
xs = 0
ys = 0

SoundHit1 = pygame.mixer.Sound("music/Звук_Шар1.ogg")
SoundHit2 = pygame.mixer.Sound("music/Звук_Шар2.ogg")
SoundHit3 = pygame.mixer.Sound("music/Звук_Шар3.ogg")
Goal = pygame.mixer.Sound("music/Goal.ogg")
def RandPlay():
        s = random.randrange(0,3)
        if s == 0:
            SoundHit1.play()
        if s == 1:
            SoundHit2.play()
        if s == 2:
            SoundHit3.play()

# Подготовка к запуску игры
done = True
clock = pygame.time.Clock()
# ---- Главный цикл ----
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

# Управление ракетками
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y1s = -3
            elif event.key == pygame.K_s:
                y1s = +3
            elif event.key == pygame.K_UP:
                y2s = -3
            elif event.key == pygame.K_DOWN:
                y2s = 3
        # - Закрывание через ESCAPE -
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        # Принажатии кнопки SPACE скорость начнёт передаваться мячику
            elif event.key == pygame.K_SPACE:
                # В зависимости от рандома выше, в таком направлении и будет лететь мяч
                # по х
                xh = random.randrange(0, 2)
                if xh == 0:
                    xs = -2
                if xh == 1:
                    xs = 2
                # по у
                yh = random.randrange(0, 2)
                if yh == 0:
                    ys = -2
                if yh == 1:
                    ys = 2
        #  Пауза игры
            elif event.key == pygame.K_b:
                xs = 0
                ys = 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                y1s = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y2s = 0

# Скорость ракеток
    RLeft.y = RLeft.y + y1s
    RRight.y = RRight.y + y2s

    # Текст (Score)
    # Он здесь находиться чтобы текст обновлялся каждый раз
    # Когда шарик сталкиваеться со стенкой
    text1 = font.render(str(score1), True, BLACK)
    text2 = font.render(str(score2), True, BLACK)
# Сталкивание со стенами по у
    if RLeft.y > 450:
        RLeft.y -= 3
    if RLeft.y < 0:
        RLeft.y += 3
    if RRight.y > 450:
        RRight.y -= 3
    if RRight.y < 0:
        RRight.y += 3
    # --- ЛОГИКА
    # Движение мячика в сторону
    x_pamat = xs
    y_pamat = ys
    ball.x += xs
    ball.y += ys
    # Отталкивание мячика от стен по у
    if ball.y > 490 or ball.y < 0:
        ys = ys * -1
        RandPlay()
    if ball.x > 690 or ball.x < 0:
        xs = xs * -1
        RandPlay()

    if ball.x > 690:
        xs = 0
        ys = 0
        ball.x = 345
        ball.y = 250
        score1 += 1
        Goal.play()
        RLeft.y1 = 225
        RRight.y2 = 225
    if ball.x < 0:
        xs = 0
        ys = 0
        ball.x = 345
        ball.y = 250
        score2 += 1
        Goal.play()
        RLeft.y1 = 225
        RRight.y2 = 225
    # Лево верхний и ниж углы
    if 660 < ball.x < 665 and RLeft.y < ball.y < RLeft.y+50:
        xs = xs * -1
        RandPlay()
        #Ускоритель шарика
        xs += 0.1
        ys += 0.1
    if 30 < ball.x < 35 and RLeft.y < ball.y+10 < RLeft.y+50:
        xs = xs * -1
        RandPlay()
        #Ускоритель шарика
        xs += 0.1
        ys += 0.1
    # Право верхний и ниж углы
    if 20 < ball.x+10 < 25 and RRight.y < ball.y < RRight.y+50:
        xs = xs * -1
        RandPlay()
        #Ускоритель шарика
        xs -= 0.1
        ys -= 0.1
    if 660 < ball.x+10 < 665 and RRight.y < ball.y+10 < RRight.y+50:
        xs = xs * -1
        RandPlay()
        #Ускоритель шарика
        xs -= 0.1
        ys -= 0.1
    background.render()

    ball.render()
    RLeft.render()
    RRight.render()
    screen.blit(text1, [320, 10])
    screen.blit(text2, [363, 10])

    pygame.display.flip()

    clock.tick(120)

pygame.quit()
