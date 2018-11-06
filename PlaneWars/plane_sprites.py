import pygame

SCREEN_RECT = pygame.Rect(0,0,480,700)

FRAME_PRE_SEC = 60

CREATE_ENEMY_EVENT = pygame.USEREVENT

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
