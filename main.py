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

class Attack_1(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 570:
            self.kill()
    
def star():
    for i in range(20):
        star = Attack_1(img_star, randint(50, 620), -50, 50, 50, 5)
        stars.add(star)
    
    
          


window = display.set_mode((700, 500))
clock = time.Clock()
FPS = 60
img_heart = 'heart.png'
img_star = 'star.png'
display.set_caption('Undertale_game')
#image = transform.scale(image.load('rune.jpg'), (700, 500))
heart = Player(img_heart, 270, 400, 40, 50, 5)
stars = sprite.Group()
game = True

while game:
    #window.blit(image,(0, 0))
    window.fill((0,0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                star()    
    stars.draw(window)
    heart.reset()
    heart.update()
    stars.update()
    display.update()
    clock.tick(FPS)