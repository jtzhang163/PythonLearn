import pygame
from plane_sprites import  *

class PlaneGame(object):
    '''Plane Game Main Class'''

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):

        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1,bg2)

        self.enemy_group = pygame.sprite.Group()

    def start_game(self):
        while True:
            self.clock.tick(FRAME_PRE_SEC)
            self.__event_handle()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("enery create ...")

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("game over ...")

        pygame.quit()
        exit()


if __name__ == '__main__':

    # create game object
    game = PlaneGame()

    # start game
    game.start_game()