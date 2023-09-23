from pygame import *
from random import *

#init()
mixer.init()

window = display.set_mode((1000, 500))
display.set_caption("Hell-Pong")
background = transform.scale(image.load("0.jpg"), (1000,500))

lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (25, 180))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 310:
            self.rect.y += self.speed

class Player_2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 310:
            self.rect.y += self.speed
'''
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.y, 15)
        bullets.add(bullet)
'''
class Ball(sprite.Sprite):
    def __init__(self, sprite_image, spriteX, spriteY, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = spriteX
        self.rect.y = spriteY
        self.speed = sprite_speed
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed
        '''
        if self.rect.y >= 420:
            self.rect.y = -65
            self.rect.x = randint(0, 620)
            self.speed = randint(1, 2)
            global lost
            lost += 1
            '''
'''
class Bullet(GameSprite):
    def __init__(self, spriteImage, spriteX, spriteY, spriteSpeed):
        super().__init__(spriteImage, spriteX, spriteY, spriteSpeed)
        self.image = transform.scale(image.load(spriteImage), (4, 8))
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= -10:
            self.kill()

class Meteor(GameSprite):
    def __init__(self, spriteImage, spriteX, spriteY, spriteSpeed):
        super().__init__(spriteImage, spriteX, spriteY, spriteSpeed)
        self.image = transform.scale(image.load(spriteImage), (65, 65))
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = -65
            self.rect.x = randint(0, 620)
            self.speed = randint(1, 2)

kills = 0

fontResult = font.SysFont('Arial', 120)

lost = 0
fontTxt = font.SysFont('Sans', 30)
'''
clock = time.Clock()
FPS = 60

mixer.music.load('In the Hall of the Mountain King_Edvard Grieg.mp3')
mixer.music.play()

Pong = mixer.Sound('pong.ogg')

players = sprite.Group()
 
player_1 = Player_1(('Player.jpg'), 10, 200, 20)
player_2 = Player_2(('Player.jpg'), 965, 200, 20)
players.add(player_1)
players.add(player_2)

balls = sprite.Group()
'''
meteors = sprite.Group()
'''
for i in range(1):
    ball = Ball(('Ball.png'), 410, 300, 0)
    balls.add(ball)
'''
for i in range(4):
    meteor = Meteor('asteroid.png', randint(0, 620), 250, randint(1, 2))
    meteors.add(meteor)

bullets = sprite.Group()

cooldown = 0
'''
game = True

finish = False
shells = 10
health = 5
ABOBA = False

ball_speed_x = 25
ball_speed_y = 25


while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y
    
    if ball.rect.colliderect(player_1.rect) or ball.rect.colliderect(player_2.rect):
        ball_speed_y *= 1
        ball_speed_x *= -1
        Pong.play()
    
    if ball.rect.x < 10:
        ball_speed_x *= -1
    if ball.rect.x > 920:
        ball_speed_x *= -1
    if ball.rect.y < 10:
        ball_speed_y *= -1
    if ball.rect.y > 420:
        ball_speed_y *= -1
    
    if not finish:  
        window.blit(background, (0, 0))

        players.update()
        players.draw(window)
        balls.update()
        balls.draw(window)

        clock.tick(FPS)
        display.update()


'''
#pip list
#pip install pyinstaller

colliders = sprite.groupcollide(monsters, bullets, True, True)

        for c in colliders:
            kills += 1
            UFO = Enemy(('ufo.png'), randint(0, 620), -65, randint(1, 2))
            monsters.add(UFO)

        colliders28 = sprite.groupcollide(players, monsters, ABOBA, True)

        for UFO in colliders28:
            kills += 1
            UFO = Enemy(('ufo.png'), randint(0, 620), -65, randint(1, 2))
            monsters.add(UFO)
            health -= 1

        collidersMeteor = sprite.groupcollide(players, meteors, ABOBA, True)
        for c in collidersMeteor:
            health -= 1
            meteor = Meteor('asteroid.png', randint(0, 620), -65, randint(1, 2))
            meteors.add(meteor)

elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if not finish:
                    if shells > 0:
                        player.fire()
                        shells -= 1
                        shooting.play()


if health == 1:
            ABOBA = True
        if health == 0:
            finish = True
            mixer.music.stop()
            window.blit(fontResult.render('Смерть', True, (128, 0, 0)), (160, 170))

        if lost >= 10:
            finish = True
            mixer.music.stop()
            window.blit(fontResult.render('Смерть', True, (128, 0, 0)), (160, 170))

        if kills >= 10:
            finish = True
            mixer.music.stop()
            window.blit(fontResult.render('Триумф', True, (0, 128, 128)), (160, 170))

        if cooldown == 1:
            RE.play()

        if cooldown < 140 and shells <= 0:
            cooldown += 1
            window.blit(fontTxt.render('Перезарядка...', True, (255,255,255)), (280, 350))
        if shells <= 0 and cooldown >= 140:
            shells = 10
            cooldown = 0

        window.blit(fontTxt.render('Пропущено: '+str(lost), True, (255,255,255)), (10, 0))
        window.blit(fontTxt.render('Повержено: '+str(kills), True, (255,255,255)), (10, 40))
        window.blit(fontTxt.render('Снаряды: '+str(shells), True, (255,255,255)), (10, 80))
        window.blit(fontTxt.render('Здоровье: '+str(health), True, (128, 0, 0)), (550, 0))





import pygame
import random
pygame.init()

WHAT1 = (102, 205, 170)
WHAT = (200, 100, 100)
BACK = (220,220,220)
WHITE = (500, 500, 500)
CARD_COLOR = (47, 79, 79)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BlUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BlUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)


window = pygame.display.set_mode((500, 500))
window.fill(BACK)


class TextArea():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def change_color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, frame_width):
        pygame.draw.rect(window, frame_color, self.rect, frame_width)

class Label(TextArea):
    def set_text(self, text, font_size, text_color):
        self.image = pygame.font.SysFont("verdana", font_size).render(text, True, text_color)

    def draw(self, shift_x, shift_y):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

class Picture(TextArea):
    def __init__(self, filename, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.image = pygame.image.load(filename)

    def draw(self):
        self.fill()
        window.blit(self.image, (self.rect.x, self.rect.y))


platform = Picture("platform.png", 200, 350, 100, 30, BACK)
ball = Picture("ball.png", 225, 250, 50, 50, BACK)


monters = list()
start_x = 5
start_y = 5
count = 9


clock = pygame.time.Clock()


for i in range(3):
    x = start_x + i*27.5
    y = start_y + 55*i
    for i in range(count):
        monster = Picture("enemy.png", x, y, 50, 50, BACK)
        monters.append(monster)
        x += 55
    count -= 1

ball_speed_x = 10
ball_speed_y = 10
platform_speed = 15
move_left = False
move_right = False

while True:
    ball.fill()
    platform.fill()

    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y
    if ball.rect.colliderect(platform.rect):
        ball_speed_y *= -1
    if ball.rect.x < 0:
        ball_speed_x *= -1
    if ball.rect.x > 450:
        ball_speed_x *= -1
    if ball.rect.y < 0:
        ball_speed_y *= -1
    if ball.rect.y > 330:
        ball_speed_y *= -1

    if move_left and platform.rect.x >= 5:
        platform.rect.x -= platform_speed

    if move_right and platform.rect.x <= 395:
        platform.rect.x += platform_speed       

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
        
    for m in monters:
        if m.rect.colliderect(ball.rect):
            monters.remove(m)
            m.fill()
            ball_speed_y *= -1
        else:
            m.draw()

    ball.draw()
    platform.draw()
    clock.tick(40)
    pygame.display.update()

    if ball.rect.y > 320:
        f1 = pygame.font.Font(None, 80)
        text1 = f1.render('Вы Проиграли!', 1, RED)
        window.blit(text1, (85, 180))
        break
        pygame.display.update()
    
    if len(monters) == 0:
        f2 = pygame.font.Font(None, 80)
        text2 = f2.render('Успех!', 1, GREEN)
        window.blit(text2, (85, 180))
        break

pygame.display.update()
'''