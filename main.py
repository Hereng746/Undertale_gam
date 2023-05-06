from pygame import *
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
        if keys[K_LEFT] and self.rect.x > -20:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > -20:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed


window = display.set_mode((700, 500))
clock = time.Clock()
FPS = 60
img_heart = 'frisk.png'
display.set_caption('Undertale_game')
image = transform.scale(image.load('rune.jpg'), (700, 500))
heart = Player(img_heart, 270, 400, 100, 100, 10)
game = True
while game:
    window.blit(image, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    heart.reset()
    display.update()
    clock.tick(FPS)