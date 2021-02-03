import pygame

from domain.Car import Car
from game.GameEngine import GameEngine


class GameInterface:
    def __init__(self, game_engine):
        pygame.init()
        self.FPS = 60
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.__game_engine = game_engine
        self.__all_sprites = self.__game_engine.get_all_sprites()



    def create_screen(self):
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('SpeedBumps')
        screen.fill(self.BLACK)
        self.__game_engine.lay_car(self.WIDTH // 2, self.HEIGHT // 2)
        # self.display_car(screen)
        pygame.display.update()
        return screen

    # def remove_car(self, screen, x, y):
    #     pygame.draw.rect(screen, self.BLACK, (x, y, *self.__game_engine.get_car_size()))
    #     pygame.display.update()

    # def display_car(self, screen):
    #     screen.fill(self.BLACK)
    #     pygame.draw.rect(screen, self.__game_engine.get_car_rect)
    #     pygame.display.update()

    def update_car(self, screen, reverse):
        # self.remove_car(screen, *self.__game_engine.get_car_pos())
        self.__game_engine.move_car(5, reverse)
        # self.display_car(screen, *self.__game_engine.get_car_pos())

    def change_car_direction(self, key):
        if key == 'left':
            self.__game_engine.change_car_direction(-30)
        else:
            self.__game_engine.change_car_direction(30)


    def move_car(self , x, y):
        self.__game_engine.move_car(x, y)

    def run_game(self):
        run = True
        clock = pygame.time.Clock()
        screen = self.create_screen()
        advance, reverse, change_direction = False, False, False
        while run:
            clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        advance = True
                    if event.key == pygame.K_r:
                        reverse = True
                    if event.key == pygame.K_LEFT:
                        change_direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        change_direction = 'right'

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        advance = False
                    if event.key == pygame.K_r:
                        reverse = False
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        change_direction = False


                if advance or reverse:
                    self.update_car(screen, reverse)
                if change_direction != False and not advance:
                    self.change_car_direction(change_direction)

                self.__all_sprites.update()

                screen.fill(self.BLACK)
                self.__all_sprites.draw(screen)
                pygame.display.flip()

        pygame.quit()

car = Car()
engine = GameEngine(car)
game = GameInterface(engine)
game.run_game()