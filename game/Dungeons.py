import pygame
import sys

pygame.init()
scr = pygame.display.set_mode((1250, 750))
pygame.display.set_caption("Dungeons")

icon = pygame.image.load('foto/icon/Avatar.jpg')
pygame.display.set_icon(icon)

menu_music = 'Music/nejnoe-spokoynoe-bezmyatejnoe-raznogolosoe-penie-ptits-v-lesu.mp3'
tutor_music = 'Music/morning-garden-acoustic-chill-15013_[cut_68sec].mp3'
scene1_music = 'Music/suspense-background-music-332370.mp3'

pygame.mixer.music.load(menu_music)
pygame.mixer.music.play(-1)

font = pygame.font.SysFont('arial', 40)
WHITE = (255, 255, 255)
text_tutor1 = font.render('Щиро радий тебе бачити в моєму проекті ', False, 'white')
text_tutor2 = font.render('коротко раскажу як тут рухатися щоб іти в перед потрібно', False, 'white')
text_tutor3 = font.render('нажати на стрілку в прово ащо в назад стрілку в ліво ', False, 'white')
text_tutor4 = font.render('стрибнути потрібно нажати x тепер ти готовий ', False, 'white')
text_tutor5 = font.render('переїти в наступний рівень для того нажми Lctrl', False, 'white')


background = pygame.image.load('foto/scene/Menu_bg.jpg')
level1 = pygame.image.load('foto/scene/Tutorial_BG.png')
jorj = pygame.image.load('foto/5253577204917465249-removebg-preview.png')
tutorpeople = pygame.image.load('foto/charencter/Vizard_tutorial_4-removebg-preview.png')
level2 = pygame.image.load('foto/scene/Tutorial_BG.png')
teleport = pygame.image.load('foto/charencter/pixil-frame-0.png')
level3 = pygame.image.load('foto/scene/scene3.jpg')
level4= pygame.image.load('foto/scene/scene4.jpg')
level5 = pygame.image.load('foto/scene/scene5.png')

playr = pygame.image.load('foto/playr/playr-removebg-preview.png')

btn_play = pygame.image.load('foto/batton/image.png').convert_alpha()
btn_exit = pygame.image.load('foto/batton/imageQuti.png').convert_alpha()

def draw_animated_button(image, x, y, scale_hover=1.1, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_rect = image.get_rect(topleft=(x, y))

    if button_rect.collidepoint(mouse):
        w, h = image.get_size()
        new_size = (int(w * scale_hover), int(h * scale_hover))
        scaled_img = pygame.transform.smoothscale(image, new_size)
        new_rect = scaled_img.get_rect(center=button_rect.center)
        scr.blit(scaled_img, new_rect.topleft)

        if click[0] == 1 and action:
            pygame.time.delay(200)
            action()
    else:
        scr.blit(image, (x, y))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_right = pygame.transform.scale(playr, (40, 60))
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right
        self.rect = self.image.get_rect(topleft=(x, y))

        self.vel_y = 0
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT]:
            dx = -5
            self.image = self.image_left
        if keys[pygame.K_RIGHT]:
            dx = 5
            self.image = self.image_right


        if keys[pygame.K_x] and self.on_ground:
            self.vel_y = -15
            self.on_ground = False

        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy = self.vel_y


        self.rect.x += dx
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if dx > 0:
                    self.rect.right = platform.rect.left
                elif dx < 0:
                    self.rect.left = platform.rect.right

        self.rect.y += dy
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if dy > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif dy < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1250:
            self.rect.right = 1250
        if self.rect.top > 750:
            self.rect.topleft = (50, 500)
            self.vel_y = 0


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((56, 53, 53))  
        self.rect = self.image.get_rect(topleft=(x, y))


def main_menu():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1)

    running = True
    while running:
        scr.blit(background, (0, 0))

        draw_animated_button(btn_play, 500, 300, action=tutorial)
        draw_animated_button(btn_exit, 500, 430, action=quit_game)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()


def tutorial():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(tutor_music)
    pygame.mixer.music.play(-1)

    running = True
    while running:

        scr.blit(tutorpeople, (1240, 650))
        scr.blit(level1, (0, 0))
        scr.blit(text_tutor1, (0, 0))
        scr.blit(text_tutor2, (0, 50))
        scr.blit(text_tutor3, (0, 100))
        scr.blit(text_tutor4, (0, 150))        
        scr.blit(text_tutor5, (0, 200))                


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LCTRL:
                running = False
                scene1()


        pygame.display.update()



def scene1():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(scene1_music)
    pygame.mixer.music.play(-1)

    player = Player(50, 500)
    platforms = pygame.sprite.Group()
    platform_list = [
        Platform(0, 700, 1250, 50),
        Platform(200, 600, 150, 20),
        Platform(400, 500, 150, 20),
        Platform(650, 450, 150, 20),
        Platform(700, 450, 150, 20),
        Platform(100, 600, 10, 200),
        Platform(1000, 500, 10, 200),
    ]
    platforms.add(platform_list)

    goal = pygame.Rect(1150, 670, 80, 80)

    all_sprites = pygame.sprite.Group(player)
    running = True
    while running:
        scr.blit(level1, (0, 0))
        scr.blit(jorj, (250, 630))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.update(platform_list)
        all_sprites.draw(scr)
        platforms.draw(scr)

        pygame.draw.rect(scr, (102, 255, 0), goal)

        if player.rect.colliderect(goal):
            scene2()
            running = False

        pygame.display.update()
        pygame.time.Clock().tick(60)

def scene2():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(scene1_music)
    pygame.mixer.music.play(-1)

    player = Player(50, 500)
    platforms = pygame.sprite.Group()
    platform_list = [
        Platform(0, 700, 1250, 50),
        Platform(180, 540, 150, 20),
        Platform(300, 620, 200, 20),
        Platform(300, 440, 150, 20),
        Platform(500, 340, 150, 20),
        Platform(700, 500, 150, 20),
        Platform(830, 450, 150, 20),
        Platform(1050, 380, 150, 20),  
    ]
    platforms.add(platform_list)

    goal = pygame.Rect(1150, 300, 80, 80)

    all_sprites = pygame.sprite.Group(player)
    running = True
    while running:
        scr.blit(level3, (0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        player.update(platform_list)
        all_sprites.draw(scr)
        platforms.draw(scr)

        pygame.draw.rect(scr, (0, 255, 0), goal)  

        if player.rect.colliderect(goal):
            running = False
            scene3()

        pygame.display.update()
        pygame.time.Clock().tick(60)

def scene3():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(scene1_music)
    pygame.mixer.music.play(-1)

    player = Player(50, 500)
    platforms = pygame.sprite.Group()
    platform_list = [
        Platform(0, 700, 1250, 50),
        Platform(1050, 150, 150, 20),
        Platform(1100, 600, 120, 20),
        Platform(1000, 500, 120, 20),
        Platform(600, 400, 500, 20),
        Platform(400, 400, 120, 20),
        Platform(300, 300, 120, 20),
        Platform(400, 200, 120, 20),
        Platform(600, 200, 50, 20),
        Platform(740, 200, 50, 20),
        Platform(890, 200, 50, 20)

    ]
    platforms.add(platform_list)

    goal = pygame.Rect(1150, 50, 80, 80)

    all_sprites = pygame.sprite.Group(player)
    running = True
    while running:
        scr.blit(level4, (0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        player.update(platform_list)
        all_sprites.draw(scr)
        platforms.draw(scr)

        pygame.draw.rect(scr, (0, 255, 0), goal)  

        if player.rect.colliderect(goal):
            running = False
            scene4()

        pygame.display.update()
        pygame.time.Clock().tick(60)

def scene4():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(scene1_music)
    pygame.mixer.music.play(-1)

    player = Player(50, 500)
    platforms = pygame.sprite.Group()
    platform_list = [
        Platform(0, 650, 1250, 200)
    ]
    platforms.add(platform_list)

    goal = pygame.Rect(670, 550, 80, 80)

    all_sprites = pygame.sprite.Group(player)
    running = True
    while running:
        scr.blit(level5, (0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        player.update(platform_list)
        all_sprites.draw(scr)
        platforms.draw(scr)

        pygame.draw.rect(scr, (222, 184, 135), goal)  

        if player.rect.colliderect(goal):
            running = False

        pygame.display.update()
        pygame.time.Clock().tick(60)


def quit_game():
    pygame.quit()
    sys.exit()

main_menu()