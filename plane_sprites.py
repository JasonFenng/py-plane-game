import random
import pygame
from constants import SCREEN_RECT


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_shadow=False):
        super().__init__('./images/background.png')
        if is_shadow:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.y


class Enemy(GameSprite):
    def __init__(self):
        super().__init__('./images/enemy1.png')
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
