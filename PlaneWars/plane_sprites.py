import random
import pygame

SCREEN_RECT = pygame.Rect(0,0,480,700)

FRAME_PRE_SEC = 60

CREATE_ENEMY_EVENT = pygame.USEREVENT

HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """plane war sprite"""

    def __init__(self, image_name, speed = 1):

        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        self.rect.y += self.speed

class Background(GameSprite):
    '''game background sprite'''

    def __init__(self, is_alt = False):

        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = - self.rect.height

    def update(self):

        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

class Enemy(GameSprite):
    '''enemy sprite'''

    def __init__(self):

        super().__init__("./images/enemy1.png")

        self.rect.bottom = self.rect.bottom - self.rect.height

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

        self.speed = random.randint(1,3)

    def update(self):

        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):

        # print("enemy is out %s" % self.rect)
        
        pass

class Hero(GameSprite):
    '''hero sprite'''

    def __init__(self):

        super().__init__("./images/me1.png", 0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        self.bullets = pygame.sprite.Group()


    def update(self):

        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):

        for i in (0,1,2):

            buttet = Bullet()

            buttet.rect.bottom = self.rect.y - 20 * i
            buttet.rect.centerx = self.rect.centerx

            self.bullets.add(buttet)


class Bullet(GameSprite):
    '''bullet sprite'''

    def __init__(self):

        super().__init__("./images/bullet1.png", -2)

    def update(self):

        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):

        print("bullet is killed..")
