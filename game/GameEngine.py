import math

import pygame


class GameEngine:
    def __init__(self, car):
        self.__car = car
        self.__all_sprites = pygame.sprite.Group()
        self.__all_sprites.add(car)

    def get_all_sprites(self):
        return self.__all_sprites


    # def get_car_size(self):
    #     return (self.__car.width, self.__car.height)

    def lay_car(self, x, y):
        self.__car.center(x, y)

    def get_car_rect(self):
        return self.__car.rect

    def move_car(self, speed, reverse):
        '''
        update car position by canging it s coordonates based on the current direction
        imagine having a circle with the origin in ox, oy and with radius 1, on which will be represented the direction
        for more detail on the formula:
        https://math.stackexchange.com/questions/1384994/rotate-a-point-on-a-circle-with-known-radius-and-position
        :param speed:how far it should move (int)
        :return:-
        '''
        backwards = 0
        if reverse:
            backwards = 180
            speed = speed // 2

        ox, oy = self.__car.rect.centerx, self.__car.rect.centery
        dx = ox + math.cos(math.radians(self.__car.direction_angle + backwards))*speed
        dy = oy + math.sin(math.radians(self.__car.direction_angle + backwards))*speed
        self.lay_car(dx, dy)


    # def get_car_pos(self):
    #     return self.__car.pos

    def change_car_direction(self, n):
        '''
        will increase/decrease the slope angle based on what button is being pushed left/right
        :return:
        '''
        self.__car.modify_direction_angle(n)
        self.__car.modify_direction_image()