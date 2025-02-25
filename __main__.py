import pygame
import os
import sys
import time
import random
import sqlite3

WIDTH = 1280
HEIGHT = 590

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
screen_size = width, height = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.mixer_music.load('data/music.mp3')
pygame.mixer.music.play(-1)
FPS = 60
clock = pygame.time.Clock()
levels = []
con = sqlite3.connect('levels_pvz')
cur = con.cursor()
result = cur.execute("""SELECT * FROM levels""").fetchall()
for elem in result:
    for i in elem:
        if i != 'lvl':
            levels.append(i)
con.close()

def terminate():
    pygame.quit()
    sys.exit()


class Goroh(pygame.sprite.Sprite):
    def __init__(self, ne_str, x, y, *group):
        super().__init__(pea_sprites, *group)
        self.ne_str = ne_str
        self.cur_frame = 0
        self.image = self.ne_str[self.cur_frame]
        self.rect = pygame.Rect(x - 20, y - 40, 60, 60)
        self.hp = 120

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.ne_str)
        self.image = self.ne_str[self.cur_frame]


class GorohStrel(pygame.sprite.Sprite):
    def __init__(self, fight, x, y, *group):
        super().__init__(pea_shooter_strel, pea_shooter_strel, *group)
        self.fight = fight
        self.cur_frame = 0
        self.image = self.fight[self.cur_frame]
        self.rect = pygame.Rect(x - 20, y - 40, 30, 60)
        self.hp = 120

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.fight)
        self.image = self.fight[self.cur_frame]
        if self.cur_frame == 29:
            Pea(self.rect.x + 10, self.rect.y)


class SunFlower(pygame.sprite.Sprite):
    def __init__(self, sun, x, y):
        super().__init__(all_sprites, sun_sprites)
        self.sun = sun
        self.cur_frame = 0
        self.hp = 120
        self.image = self.sun[self.cur_frame]
        self.rect = pygame.Rect(x - 40, y - 60, 60, 60)

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.sun)
        self.image = self.sun[self.cur_frame]


class Zombi(pygame.sprite.Sprite):
    def __init__(self, zombie_pai, x, y, hp):
        super().__init__(zombie_go_sprites, all_sprites)
        self.zombie = zombie_pai
        self.cur_frame = 0
        self.image = self.zombie[self.cur_frame]
        self.hp = hp
        self.rect = pygame.Rect(x, y, 40, 150)
        self.q = 0

    def update(self):
        if self.q == 3:
            if self.rect.x >= 260:
                self.rect.x -= 5
                self.q = 0
        else:
            self.q += 1
            self.cur_frame = (self.cur_frame + 1) % len(self.zombie)
            self.image = self.zombie[self.cur_frame]


class ZombieEat(pygame.sprite.Sprite):
    def __init__(self, zombie_pai, x, y, hp):
        super().__init__(zombie_eat_sprites, all_sprites)
        self.zombie = zombie_pai
        self.cur_frame = 0
        self.image = self.zombie[self.cur_frame]
        self.rect = pygame.Rect(x, y, 40, 150)
        self.hp = hp
        self.q = 0

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.zombie)
        self.image = self.zombie[self.cur_frame]


class Pea(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(pea_sprites, all_sprites)
        image = load_image('Pea.png')
        self.image = pygame.transform.scale(image, (20, 20))
        self.rect = pygame.Rect(x, y + 10, 5, 10)
        self.speed = 10

    def update(self):
        if self.rect.x <= WIDTH:
            self.rect.x += self.speed


class Cartoha(pygame.sprite.Sprite):
    def __init__(self, cartoha_pai, x, y):
        super().__init__(all_sprites, cartoha_sprites)
        self.cartoha = cartoha_pai
        self.cur_frame = 0
        self.hp = 260
        self.image = self.cartoha[self.cur_frame]
        self.rect = pygame.Rect(x - 27, y - 47, 60, 60)

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.cartoha)
        self.image = self.cartoha[self.cur_frame]


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
    fon = pygame.transform.scale(load_image('GameOver.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    running = True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        time.sleep(5)
    sys.exit()

def start_screen():
    fon = pygame.transform.scale(load_image('start_screen.PNG'), (WIDTH, HEIGHT))
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

    if levels[1] == 'False':
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

    if levels[2] == 'False':
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
                if levels[1] == 'True':
                    if button2_rect.collidepoint(event.pos):
                        return 2
                if levels[2] == 'True':
                    if button3_rect.collidepoint(event.pos):
                        return 3
        if button1_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(red_start_button1, (147, 410))
        elif not button1_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(start_button1, (147, 410))
        if levels[1] == 'True':
            if button2_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(red_start_button2, (577, 410))
            elif not button2_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(start_button2, (577, 410))
        if levels[2] == 'True':
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

def rules1():
    fon = pygame.transform.scale(load_image('nothomezombi.jpg'), (1280, 590))
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

def rules2():
    fon = pygame.transform.scale(load_image('sunlov.jpg'), (1280, 590))
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

def rules3():
    fon = pygame.transform.scale(load_image('2open.jpg'), (1280, 590))
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

goroh_nestrel = []
goroh_strel = []
zombie_go = []
zombie_eat = []
sun_flowers = []
cartoha_s = []
s = None
inf = False

for i in range(50):
    if i != 0:
        filename = 'goroh/frame-{}.gif'.format(i)
        img = load_image(filename)
        img.set_colorkey((0, 0, 0))
        img_gor = pygame.transform.scale(img, (60, 60))
        goroh_nestrel.append(img_gor)

        filename1 = 'goroh_str/frame-{}.gif'.format(i)
        img1 = load_image(filename1)
        img1.set_colorkey((0, 0, 0))
        img_gor_str = pygame.transform.scale(img1, (60, 60))
        goroh_strel.append(img_gor_str)

        filename2 = 'sun_flower/frame-{}.gif'.format(i)
        img2 = load_image(filename2)
        img2.set_colorkey((0, 0, 0))
        img_sun_flower = pygame.transform.scale(img2, (80, 80))
        sun_flowers.append(img_sun_flower)

for i in range(47):
    if i != 0:
        filename = 'zombi_go/frame-{}.gif'.format(i)
        img = load_image(filename)
        img.set_colorkey((0, 0, 0))
        img_zombie_go = pygame.transform.scale(img, (150,150))
        zombie_go.append(img_zombie_go)

for i in range(44):
    if i != 0:
        filename = 'cartoha/frame-{}.gif'.format(i)
        img = load_image(filename)
        img.set_colorkey((0, 0, 0))
        img_cartoha = pygame.transform.scale(img, (60, 60))
        cartoha_s.append(img_cartoha)

for i in range(40):
    if i != 0:
        filename = 'zombi_est/frame-{}.gif'.format(i)
        img = load_image(filename)
        img.set_colorkey((0, 0, 0))
        img_zombie_est = pygame.transform.scale(img, (150, 150))
        zombie_eat.append(img_zombie_est)

def level1():
    fon_s = pygame.transform.scale(load_image('start_game.PNG'), (WIDTH, HEIGHT))
    victory = pygame.transform.scale(load_image('victory.png'), (500, 150))

    sun_amount = pygame.transform.scale(load_image('sun_place.PNG'), (150, 70))

    goroh = pygame.transform.scale(load_image('goroh.png'), (125, 65))
    button_goroh = pygame.Rect(50, 25, 125, 70)
    vybor_goroh = 0
    ne_strel = True

    plants_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    amount = 150
    amount_zombies = 5

    sun = load_image("sun.JPEG", -1)
    sun = pygame.transform.scale(sun, (50, 50))
    current_state_sun = 1
    speed = 1
    wait_time = 17000
    wait_start_time = 0
    image_rect = sun.get_rect()
    image_rect.x = random.randrange(368, 1256)
    image_rect.y = -50

    spawn_delay = 7000
    last_spawn = pygame.time.get_ticks()

    font = pygame.font.Font(None, 50)
    sun_amount_text = font.render(str(amount), 1, (169, 169, 169))

    start_time = pygame.time.get_ticks()
    show_text = True

    counter, text = 3, '3'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont(None, 150)

    running = True
    while running:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                terminate()
            if events.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else ''
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                if image_rect.collidepoint(events.pos):
                    amount += 25
                    current_state_sun = 1
                    sun_amount_text = font.render(str(amount), 1, (169, 169, 169))
                    wait_start_time = pygame.time.get_ticks()
                elif button_goroh.collidepoint(events.pos):
                    pygame.draw.rect(screen, (255, 255, 0),
                                     (50, 25, 125, 70), 3)
                    vybor_goroh = 1
            if events.type == pygame.MOUSEBUTTONDOWN:
                coords = coord(events.pos)
                if coords is not None:
                    if amount >= 100:
                        if vybor_goroh == 1:
                            if coords[2][0] == 2:
                                if plants_list[coords[2][1]] == 0:
                                    shooter = Goroh(goroh_nestrel, coords[0], coords[1], pea_shooter_line2)
                                    plants_list[coords[2][1]] = (shooter, 1)
                                    GorohStrel(goroh_strel, coords[0], coords[1], pea_shooter_strel_line2)
                                    vybor_goroh = 0
                                    amount -= 100
                                    sun_amount_text = font.render(str(amount), 1, (169, 169, 169))

        screen.blit(fon_s, (0, 0))
        screen.blit(sun_amount, (200, 25))
        screen.blit(goroh, (50, 25))
        screen.blit(font.render(text, True, (255, 0, 0)), (640, 295))
        screen.blit(sun_amount_text, (264, 41))
        pygame.draw.rect(screen, (255, 255, 0),
                         (360, 263, 894, 115), 3)

        if button_goroh.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 25, 125, 70), 3)

        if amount_zombies == 0 and zombie_list[2] == []:
            con_db = sqlite3.connect("levels_pvz")
            cur_db = con_db.cursor()
            cur_db.execute("""UPDATE levels SET level2 = 'True' WHERE True_False = 'lvl'""")
            con_db.commit()
            con_db.close()
            screen.blit(victory, (390, 220))
            pygame.display.flip()
            time.sleep(5)
            screen.fill((0, 0, 0))
            pygame.display.flip()
            all_sprites.empty()
            pea_shooter_strel.empty()
            pea_sprites.empty()
            pea_shooter_line2.empty()
            pea_shooter_strel_line2.empty()
            zombie_go_sprites.empty()
            zombie_eat_sprites.empty()
            running = False

        now = pygame.time.get_ticks()
        if now - last_spawn >= spawn_delay:
            if amount_zombies != 0:
                Zombi(zombie_go, WIDTH - 120, 222, 140)
                zombie_list[2].append(0)
                spawn_delay = random.randrange(5000, 13000, 1000)
                last_spawn = now
                amount_zombies -= 1

        if zombie_list[2]:
            ne_strel = False

        for pea in pea_sprites:
            for zombie_go_spr in zombie_go_sprites:
                if pygame.sprite.collide_mask(pea, zombie_go_spr):
                    pea.kill()
                    if zombie_go_spr.hp != 0:
                        zombie_go_spr.hp -= 20
                    else:
                        zombie_go_spr.kill()
                        zombie_list[2].remove(0)
                        if not zombie_list[2]:
                            ne_strel = False

        for pea_shooters in pea_shooter_strel:
            for zombie_go_spr in zombie_go_sprites:
                if pygame.sprite.collide_mask(pea_shooters, zombie_go_spr):
                    ZombieEat(zombie_eat, zombie_go_spr.rect.x - 75, zombie_go_spr.rect.y, zombie_go_spr.hp)
                    zombie_go_spr.kill()

        for pea in pea_sprites:
            for zombie_est_spr in zombie_eat_sprites:
                if pygame.sprite.collide_mask(pea, zombie_est_spr):
                    pea.kill()
                    if zombie_est_spr.hp != 0:
                        zombie_est_spr.hp -= 20
                    else:
                        zombie_est_spr.kill()
                        zombie_list[2].remove(0)
                        if not zombie_list[2]:
                            ne_strel = False

        for pea_shooters in pea_shooter_strel:
            for zombie_eat_spr in zombie_eat_sprites:
                if pygame.sprite.collide_mask(pea_shooters, zombie_eat_spr):
                    if pea_shooters.hp != 0:
                        pea_shooters.hp -= 0.5
                    else:
                        coor = coord((pea_shooters.rect.x, pea_shooters.rect.y))
                        plants_list[coor[2][1]][0].kill()
                        plants_list[coor[2][1]] = 0
                        pea_shooters.kill()
                        Zombi(zombie_go, zombie_eat_spr.rect.x, zombie_eat_spr.rect.y, zombie_eat_spr.hp)
                        zombie_eat_spr.kill()

        for zomb in zombie_go_sprites:
            if zomb.rect.x <= 270:
                fon_s = pygame.transform.scale(load_image('GameOver.png'), (WIDTH, HEIGHT))
                screen.blit(fon_s, (0, 0))
                pygame.display.flip()
                time.sleep(5)
                terminate()

        if current_state_sun == 0:
            screen.blit(sun, (image_rect.x, image_rect.y))
            image_rect.y += speed
            if image_rect.top > HEIGHT:
                current_state_sun = 1
                wait_start_time = pygame.time.get_ticks()

        elif current_state_sun == 1:
            if pygame.time.get_ticks() - wait_start_time > wait_time:
                current_state_sun = 0
                image_rect.y = -50
                wait_time = 10000
                image_rect.x = random.randrange(368, 1256)

        all_sprites.draw(screen)
        all_sprites.update()

        if ne_strel:
            pea_shooter_line2.draw(screen)
            pea_shooter_line2.update()
        else:
            pea_shooter_strel_line2.draw(screen)
            pea_shooter_strel_line2.update()

        intro_text = "Первый уровень проходит только на этой полосе"
        font = pygame.font.Font(None, 50)
        string_rendered = font.render(intro_text, 1, (120, 255, 165))

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 3000:
            show_text = False

        if show_text:
            screen.blit(string_rendered, (360, 458))

        clock.tick(FPS)
        pygame.display.flip()

def level2():
    fon_s = pygame.transform.scale(load_image('start_game.PNG'), (WIDTH, HEIGHT))
    victory = pygame.transform.scale(load_image('victory.png'), (500, 150))

    sun_amount = pygame.transform.scale(load_image('sun_place.PNG'), (150, 70))

    goroh = pygame.transform.scale(load_image('goroh.png'), (125, 65))
    button_goroh = pygame.Rect(50, 25, 125, 70)
    vybor = 0
    ne_strel = [False, False, False, False, False]

    sun_flower = pygame.transform.scale(load_image('podsolnuh.png'), (125, 65))
    sun_flower_button = pygame.Rect(50, 120, 125, 70)

    plants_list = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                   [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                   [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                   [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                   [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]]

    amount = 150
    amount_zombies = 10

    sun = load_image("sun.JPEG", -1)
    sun = pygame.transform.scale(sun, (50, 50))
    suny = pygame.transform.scale(sun, (40, 40))
    current_state_sun = 1
    speed = 1
    wait_time = 25000
    wait_time_sun = 10000
    sunies = []
    wait_start_time = 0
    image_rect = sun.get_rect()
    image_rect.x = random.randrange(368, 1256)
    image_rect.y = -50

    spawn_delay = 15000
    last_spawn = pygame.time.get_ticks()

    font = pygame.font.Font(None, 50)
    sun_amount_text = font.render(str(amount), 1, (169, 169, 169))

    start_time = pygame.time.get_ticks()
    show_text = True

    counter, text = 3, '3'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont(None, 150)

    running = True
    while running:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                terminate()
            if events.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else ''
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                if image_rect.collidepoint(events.pos):
                    amount += 25
                    current_state_sun = 1
                    sun_amount_text = font.render(str(amount), 1, (169, 169, 169))
                    wait_start_time = pygame.time.get_ticks()
                elif button_goroh.collidepoint(events.pos):
                    pygame.draw.rect(screen, (255, 255, 0),
                                     (50, 25, 125, 70), 3)
                    vybor = 1
                elif sun_flower_button.collidepoint(events.pos):
                    pygame.draw.rect(screen, (255, 255, 0),
                                     (50, 120, 125, 70), 3)
                    vybor = 2
                for co_sun in sunies:
                    suny_rect = pygame.Rect(co_sun[1], co_sun[2], 40, 40)
                    if suny_rect.collidepoint(events.pos):
                        amount += 25
                        sun_amount_text = font.render(str(amount), 1, (169, 169, 169))
                        co_sun[3] = False
            if events.type == pygame.MOUSEBUTTONDOWN:
                coords = coord(pygame.mouse.get_pos())
                if coords is not None:
                    if coords[2][0] == 2 or coords[2][0] == 1 or coords[2][0] == 3:
                        if vybor == 1:
                            if amount >= 100:
                                if plants_list[coords[2][0]][coords[2][1]] == (0, 0):
                                    group_g = 'pea_shooter_line{}'.format(coords[2][0])
                                    shooter = Goroh(goroh_nestrel, coords[0], coords[1], eval(group_g))
                                    x = coords[2][0]
                                    y = coords[2][1]
                                    group_gs = 'pea_shooter_strel_line{}'.format(coords[2][0])
                                    shooter_strel = GorohStrel(goroh_strel, coords[0], coords[1], eval(group_gs))
                                    plants_list[x][y] = (shooter, shooter_strel)
                                    vybor = 0
                                    amount -= 100
                                    sun_amount_text = font.render(str(amount), 1, (169, 169, 169))
                        elif vybor == 2:
                            if amount >= 50:
                                if plants_list[coords[2][0]][coords[2][1]] == (0, 0):
                                    flower = SunFlower(sun_flowers, coords[0], coords[1])
                                    x = coords[2][0]
                                    y = coords[2][1]
                                    plants_list[x][y] = (flower, flower)
                                    sunies.append([pygame.time.get_ticks(), coords[0], coords[1], False])
                                    vybor = 0
                                    amount -= 50
                                    sun_amount_text = font.render(str(amount), 1, (169, 169, 169))

        screen.blit(fon_s, (0, 0))
        screen.blit(sun_amount, (200, 25))
        screen.blit(goroh, (50, 25))
        screen.blit(sun_flower, (50, 120))
        screen.blit(font.render(text, True, (255, 0, 0)), (640, 295))
        screen.blit(sun_amount_text, (264, 41))
        pygame.draw.rect(screen, (255, 255, 0),
                         (360, 174, 898, 286), 3)

        if button_goroh.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 25, 125, 70), 3)
        if sun_flower_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 120, 125, 70), 3)

        if amount_zombies == 0 and zombie_list == [[], [], [], [], []]:
            con_db = sqlite3.connect("levels_pvz")
            cur_db = con_db.cursor()
            cur_db.execute("""UPDATE levels SET level3 = 'True' WHERE True_False = 'lvl'""")
            con_db.commit()
            con_db.close()
            screen.blit(victory, (390, 220))
            pygame.display.flip()
            time.sleep(5)
            screen.fill((0, 0, 0))
            pygame.display.flip()
            all_sprites.empty()
            pea_shooter_strel.empty()
            pea_sprites.empty()
            pea_shooter_line1.empty()
            pea_shooter_strel_line1.empty()
            pea_shooter_line2.empty()
            pea_shooter_strel_line2.empty()
            pea_shooter_line3.empty()
            pea_shooter_strel_line3.empty()
            zombie_go_sprites.empty()
            zombie_eat_sprites.empty()
            running = False

        now = pygame.time.get_ticks()
        if now - last_spawn >= spawn_delay:
            if amount_zombies != 0:
                y = None
                line = random.randrange(1, 4)
                if line == 1:
                    y = 120
                elif line == 2:
                    y = 230
                elif line == 3:
                    y = 313
                zomb = Zombi(zombie_go, WIDTH - 120, y, 120)
                zombie_list[line].append(zomb)
                spawn_delay = random.randrange(9000, 13000, 1000)
                last_spawn = now
                amount_zombies -= 1
                ne_strel[line] = True

        sun_now = pygame.time.get_ticks()
        for suni in sunies:
            if sunies:
                if sun_now - suni[0] >= wait_time_sun:
                    suni[3] = True
                    suni[0] = pygame.time.get_ticks()

        for suni in sunies:
            if sunies:
                if suni[3]:
                    screen.blit(suny, (suni[1] + 10, suni[2]))

        for pea in pea_sprites:
            for zombie_go_spr in zombie_go_sprites:
                if pygame.sprite.collide_mask(pea, zombie_go_spr):
                    pea.kill()
                    if zombie_go_spr.hp != 0:
                        zombie_go_spr.hp -= 20
                    else:
                        zombi_del = 144
                        for z in range(len(zombie_list)):
                            for y in range(len(zombie_list[z])):
                                if zombie_list[z][y] == zombie_go_spr:
                                    zombi_del = z
                        if zombi_del != 144:
                            zombie_list[zombi_del].remove(zombie_go_spr)
                            if not zombie_list[zombi_del]:
                                ne_strel[zombi_del] = False
                        zombie_go_spr.kill()

        for pea_shooters in pea_shooter_strel:
            for zombie_go_spr in zombie_go_sprites:
                if pygame.sprite.collide_mask(pea_shooters, zombie_go_spr):
                    line1 = 0
                    line2 = 0
                    for z in range(len(zombie_list)):
                        for y in range(len(zombie_list[z])):
                            if zombie_list[z][y] == zombie_go_spr:
                                line1 = z
                    for p in range(5):
                        for y in range(9):
                            if plants_list[p][y]:
                                if pea_shooters == plants_list[p][y][1]:
                                    line2 = p
                    if line1 == line2:
                        zome = ZombieEat(zombie_eat, zombie_go_spr.rect.x - 75, zombie_go_spr.rect.y, zombie_go_spr.hp)
                        zombie_list[line1].remove(zombie_go_spr)
                        zombie_list[line1].append(zome)
                        zombie_go_spr.kill()

        for sun_flow in sun_sprites:
            for zombie_go_spr in zombie_go_sprites:
                if pygame.sprite.collide_mask(sun_flow, zombie_go_spr):
                    line1 = 0
                    line2 = 0
                    for z in range(len(zombie_list)):
                        for y in range(len(zombie_list[z])):
                            if zombie_list[z][y] == zombie_go_spr:
                                line1 = z
                    for p in range(5):
                        for y in range(9):
                            if plants_list[p][y]:
                                if sun_flow == plants_list[p][y][1]:
                                    line2 = p
                    if line1 == line2:
                        zome = ZombieEat(zombie_eat, zombie_go_spr.rect.x - 75, zombie_go_spr.rect.y, zombie_go_spr.hp)
                        zombie_list[line1].remove(zombie_go_spr)
                        zombie_list[line1].append(zome)
                        zombie_go_spr.kill()

        for sun_flow in sun_sprites:
            for zombie_eat_spr in zombie_eat_sprites:
                if pygame.sprite.collide_mask(sun_flow, zombie_eat_spr):
                    if sun_flow.hp != 0:
                        sun_flow.hp -= 0.5
                    else:
                        for sho in range(5):
                            for y in range(9):
                                for t in range(2):
                                    if plants_list[sho][y][t] == sun_flow:
                                        plants_list[sho][y][0].kill()
                                        plants_list[sho][y] = (0, 0)
                                        for sunie in sunies:
                                            if sunie[1] == (sun_flow.rect.x + 40) and sunie[2] == (sun_flow.rect.y + 60):
                                                del sunies[sunies.index(sunie)]
                                        sun_flow.kill()
                        zome = Zombi(zombie_go, zombie_eat_spr.rect.x, zombie_eat_spr.rect.y, zombie_eat_spr.hp)
                        for z in range(len(zombie_list)):
                            for e in range(len(zombie_list[z])):
                                if zombie_list[z][e] == zombie_eat_spr:
                                    zombie_list[z].remove(zombie_eat_spr)
                                    zombie_list[z].append(zome)
                        zombie_eat_spr.kill()

        for pea in pea_sprites:
            for zombie_est_spr in zombie_eat_sprites:
                if pygame.sprite.collide_mask(pea, zombie_est_spr):
                    pea.kill()
                    if zombie_est_spr.hp != 0:
                        zombie_est_spr.hp -= 20
                    else:
                        zombi_del = 144
                        for z in range(len(zombie_list)):
                            for y in range(len(zombie_list[z])):
                                if zombie_list[z][y] == zombie_est_spr:
                                    zombi_del = z
                        if zombi_del != 144:
                            zombie_list[zombi_del].remove(zombie_est_spr)
                            if not zombie_list[zombi_del]:
                                ne_strel[zombi_del] = False
                        zombie_est_spr.kill()

        for pea_shooters in pea_shooter_strel:
            for zombie_eat_spr in zombie_eat_sprites:
                if pygame.sprite.collide_mask(pea_shooters, zombie_eat_spr):
                    if pea_shooters.hp != 0:
                        pea_shooters.hp -= 0.5
                    else:
                        for sho in range(5):
                            for y in range(9):
                                for t in range(2):
                                    if plants_list[sho][y][t] == pea_shooters:
                                        plants_list[sho][y][0].kill()
                                        plants_list[sho][y] = (0, 0)
                                        pea_shooters.kill()
                        zome = Zombi(zombie_go, zombie_eat_spr.rect.x, zombie_eat_spr.rect.y, zombie_eat_spr.hp)
                        for z in range(len(zombie_list)):
                            for e in range(len(zombie_list[z])):
                                if zombie_list[z][e] == zombie_eat_spr:
                                    zombie_list[z].remove(zombie_eat_spr)
                                    zombie_list[z].append(zome)
                        zombie_eat_spr.kill()

        for zomb in zombie_go_sprites:
            if zomb.rect.x <= 270:
                fon_s = pygame.transform.scale(load_image('GameOver.png'), (WIDTH, HEIGHT))
                screen.blit(fon_s, (0, 0))
                pygame.display.flip()
                time.sleep(5)
                terminate()

        if current_state_sun == 0:
            screen.blit(sun, (image_rect.x, image_rect.y))
            image_rect.y += speed
            if image_rect.top > HEIGHT:
                current_state_sun = 1
                wait_start_time = pygame.time.get_ticks()

        elif current_state_sun == 1:
            if pygame.time.get_ticks() - wait_start_time > wait_time:
                current_state_sun = 0
                image_rect.y = -50
                wait_time = 10000
                image_rect.x = random.randrange(368, 1256)

        all_sprites.draw(screen)
        all_sprites.update()

        for stre in range(len(ne_strel)):
            if ne_strel[stre]:
                shot = eval('pea_shooter_strel_line{}'.format(stre))
                shot.draw(screen)
                shot.update()
            else:
                shot = eval('pea_shooter_line{}'.format(stre))
                shot.draw(screen)
                shot.update()

        intro_text = ["Второй уровень проходит", 'только на этих 3-ех полосах']
        font = pygame.font.Font(None, 50)
        string_rendered = font.render(intro_text[0], 1, (120, 255, 165))
        string_rendered1 = font.render(intro_text[1], 1, (120, 255, 165))

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 3000:
            show_text = False

        if show_text:
            screen.blit(string_rendered, (500, 458))
            screen.blit(string_rendered1, (500, 488))

        clock.tick(FPS)
        pygame.display.flip()

def level3():
    cartoha = pygame.transform.scale(load_image('cartoha.jpg'), (125, 65))
    button_cartoha = pygame.Rect(50, 215, 125, 70)

    fon_s = pygame.transform.scale(load_image('start_game.PNG'), (WIDTH, HEIGHT))
    victory = pygame.transform.scale(load_image('victory.png'), (500, 150))

    sun_amount = pygame.transform.scale(load_image('sun_place.PNG'), (150, 70))

    goroh = pygame.transform.scale(load_image('goroh.png'), (125, 65))
    button_goroh = pygame.Rect(50, 25, 125, 70)
    vybor = 0
    ne_strel = [False, False, False, False, False]

    sun_flower = pygame.transform.scale(load_image('podsolnuh.png'), (125, 65))
    sun_flower_button = pygame.Rect(50, 120, 125, 70)

    plants_list = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                   [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                   [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                   [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                   [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]]

    amount = 150
    amount_zombies = 10

    sun = load_image("sun.JPEG", -1)
    sun = pygame.transform.scale(sun, (50, 50))
    suny = pygame.transform.scale(sun, (40, 40))
    current_state_sun = 1
    speed = 1
    wait_time = 25000
    wait_time_sun = 10000
    sunies = []
    wait_start_time = 0
    image_rect = sun.get_rect()
    image_rect.x = random.randrange(368, 1256)
    image_rect.y = -50

    spawn_delay = 15000
    last_spawn = pygame.time.get_ticks()

    font1 = pygame.font.SysFont(None, 50)
    sun_amount_text = font1.render(str(amount), 1, (169, 169, 169))

    counter, text = 3, '3'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    running = True
    while running:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                terminate()
            if events.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else ''
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                if image_rect.collidepoint(events.pos):
                    amount += 25
                    current_state_sun = 1
                    sun_amount_text = font1.render(str(amount), 1, (169, 169, 169))
                    wait_start_time = pygame.time.get_ticks()
                elif button_goroh.collidepoint(events.pos):
                    pygame.draw.rect(screen, (255, 255, 0),
                                     (50, 25, 125, 70), 3)
                    vybor = 1
                elif sun_flower_button.collidepoint(events.pos):
                    pygame.draw.rect(screen, (255, 255, 0),
                                     (50, 120, 125, 70), 3)
                    vybor = 2
                elif button_cartoha.collidepoint(events.pos):
                    pygame.draw.rect(screen, (255, 255, 0),
                                     (50, 215, 125, 70), 3)
                    vybor = 3
                for co_sun in sunies:
                    suny_rect = pygame.Rect(co_sun[1], co_sun[2], 40, 40)
                    if suny_rect.collidepoint(events.pos):
                        amount += 25
                        sun_amount_text = font1.render(str(amount), 1, (169, 169, 169))
                        co_sun[3] = False
            if events.type == pygame.MOUSEBUTTONDOWN:
                coords = coord(pygame.mouse.get_pos())
                if coords is not None:
                    if vybor == 1:
                        if amount >= 100:
                            if plants_list[coords[2][0]][coords[2][1]] == (0, 0):
                                group_g = 'pea_shooter_line{}'.format(coords[2][0])
                                shooter = Goroh(goroh_nestrel, coords[0], coords[1], eval(group_g))
                                x = coords[2][0]
                                y = coords[2][1]
                                group_gs = 'pea_shooter_strel_line{}'.format(coords[2][0])
                                shooter_strel = GorohStrel(goroh_strel, coords[0], coords[1], eval(group_gs))
                                plants_list[x][y] = (shooter, shooter_strel)
                                vybor = 0
                                amount -= 100
                                sun_amount_text = font1.render(str(amount), 1, (169, 169, 169))
                    elif vybor == 2:
                        if amount >= 50:
                            if plants_list[coords[2][0]][coords[2][1]] == (0, 0):
                                flower = SunFlower(sun_flowers, coords[0], coords[1])
                                x = coords[2][0]
                                y = coords[2][1]
                                plants_list[x][y] = (flower, flower)
                                sunies.append([pygame.time.get_ticks(), coords[0], coords[1], False])
                                vybor = 0
                                amount -= 50
                                sun_amount_text = font1.render(str(amount), 1, (169, 169, 169))
                    elif vybor == 3:
                        if amount >= 50:
                            if plants_list[coords[2][0]][coords[2][1]] == (0, 0):
                                flower = Cartoha(cartoha_s, coords[0], coords[1])
                                x = coords[2][0]
                                y = coords[2][1]
                                plants_list[x][y] = (flower, flower)
                                vybor = 0
                                amount -= 50
                                sun_amount_text = font1.render(str(amount), 1, (169, 169, 169))

        screen.blit(fon_s, (0, 0))
        screen.blit(sun_amount, (200, 25))
        screen.blit(goroh, (50, 25))
        screen.blit(sun_flower, (50, 120))
        screen.blit(font1.render(text, True, (255, 0, 0)), (640, 295))
        screen.blit(sun_amount_text, (264, 41))
        screen.blit(cartoha, (50, 215))

        if button_goroh.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 25, 125, 70), 3)
        if sun_flower_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 120, 125, 70), 3)
        if button_cartoha.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 255, 0),
                             (50, 215, 125, 70), 3)

        if amount_zombies == 0 and zombie_list == [[], [], [], [], []]:
            con_db = sqlite3.connect("levels_pvz")
            cur_db = con_db.cursor()
            cur_db.execute("""UPDATE levels SET level3 = 'True' WHERE True_False = 'lvl'""")
            con_db.commit()
            con_db.close()
            screen.blit(victory, (390, 220))
            pygame.display.flip()
            time.sleep(5)
            screen.fill((0, 0, 0))
            pygame.display.flip()
            all_sprites.empty()
            pea_shooter_strel.empty()
            pea_sprites.empty()
            zombie_go_sprites.empty()
            zombie_eat_sprites.empty()
            running = False

        now = pygame.time.get_ticks()
        if now - last_spawn >= spawn_delay:
            if amount_zombies != 0:
                y = None
                line = random.randrange(0, 5)
                if line == 0:
                    y = 30
                if line == 1:
                    y = 120
                elif line == 2:
                    y = 230
                elif line == 3:
                    y = 313
                if line == 4:
                    y = 405
                zomb = Zombi(zombie_go, WIDTH - 120, y, 120)
                zombie_list[line].append(zomb)
                spawn_delay = random.randrange(8000, 13000, 1000)
                last_spawn = now
                amount_zombies -= 1
                ne_strel[line] = True

        sun_now = pygame.time.get_ticks()
        for suni in sunies:
            if sunies:
                if sun_now - suni[0] >= wait_time_sun:
                    suni[3] = True
                    suni[0] = pygame.time.get_ticks()

        for suni in sunies:
            if sunies:
                if suni[3]:
                    screen.blit(suny, (suni[1] + 10, suni[2]))

        for pea in pea_sprites:
            for zombie_go_spr in zombie_go_sprites:
                if pygame.sprite.collide_mask(pea, zombie_go_spr):
                    pea.kill()
                    if zombie_go_spr.hp != 0:
                        zombie_go_spr.hp -= 20
                    else:
                        zombi_del = 144
                        for z in range(len(zombie_list)):
                            for y in range(len(zombie_list[z])):
                                if zombie_list[z][y] == zombie_go_spr:
                                    zombi_del = z
                        if zombi_del != 144:
                            print(zombie_list)
                            zombie_list[zombi_del].remove(zombie_go_spr)
                            print(zombie_list)
                            if not zombie_list[zombi_del]:
                                print(ne_strel)
                                ne_strel[zombi_del] = False
                        zombie_go_spr.kill()

        for pea_shooters in pea_shooter_strel:
            for zombie_go_spr in zombie_go_sprites:
                if pygame.sprite.collide_mask(pea_shooters, zombie_go_spr):
                    line1 = 0
                    line2 = 0
                    for z in range(len(zombie_list)):
                        for y in range(len(zombie_list[z])):
                            if zombie_list[z][y] == zombie_go_spr:
                                line1 = z
                    for p in range(5):
                        for y in range(9):
                            if plants_list[p][y]:
                                if pea_shooters == plants_list[p][y][1]:
                                    line2 = p
                    if line1 == line2:
                        zome = ZombieEat(zombie_eat, zombie_go_spr.rect.x - 75, zombie_go_spr.rect.y, zombie_go_spr.hp)
                        zombie_list[line1].remove(zombie_go_spr)
                        zombie_list[line1].append(zome)
                        zombie_go_spr.kill()

        for cartoh in cartoha_sprites:
            for zombie_go_spr in zombie_go_sprites:
                if pygame.sprite.collide_mask(cartoh, zombie_go_spr):
                    line1 = 0
                    line2 = 0
                    for z in range(len(zombie_list)):
                        for y in range(len(zombie_list[z])):
                            if zombie_list[z][y] == zombie_go_spr:
                                line1 = z
                    for p in range(5):
                        for y in range(9):
                            if plants_list[p][y]:
                                if cartoh == plants_list[p][y][1]:
                                    line2 = p
                    if line1 == line2:
                        zome = ZombieEat(zombie_eat, zombie_go_spr.rect.x - 75, zombie_go_spr.rect.y, zombie_go_spr.hp)
                        zombie_list[line1].remove(zombie_go_spr)
                        zombie_list[line1].append(zome)
                        zombie_go_spr.kill()

        for cartoh in cartoha_sprites:
            for zombie_eat_spr in zombie_eat_sprites:
                if pygame.sprite.collide_mask(cartoh, zombie_eat_spr):
                    if cartoh.hp != 0:
                        cartoh.hp -= 0.5
                    else:
                        for sho in range(5):
                            for y in range(9):
                                for t in range(2):
                                    if plants_list[sho][y][t] == cartoh:
                                        plants_list[sho][y][0].kill()
                                        plants_list[sho][y] = (0, 0)
                                        cartoh.kill()
                        zome = Zombi(zombie_go, zombie_eat_spr.rect.x, zombie_eat_spr.rect.y, zombie_eat_spr.hp)
                        for z in range(len(zombie_list)):
                            for e in range(len(zombie_list[z])):
                                if zombie_list[z][e] == zombie_eat_spr:
                                    zombie_list[z].remove(zombie_eat_spr)
                                    zombie_list[z].append(zome)
                        zombie_eat_spr.kill()

        for sun_flow in sun_sprites:
            for zombie_go_spr in zombie_go_sprites:
                if pygame.sprite.collide_mask(sun_flow, zombie_go_spr):
                    line1 = 0
                    line2 = 0
                    for z in range(len(zombie_list)):
                        for y in range(len(zombie_list[z])):
                            if zombie_list[z][y] == zombie_go_spr:
                                line1 = z
                    for p in range(5):
                        for y in range(9):
                            if plants_list[p][y]:
                                if sun_flow == plants_list[p][y][1]:
                                    line2 = p
                    if line1 == line2:
                        zome = ZombieEat(zombie_eat, zombie_go_spr.rect.x - 75, zombie_go_spr.rect.y, zombie_go_spr.hp)
                        zombie_list[line1].remove(zombie_go_spr)
                        zombie_list[line1].append(zome)
                        zombie_go_spr.kill()

        for sun_flow in sun_sprites:
            for zombie_eat_spr in zombie_eat_sprites:
                if pygame.sprite.collide_mask(sun_flow, zombie_eat_spr):
                    if sun_flow.hp != 0:
                        sun_flow.hp -= 0.5
                    else:
                        for sho in range(5):
                            for y in range(9):
                                for t in range(2):
                                    if plants_list[sho][y][t] == sun_flow:
                                        plants_list[sho][y][0].kill()
                                        plants_list[sho][y] = (0, 0)
                                        for sunie in sunies:
                                            if sunie[1] == (sun_flow.rect.x + 40) and sunie[2] == (
                                                    sun_flow.rect.y + 60):
                                                del sunies[sunies.index(sunie)]
                                        sun_flow.kill()
                        zome = Zombi(zombie_go, zombie_eat_spr.rect.x, zombie_eat_spr.rect.y, zombie_eat_spr.hp)
                        for z in range(len(zombie_list)):
                            for e in range(len(zombie_list[z])):
                                if zombie_list[z][e] == zombie_eat_spr:
                                    zombie_list[z].remove(zombie_eat_spr)
                                    zombie_list[z].append(zome)
                        zombie_eat_spr.kill()

        for pea in pea_sprites:
            for zombie_est_spr in zombie_eat_sprites:
                if pygame.sprite.collide_mask(pea, zombie_est_spr):
                    pea.kill()
                    if zombie_est_spr.hp != 0:
                        zombie_est_spr.hp -= 20
                    else:
                        zombi_del = 144
                        for z in range(len(zombie_list)):
                            for y in range(len(zombie_list[z])):
                                if zombie_list[z][y] == zombie_est_spr:
                                    zombi_del = z
                        if zombi_del != 144:
                            zombie_list[zombi_del].remove(zombie_est_spr)
                            if not zombie_list[zombi_del]:
                                ne_strel[zombi_del] = False
                        zombie_est_spr.kill()

        for pea_shooters in pea_shooter_strel:
            for zombie_eat_spr in zombie_eat_sprites:
                if pygame.sprite.collide_mask(pea_shooters, zombie_eat_spr):
                    if pea_shooters.hp != 0:
                        pea_shooters.hp -= 0.5
                    else:
                        for sho in range(5):
                            for y in range(9):
                                for t in range(2):
                                    if plants_list[sho][y][t] == pea_shooters:
                                        plants_list[sho][y][0].kill()
                                        plants_list[sho][y] = (0, 0)
                                        pea_shooters.kill()
                        zome = Zombi(zombie_go, zombie_eat_spr.rect.x, zombie_eat_spr.rect.y, zombie_eat_spr.hp)
                        for z in range(len(zombie_list)):
                            for e in range(len(zombie_list[z])):
                                if zombie_list[z][e] == zombie_eat_spr:
                                    zombie_list[z].remove(zombie_eat_spr)
                                    zombie_list[z].append(zome)
                        zombie_eat_spr.kill()

        for zomb in zombie_go_sprites:
            if zomb.rect.x <= 270:
                fon_s = pygame.transform.scale(load_image('GameOver.png'), (WIDTH, HEIGHT))
                screen.blit(fon_s, (0, 0))
                pygame.display.flip()
                time.sleep(5)
                terminate()

        if current_state_sun == 0:
            screen.blit(sun, (image_rect.x, image_rect.y))
            image_rect.y += speed
            if image_rect.top > HEIGHT:
                current_state_sun = 1
                wait_start_time = pygame.time.get_ticks()

        elif current_state_sun == 1:
            if pygame.time.get_ticks() - wait_start_time > wait_time:
                current_state_sun = 0
                image_rect.y = -50
                wait_time = 10000
                image_rect.x = random.randrange(368, 1256)

        all_sprites.draw(screen)
        all_sprites.update()

        for stre in range(len(ne_strel)):
            if ne_strel[stre]:
                shot = eval('pea_shooter_strel_line{}'.format(stre))
                shot.draw(screen)
                shot.update()
            else:
                shot = eval('pea_shooter_line{}'.format(stre))
                shot.draw(screen)
                shot.update()

        clock.tick(FPS)
        pygame.display.flip()

all_sprites = pygame.sprite.Group()
sun_sprites = pygame.sprite.Group()
cartoha_sprites = pygame.sprite.Group()
pea_shooter_line0 = pygame.sprite.Group()
pea_shooter_strel_line0 = pygame.sprite.Group()
pea_shooter_line1 = pygame.sprite.Group()
pea_shooter_strel_line1 = pygame.sprite.Group()
pea_shooter_line2 = pygame.sprite.Group()
pea_shooter_strel_line2 = pygame.sprite.Group()
pea_shooter_line3 = pygame.sprite.Group()
pea_shooter_strel_line3 = pygame.sprite.Group()
pea_shooter_line4 = pygame.sprite.Group()
pea_shooter_strel_line4 = pygame.sprite.Group()
pea_sprites = pygame.sprite.Group()
pea_shooter_strel = pygame.sprite.Group()
zombie_go_sprites = pygame.sprite.Group()
zombie_eat_sprites = pygame.sprite.Group()
zombie_list = [[], [], [], [], []]
a = start_screen()

if a == 1:
    rules()
    rules1()
    rules2()
    rules3()
    level1()
    zombie_list = [[], [], [], [], []]
    a = 2

if a == 2:
    level2()
    zombie_list = [[], [], [], [], []]
    a = 3

if a == 3:
    level3()

if s == 4:
    end_screen()

pygame.quit()
sys.exit()