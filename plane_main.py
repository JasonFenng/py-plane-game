import pygame
from plane_sprites import GameSprite, Background
from constants import *


class PlaneGame(object):

    def __init__(self):
        # create game window
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # create game clock
        self.clock = pygame.time.Clock()
        # create game sprites
        self.__create_sprites()
        # create enemy
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.background_group = pygame.sprite.Group(bg1, bg2)

    def start_game(self):
        print('start...')
        while True:
            # set fps
            self.clock.tick(FPS)
            # add event listener
            self.__event_handler()
            # update sprites
            self.__update_sprites()
            # update display
            pygame.display.update()

    @staticmethod
    def __event_handler():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print('enemy show...')

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.background_group.update()
        self.background_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print('game over')
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
