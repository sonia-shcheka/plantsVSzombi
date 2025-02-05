import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

pygame.init()
screen_size = width, height = (1280, 590)
screen = pygame.display.set_mode(screen_size)
pygame.mixer_music.load('data/music.mp3')
pygame.mixer.music.play(-1)
FPS = 60
clock = pygame.time.Clock()
levels = [True, True, True]

def terminate():
    pygame.quit()
    sys.exit()


class Goroh(pygame.sprite.Sprite):
    def __init__(self, ne_str, x, y):
        super().__init__(all_sprites)
        self.ne_str = ne_str
        self.cur_frame = 0
        self.image = self.ne_str[self.cur_frame]
        self.rect = pygame.Rect(x - 20, y - 40, 60, 60)

    def update(self):
        self.cur_frame = (self.cur_frame + 8) % len(self.ne_str)
        self.image = self.ne_str[self.cur_frame]

    def goroh_strel(self, strel):
        self.cur_frame = 0
        self.image = strel[self.cur_frame]


class SunFlower(pygame.sprite.Sprite):
    def __init__(self, sun, x, y):
        super().__init__(all_sprites)
        self.sun = sun
        self.cur_frame = 0
        self.image = self.sun[self.cur_frame]
        self.rect = pygame.Rect(x - 20, y - 40, 60, 60)

    def update(self):
        self.cur_frame = (self.cur_frame + 8) % len(self.sun)
        self.image = self.sun[self.cur_frame]


class Sun(pygame.sprite.Sprite):
    def __init__(self, sun, x, y):
        super().__init__(all_sprites)
        self.sun = sun
        self.cur_frame = 0
        self.image = self.sun[self.cur_frame]
        self.rect = pygame.Rect(x - 20, y - 40, 60, 60)

    def update(self):
        pass


class Zombi(pygame.sprite.Sprite):
    def __init__(self, zombie_pai):
        super().__init__(all_sprites)
        self.zombie = zombie_pai
        self.cur_frame = 0
        self.image = self.zombie[self.cur_frame]
        self.rect = pygame.Rect(1280, 590, 150, 120)

    def update(self):
        pass

    def zombi_est(self, zombi_est_pai):
        self.cur_frame = 0
        self.image = zombi_est_pai[self.cur_frame]



class Cartoha(pygame.sprite.Sprite):
    def __init__(self, cartoha_pai, x, y):
        super().__init__(all_sprites, plants)
        self.cartoha = cartoha_pai
        self.cur_frame = 0
        self.image = self.cartoha[self.cur_frame]
        self.rect = pygame.Rect(x - 20, y - 40, 60, 60)

    def update(self):
        self.cur_frame = (self.cur_frame + 2) % len(self.cartoha)
        self.image = self.cartoha[self.cur_frame]


class Gazon(pygame.sprite.Sprite):
    def __init__(self, gazon, x, y):
        super().__init__(all_sprites, gazon_cos)
        self.gazon = gazon
        self.image = self.gazon
        self.rect = pygame.Rect(x - 20, y - 40, 60, 60)

    def update(self):
        pass


class Board:
    def __init__(self, widthh, heightt):
        self.width = widthh
        self.height = heightt
        self.board = [[0] * widthh for _ in range(heightt)]


def coord(event_pos):
    if 368 <= event_pos[0] <= 463 and 83 <= event_pos[1] <= 175:
        return 415, 129, (0, 0)
    elif 464 <= event_pos[0] <= 550 and 77 <= event_pos[1] <= 173:
        return 507, 125, (0, 1)
    elif 551 <= event_pos[0] <= 652 and 71 <= event_pos[1] <= 178:
        return 601, 124, (0, 2)
    elif 653 <= event_pos[0] <= 748 and 66 <= event_pos[1] <= 176:
        return 700, 121, (0, 3)
    elif 749 <= event_pos[0] <= 848 and 65 <= event_pos[1] <= 178:
        return 798, 122, (0, 4)
    elif 849 <= event_pos[0] <= 945 and 64 <= event_pos[1] <= 176:
        return 897, 121, (0, 5)
    elif 946 <= event_pos[0] <= 1041 and 67 <= event_pos[1] <= 178:
        return 993, 122, (0, 6)
    elif 1042 <= event_pos[0] <= 1139 and  78 <= event_pos[1] <= 178:
        return 1090, 128, (0, 7)
    elif 1140 <= event_pos[0] <= 1238 and 83 <= event_pos[1] <= 181:
        return 1189, 132, (0, 8)
    elif 361 <= event_pos[0] <= 459 and 174 <= event_pos[1] <= 270:
        return 410, 222, (1, 0)
    elif 460 <= event_pos[0] <= 547 and 174 <= event_pos[1] <= 271:
        return 503, 222, (1, 1)
    elif 548 <= event_pos[0] <= 650 and 179 <= event_pos[1] <= 270:
        return 599, 224, (1, 2)
    elif 651 <= event_pos[0] <= 752 and 177 <= event_pos[1] <= 274:
        return 701, 225, (1, 3)
    elif 753 <= event_pos[0] <= 840 and 179 <= event_pos[1] <= 272:
        return 796, 225, (1, 4)
    elif 841 <= event_pos[0] <= 945 and 177 <= event_pos[1] <= 270:
        return 893, 223, (1, 5)
    elif 946 <= event_pos[0] <= 1033 and 179 <= event_pos[1] <= 273:
        return 989, 226, (1, 6)
    elif 1034 <= event_pos[0] <= 1131 and 179 <= event_pos[1] <= 273:
        return 1082, 226, (1, 7)
    elif 1132 <= event_pos[0] <= 1249 and 182 <= event_pos[1] <= 273:
        return 1190, 227, (1, 8)
    elif 363 <= event_pos[0] <= 458 and 271 <= event_pos[1] <= 370:
        return 410, 320, (2, 0)
    elif 459 <= event_pos[0] <= 550 and 272 <= event_pos[1] <= 372:
        return 504, 322, (2, 1)
    elif 551 <= event_pos[0] <= 656 and 271 <= event_pos[1] <= 374:
        return 603, 322, (2, 2)
    elif 657 <= event_pos[0] <= 751 and 272 <= event_pos[1] <= 378:
        return 704, 325, (2, 3)
    elif 752 <= event_pos[0] <= 843 and 275 <= event_pos[1] <= 379:
        return 797, 327, (2, 4)
    elif 844 <= event_pos[0] <= 948 and 273 <= event_pos[1] <= 376:
        return 896, 324, (2, 5)
    elif 949 <= event_pos[0] <= 1033 and 274 <= event_pos[1] <= 378:
        return 991, 326, (2, 6)
    elif 1034 <= event_pos[0] <= 1137 and 274 <= event_pos[1] <= 379:
        return 1085, 326, (2, 7)
    elif 1138 <= event_pos[0] <= 1256 and 274 <= event_pos[1] <= 378:
        return 1197, 326, (2, 8)
    elif 360 <= event_pos[0] <= 455 and 371 <= event_pos[1] <= 461:
        return 407, 416, (3, 0)
    elif 456 <= event_pos[0] <= 551 and 373 <= event_pos[1] <= 463:
        return 503, 418, (3, 1)
    elif 552 <= event_pos[0] <= 652 and 375 <= event_pos[1] <= 466:
        return 602, 420, (3, 2)
    elif 653 <= event_pos[0] <= 751 and 379 <= event_pos[1] <= 464:
        return 702, 421, (3, 3)
    elif 752 <= event_pos[0] <= 843 and 380 <= event_pos[1] <= 462:
        return 797, 421, (3, 4)
    elif 844 <= event_pos[0] <= 945 and 377 <= event_pos[1] <= 462:
        return 894, 419, (3, 5)
    elif 946 <= event_pos[0] <= 1033 and 379 <= event_pos[1] <= 463:
        return 989, 421, (3, 6)
    elif 1034 <= event_pos[0] <= 1139 and 380 <= event_pos[1] <= 460:
        return 1086, 420, (3, 7)
    elif 1140 <= event_pos[0] <= 1252 and 379 <= event_pos[1] <= 460:
        return 1196, 419, (3, 8)
    elif 350 <= event_pos[0] <= 459 and 462 <= event_pos[1] <= 563:
        return 404, 512, (4, 0)
    elif 460 <= event_pos[0] <= 554 and 464 <= event_pos[1] <= 563:
        return 507, 513, (4, 1)
    elif 555 <= event_pos[0] <= 660 and 467 <= event_pos[1] <= 556:
        return 607, 511, (4, 2)
    elif 661 <= event_pos[0] <= 750 and 465 <= event_pos[1] <= 562:
        return 705, 513, (4, 3)
    elif 751 <= event_pos[0] <= 854 and 463 <= event_pos[1] <= 562:
        return 802, 512, (4, 4)
    elif 855 <= event_pos[0] <= 944 and 463 <= event_pos[1] <= 560:
        return 899, 511, (4, 5)
    elif 945 <= event_pos[0] <= 1042 and 464 <= event_pos[1] <= 561:
        return 993, 512, (4, 6)
    elif 1043 <= event_pos[0] <= 1138 and 461 <= event_pos[1] <= 562:
        return 1090, 511, (4, 7)
    elif 1139 <= event_pos[0] <= 1257 and 461 <= event_pos[1] <= 556:
        return 1198, 508, (4, 8)
    else:
        return None

def end_screen():
    fon = pygame.transform.scale(load_image('GameOver.png'), (1280, 590))
    screen.blit(fon, (0, 0))

def start_screen():
    fon = pygame.transform.scale(load_image('start_screen.PNG'), (1280, 590))
    screen.blit(fon, (0, 0))

    level1_pai = pygame.transform.scale(load_image('level1_pai.JPEG', -1), (250, 270))
    screen.blit(level1_pai, (85, 150))
    start_button1 = pygame.transform.scale(load_image('start_button.png', -1), (125, 30))
    screen.blit(start_button1, (147, 410))
    button1_rect = pygame.Rect(147, 410, 125, 30)
    red_start_button1 = pygame.transform.scale(load_image('red_start_button.JPEG', -1), (125, 30))

    level1_pai = pygame.transform.scale(load_image('level2_pai.JPEG', -1), (250, 270))
    start_button2 = pygame.transform.scale(load_image('start_button.png', -1), (125, 30))
    button2_rect = pygame.Rect(577, 410, 125, 30)
    red_start_button2 = pygame.transform.scale(load_image('red_start_button.JPEG', -1), (125, 30))

    level2_chb = pygame.transform.scale(load_image('level2_chb.jpg', -1), (250, 270))
    start_button2_chb = pygame.transform.scale(load_image('play_button_chb.jpg', -1), (125, 30))

    if not levels[1]:
        screen.blit(level2_chb, (515, 150))
        screen.blit(start_button2_chb, (577, 410))

    else:
        screen.blit(level1_pai, (515, 150))
        screen.blit(start_button2, (577, 410))

    level3_pai = pygame.transform.scale(load_image('level3_pai.JPEG', -1), (250, 270))
    start_button3 = pygame.transform.scale(load_image('start_button.png', -1), (125, 30))
    button3_rect = pygame.Rect(1007, 410, 125, 30)
    red_start_button3 = pygame.transform.scale(load_image('red_start_button.JPEG', -1), (125, 30))

    level3_chb = pygame.transform.scale(load_image('level3_chb.jpg', -1), (250, 270))
    start_button3_chb = pygame.transform.scale(load_image('play_button_chb.jpg', -1), (125, 30))

    if not levels[2]:
        screen.blit(level3_chb, (945, 150))
        screen.blit(start_button3_chb, (1007, 410))

    else:
        screen.blit(level3_pai, (945, 150))
        screen.blit(start_button3, (1007, 410))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button1_rect.collidepoint(event.pos):
                    return 1
                if levels[1]:
                    if button2_rect.collidepoint(event.pos):
                        return 2
                if levels[2]:
                    if button3_rect.collidepoint(event.pos):
                        return 3
        if button1_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(red_start_button1, (147, 410))
        elif not button1_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(start_button1, (147, 410))
        if levels[1]:
            if button2_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(red_start_button2, (577, 410))
            elif not button2_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(start_button2, (577, 410))
        if levels[2]:
            if button3_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(red_start_button3, (1007, 410))
            elif not button3_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(start_button3, (1007, 410))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)

def rules():
    fon = pygame.transform.scale(load_image('info_pic.PNG'), (1280, 590))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)

gorohi = {'gor': [], 'gor_fig': []}
zombie = {'go': [], 'est': []}
sun_flowers = []
cartoha_s =[]
inf = False

for i in range(50):
    if i != 0:
        filename = 'goroh/frame-{}.gif'.format(i)
        img = load_image(filename)
        img.set_colorkey((0, 0, 0))
        img_gor = pygame.transform.scale(img, (60, 60))
        gorohi['gor'].append(img_gor)

        filename1 = 'goroh_str/frame-{}.gif'.format(i)
        img1 = load_image(filename1)
        img1.set_colorkey((0, 0, 0))
        img_gor_str = pygame.transform.scale(img1, (60, 60))
        gorohi['gor_fig'].append(img_gor_str)

        filename2 = 'sun_flower/frame-{}.gif'.format(i)
        img2 = load_image(filename2)
        img2.set_colorkey((0, 0, 0))
        img_sun_flower = pygame.transform.scale(img2, (60, 60))
        sun_flowers.append(img_sun_flower)

for i in range(47):
    if i != 0:
        filename = 'zombi_go/frame-{}.gif'.format(i)
        img = load_image(filename)
        img.set_colorkey((0, 0, 0))
        img_zombie_go = pygame.transform.scale(img, (120,120))
        zombie['go'].append(img_zombie_go)

for i in range(22, 36):
    filename = 'cartoha/frame-{}.gif'.format(i)
    img = load_image(filename)
    img.set_colorkey((0, 0, 0))
    img_cartoha = pygame.transform.scale(img, (120, 120))
    cartoha_s.append(img_cartoha)

for i in range(40):
    if i != 0:
        filename = 'zombi_est/frame-{}.gif'.format(i)
        img = load_image(filename)
        img.set_colorkey((0, 0, 0))
        img_zombie_est = pygame.transform.scale(img, (120,120))
        zombie['est'].append(img_zombie_est)


def level1():
    fon_s = pygame.transform.scale(load_image('start_game.PNG'), (1280, 590))

    sun_amount = pygame.transform.scale(load_image('sun_place.PNG'), (150, 70))

    tr = pygame.transform.scale(load_image('gazon.webp'), (70, 50))
    Gazon(tr, 310, 132)
    Gazon(tr, 310, 224)
    Gazon(tr, 310, 322)
    Gazon(tr, 310, 418)
    Gazon(tr, 310, 517)

    goroh = pygame.transform.scale(load_image('goroh.png'), (125, 65))
    button_goroh = pygame.Rect(50, 25, 125, 70)

    start_time = pygame.time.get_ticks()
    show_text = True

    running = True
    while running:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False

        screen.blit(fon_s, (0, 0))
        screen.blit(sun_amount, (200, 25))
        screen.blit(goroh, (50, 25))

        pygame.draw.rect(screen, (255, 255, 0),
                         (360, 263, 894, 115), 3)

        if button_goroh.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 25, 125, 70), 3)

        intro_text = "Первый уровень проходит только на этой полосе"
        font = pygame.font.Font(None, 50)
        string_rendered = font.render(intro_text, 1, (120, 255, 165))


        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 5000:
            show_text = False

        if show_text:
            screen.blit(string_rendered, (360, 458))

        pygame.display.flip()

def level2():
    fon_s = pygame.transform.scale(load_image('start_game.PNG'), (1280, 590))
    sun_amount = pygame.transform.scale(load_image('sun_place.PNG'), (150, 70))

    tr = pygame.transform.scale(load_image('gazon.webp'), (70, 50))
    Gazon(tr, 310, 132)
    Gazon(tr, 310, 224)
    Gazon(tr, 310, 322)
    Gazon(tr, 310, 418)
    Gazon(tr, 310, 517)

    goroh = pygame.transform.scale(load_image('goroh.png'), (125, 65))
    button_goroh = pygame.Rect(50, 25, 125, 70)
    sun_flower = pygame.transform.scale(load_image('podsolnuh.png'), (125, 65))
    button_sun_flower = pygame.Rect(50, 120, 125, 70)

    start_time = pygame.time.get_ticks()
    show_text = True

    clock.tick(FPS)
    running = True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            if events.type == pygame.MOUSEBUTTONDOWN:
                print(events.pos)
        screen.blit(fon_s, (0, 0))
        screen.blit(sun_amount, (200, 25))
        screen.blit(goroh, (50, 25))
        screen.blit(sun_flower, (50, 120))

        if button_goroh.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 25, 125, 70), 3)

        if button_sun_flower.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 120, 125, 70), 3)
        pygame.draw.rect(screen, (255, 255, 0),
                         (360, 174, 898, 286), 3)

        intro_text = ["Второй уровень проходит", 'только на этих 3-ех полосах']
        font = pygame.font.Font(None, 50)
        string_rendered = font.render(intro_text[0], 1, (120, 255, 165))
        string_rendered1 = font.render(intro_text[1], 1, (120, 255, 165))

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 5000:
            show_text = False

        if show_text:
            screen.blit(string_rendered, (500, 458))
            screen.blit(string_rendered1, (500, 488))


        pygame.display.flip()

def level3():
    fon_s = pygame.transform.scale(load_image('start_game.PNG'), (1280, 590))
    sun_amount = pygame.transform.scale(load_image('sun_place.PNG'), (150, 70))
    goroh = pygame.transform.scale(load_image('goroh.png'), (125, 65))
    button_goroh = pygame.Rect(50, 25, 125, 70)
    sun_flower = pygame.transform.scale(load_image('podsolnuh.png'), (125, 65))
    button_sun_flower = pygame.Rect(50, 120, 125, 70)
    cartoha = pygame.transform.scale(load_image('cartoha.jpg'), (125, 65))
    button_cartoha = pygame.Rect(50, 215, 125, 70)

    tr = pygame.transform.scale(load_image('gazon.webp'), (70, 50))
    Gazon(tr, 310, 132)
    Gazon(tr, 310, 224)
    Gazon(tr, 310, 322)
    Gazon(tr, 310, 418)
    Gazon(tr, 310, 517)

    clock.tick(60)
    running = True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        screen.blit(fon_s, (0, 0))
        screen.blit(sun_amount, (200, 25))
        screen.blit(goroh, (50, 25))
        screen.blit(sun_flower, (50, 120))
        screen.blit(cartoha, (50, 215))

        if button_goroh.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 25, 125, 70), 3)

        if button_sun_flower.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 120, 125, 70), 3)

        if button_cartoha.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 215, 125, 70), 3)

        pygame.display.flip()

all_sprites = pygame.sprite.Group()
plants = pygame.sprite.Group()
zombi = pygame.sprite.Group()
gazon_cos = pygame.sprite.Group()
a = start_screen()
board = Board(9, 5)

if a == 1:
    rules()
    level1()

elif a == 2:
    level2()

elif a == 3:
    level3()

pygame.quit()
sys.exit()