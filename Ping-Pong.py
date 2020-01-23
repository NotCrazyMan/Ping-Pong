import pygame
import random
import sys

# Вводим цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
# Даём размер окна
size = (700, 500)
screen = pygame.display.set_mode(size)
# Называем игровое окно
pygame.display.set_caption("Ping-Pong_Original")
# Шрифт
font = pygame.font.Font(None, 40)
font = pygame.font.Font(None, 30)
# Счётчик голов
score1 = 0
score2 = 0
On = "Sound On"
Off = "Sound Off"

# Координаты мячика
x = 345
y = 255
# Координаты левой ракетки
y1 = 225
y1s = 0
# Координаты правой ракетки
y2 = 225
y2s = 0

# Loop until the user clicks the close button.
done = False

# Делаем фпс в игре
# Точнее делаем время обнавления игры кадров в секунду
clock = pygame.time.Clock()

# ----- Вводи спрайты в игру -----
# Координаты заднего фона
background_position = [0, 0]
# Загружаем задний фон
background_image = pygame.image.load("pictures/Поле пинг-понг.png").convert()
# Загружаем спрайт левой ракетки
player_image = pygame.image.load("pictures/Ракетка левая.png").convert()
# Загружаем спрайт правой ракетки
player_image1 = pygame.image.load("pictures/Ракетка правая.png").convert()
# Загружаем спрайт мячика
ball_image = pygame.image.load("pictures/Мяч пин-понг.png").convert()
# Делаем черный цвет прозрачным для спрайта мячика
ball_image.set_colorkey(BLACK)

# Рандомайзер для направления мячика с начала игры
xh = 0
yh = 0
# скорость мячика
xs = 0
ys = 0
SoundSettings = 0


# --------- Создание гл. Меню ---------
class Menu():
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.bitmap = pygame.image.load(filename)

    def menu(self):
        done = True
        # -- Позиция кнопки Start --
        # Верхний левый угл Start
        start_pos = (250, 150)
        s_p_x = start_pos[0]
        s_p_y = start_pos[1]
        # Правый нижний угл Start
        start_pos1 = (450, 200)
        s_p1_x = start_pos1[0]
        s_p1_y = start_pos1[1]
        # -- Позиция кнопки Quit --
        quit_pos = (250, 239)
        # Верхний левый угл Quit
        q_p_x = quit_pos[0]
        q_p_y = quit_pos[1]
        quit_pos1 = (450, 289)
        # Правый нижний угл Quit
        q_p1_x = quit_pos1[0]
        q_p1_y = quit_pos1[1]
        # ---- Гл. Цикл гл. меню ----
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False
                    # Работа с мышкой
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Опознание позиции мышки
                    pos = pygame.mouse.get_pos()
                    posx = pos[0]
                    posy = pos[1]
                    # Проверка позиции мышки и кнопки Start
                    if s_p_x < posx < s_p1_x and s_p_y < posy < s_p1_y:
                        done = False
                    elif q_p_x < posx < q_p1_x and q_p_y < posy < q_p1_y:
                        sys.exit()
                    elif s_p_x < posx < s_p1_x and s_p_y < posy < s_p1_y:
                        SoundSettings = 1
                    # Выход из игры через кнопку ESCAPE
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        done = False
            #    test_s = font.render(On, True, BLACK)
            #    test_s1 = font.render(Off, True, BLACK)
            #    if SoundSettings == 0:
            #        screen.blit(text_s, [420, 410])
            #    if SoundSettings == 1:
            ##screen.blit(text_1, [420, 410])

            screen.blit(self.bitmap, (self.x, self.y))
            pygame.display.flip()


# Даём координаты и запускаем выше написаный код
plunt = Menu(0, 0, "pictures/Набросок_гл_меню.png")
# Применение цикла в классе
plunt.menu()

# Добавление звуков
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
if SoundSettings == 0:
    SoundHit1 = pygame.mixer.Sound("music/Звук_Шар1.ogg")
    SoundHit2 = pygame.mixer.Sound("music/Звук_Шар2.ogg")
    SoundHit3 = pygame.mixer.Sound("music/Звук_Шар3.ogg")
    Goal = pygame.mixer.Sound("music/Goal.ogg")


    # Рандомазейр звков для ударов
    def RandPlay():
        s = random.randrange(0, 3)
        if s == 0:
            SoundHit1.play()
        if s == 1:
            SoundHit2.play()
        if s == 2:
            SoundHit3.play()

# -------- Главный цикл -----------
while not done:
    # --- Главный действие цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

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
            # Закрывание через ESCAPE
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
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y2s = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                y1s = 0

    # Изменение координат учитывая код скорости выше
    y2 = y2 + y2s
    y1 = y1 + y1s

    # Текст (Score)
    # Он здесь находиться чтобы текст обновлялся каждый раз
    # Когда шарик сталкиваеться со стенкой
    text1 = font.render(str(score1), True, BLACK)
    text2 = font.render(str(score2), True, BLACK)

    # Преграда для ракеток чтобы не вылезали за экран
    if y2 > 450:
        y2 -= 3
    if y2 < 0:
        y2 += 3
    if y1 > 450:
        y1 -= 3
    if y1 < 0:
        y1 += 3

    # --- ЛОГИКА
    # Движение мячика в сторону
    x += xs
    y += ys

    # Отталкивание мячика от стен по у
    if y > 490 or y < 0:
        ys = ys * -1
        # рандомный звук при столкновение верхних стен
        # RandPlay()
    if x > 690 or x < 0:
        xs = xs * -1
        # рандомный звук при столкновение верхних стен
        # RandPlay()

    # Зачисление очков при попадание шарика
    # на сторону противника
    if x > 690:
        xs = 0
        ys = 0
        x = 345
        y = 255
        score1 += 1
        # Звук гола при проходе мячика за ракетку
        Goal.play()
        y1 = 225
        y2 = 225
    if x < 0:
        xs = 0
        ys = 0
        x = 345
        y = 255
        score2 += 1
        # Звук гола при проходе мячика за ракетку
        Goal.play()
        y1 = 225
        y2 = 225
    # Отталкивание мячика от ракеток
    if 30 < x < 34 and y1 - 8 < y < y1 + 62:
        if 30 < x < 34 and y1 - 8 < y + 10 < y1 + 62:
            xs = xs * -1
            # Рандомный звук при ударе с ракеткой
            RandPlay()

        if not (xs and ys == 3 and -3):
            # Ускоритель шарика
            xs += 0.1
            ys += 0.1

    if 660 < x + 10 < 664 and y2 - 8 < y < y2 + 62:
        if 660 < x + 10 < 664 and y2 - 8 < y + 10 < y2 + 62:
            xs = xs * -1
            # Рандомный звук при ударе с ракеткой
            RandPlay()
        # Ускоритель и также блокиратор скорости
        if not (xs and ys == 3 or -3):
            # Ускоритель шарика
            xs -= 0.1
            ys -= 0.1

    # Если вы хотите задний фон, поместись здесь
    # Задний фон
    screen.blit(background_image, background_position)

    # --- Здесь должен быть код для рисования

    screen.blit(player_image, [20, y1])
    screen.blit(player_image1, [660, y2])

    screen.blit(ball_image, [x, y])
    screen.blit(text1, [320, 10])
    screen.blit(text2, [363, 10])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Здесь определяем кол-во фпс в игре
    clock.tick(120)

# Закрываем игру
pygame.quit()
