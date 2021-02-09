import math
import random

import pygame

from domain.Troll import Troll


class GameEngine:
    def __init__(self, car):
        self.__car = car
        self.__trolls = []
        self.__dead_trolls_count = 5
        self.__all_sprites = pygame.sprite.Group()
        self.__all_sprites.add(car)

    def get_all_sprites(self):
        return self.__all_sprites

    def get_dead_trolls(self):
        return self.__dead_trolls_count

    def spawn_trolls(self):
        for i in range(self.__dead_trolls_count):
            troll = Troll()
            random_x, random_y = random.randint(5, 1195), random.randint(5, 795)
            troll.center(random_x, random_y)
            self.__trolls.append(troll)
            self.__all_sprites.add(troll)
            self.__dead_trolls_count -= 1


    def lay_car(self, x, y):
        '''
        set new center for car obj
        :param x:
        :param y:
        :return:
        '''
        self.__car.center(x, y)

    def lay_troll(self, x, y, nb):
        self.__trolls[nb].center(x, y)

    def get_car_rect(self):
        return self.__car.rect

    def move_troll(self, speed, nb):
        self.__trolls[nb].change_direction_times()
        ox, oy = self.__trolls[nb].rect.centerx, self.__trolls[nb].rect.centery
        dx = ox + math.cos(math.radians(self.__trolls[nb].direction_angle)) * speed
        dy = oy + math.sin(math.radians(self.__trolls[nb].direction_angle)) * speed
        # might change these with the distance between center and border
        # if dx > 171 and dx < 1030 and dy > 20 and dy < 780:
        self.lay_troll(dx, dy, nb)

    def move_car(self, speed, reverse):
        '''
        update car position by canging it s coordonates based on the current direction
        imagine having a circle with the origin in ox, oy and with radius 1, on which will be represented the direction
        for more detail on the formula:
        https://math.stackexchange.com/questions/1384994/rotate-a-point-on-a-circle-with-known-radius-and-position
        :param speed:how far it should move (int)
        :return:-
        '''
        #move in the opp dir if backwards is 180
        backwards = 0
        if reverse:
            backwards = 180
            speed = speed // 2

        ox, oy = self.__car.rect.centerx, self.__car.rect.centery
        dx = ox + math.cos(math.radians(self.__car.direction_angle + backwards))*speed
        dy = oy + math.sin(math.radians(self.__car.direction_angle + backwards))*speed
        #might change these with the distance between center and border
        if dx > 171 and dx < 1030 and dy > 20 and dy < 780:
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

    # def check_car_on_road(self, speed):
    #     if self.__car.rect.centerx