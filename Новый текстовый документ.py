from pygame import *
from random import *

#init()
#mixer.init()

window = display.set_mode((1000, 500))
display.set_caption("Hell-Pong")
background = transform.scale(image.load("0.jpg"), (1000,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (25, 130))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 360:
            self.rect.y += self.speed

class Player_2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 360:
            self.rect.y += self.speed
'''
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.y, 15)
        bullets.add(bullet)
'''
class Ball(GameSprite):
    def __init__(self, spriteImage, spriteX, spriteY, spriteSpeed):
        super().__init__(spriteImage, spriteX, spriteY, spriteSpeed)
        self.image = transform.scale(image.load(spriteImage), (80, 80))
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 420:
            self.rect.y = -65
            self.rect.x = randint(0, 620)
            self.speed = randint(1, 2)
            global lost
            lost += 1
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
'''
mixer.music.load('space.ogg')
mixer.music.play()
shooting = mixer.Sound('fire.ogg')
RE = mixer.Sound('RE.ogg')
'''
players = sprite.Group()
 
player_1 = Player_1(('Player.jpg'), 10, 200, 15)
player_2 = Player_2(('Player.jpg'), 965, 200, 15)
players.add(player_1)
players.add(player_2)

balls = sprite.Group()
'''
meteors = sprite.Group()
'''
for i in range(1):
    ball = Ball(('Ball.png'), randint(0, 620), -65, randint(1, 2))
    balls.add(ball)
'''
for i in range(4):
    meteor = Meteor('asteroid.png', randint(0, 620), -65, randint(1, 2))
    meteors.add(meteor)

bullets = sprite.Group()

cooldown = 0
'''
game = True

finish = False
shells = 10
health = 5
ABOBA = False


while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
                
    if not finish:  
        window.blit(background, (0, 0))

        #bullets.update()
        #bullets.draw(window)
        players.update()
        players.draw(window)
        balls.update()
        balls.draw(window)
        #meteors.update()
        #meteors.draw(window)

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
'''