from pygame import *
from time import sleep
from random import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 660:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > -10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 460:
            self.rect.y += self.speed
    def shoot(self):
        star = Attack_1(img_star, randint(50, 620), -40, 50, 50, 5)
        stars2.add(star)
    def shoot2(self):
        ball = Attack_2(img_ball, randint(50, 620), -40, 50, 50, 5)
        balls.add(ball)


class Attack_1(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 550:
            self.kill()
    
    
class Attack_2(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > randint(250, 450):
            self.kill()
            y_star = Star_1(img_star, self.rect.centerx, self.rect.top, 50, 50, 5)
            y_star2 = Star_2(img_star, self.rect.centerx, self.rect.top, 50, 50, 5)
            x_star = Star_3(img_star, self.rect.centerx, self.rect.top, 50, 50, 5)
            x_star2 = Star_4(img_star, self.rect.centerx, self.rect.top, 50, 50, 5)
            stars3.add(y_star)
            stars3.add(y_star2)
            stars3.add(x_star)
            stars3.add(x_star2)
  
class Attack_3(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 700:
            self.kill()
            


class Star_1(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 550:
            self.kill()

class Star_2(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -50:
            self.kill()

class Star_3(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 550:
            self.kill()
        
class Star_4(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -50:
            self.kill()
          
def starss(y):
    for i in range(5):
        star1 = Attack_3(img_star, -50, y, 50, 50, 5)
        stars.add(star1)
        y+=100

window = display.set_mode((700, 500))
clock = time.Clock()
FPS = 60
img_heart = 'heart.png'
img_star = 'star.png'
img_ball = 'ball.png'
display.set_caption('Undertale_game')
#image = transform.scale(image.load('rune.jpg'), (700, 500))
heart = Player(img_heart, 270, 400, 30, 40, 5)
balls = sprite.Group()
stars2 = sprite.Group()
stars = sprite.Group()
stars3 = sprite.Group()
game = True
y = 50
while game:
    #window.blit(image,(0, 0))
    window.fill((0,0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_1:
                heart.shoot()
            elif e.key == K_2:
                starss(y)
            elif e.key == K_3:
                heart.shoot2()
                balls.update()
                




    if sprite.spritecollide(heart, stars, False):
        game = False
    if sprite.spritecollide(heart, stars2, False):
        game = False
    if sprite.spritecollide(heart, stars3, False):
        game = False
    stars3.draw(window)
    stars3.update()
    stars2.draw(window)
    stars2.update()
    stars.draw(window)
    stars.update()
    balls.draw(window)
    balls.update()
    heart.reset()
    heart.update()
    display.update()
    clock.tick(FPS)