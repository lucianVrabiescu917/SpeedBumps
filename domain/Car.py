import pygame


class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((35, 35))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()

        # self._width = width
        # self._height = height
        # self._pos = None
        self.direction_angle = 0 #0 -> 360 will represent the angle

    # @property
    # def height(self):
    #     return self._height
    #
    # @property
    # def width(self):
    #     return self._width
    # @property
    # def rect(self):
    #     return self.rect

    # @property
    # def direction_angle(self):
    #     return self.direction_angle

    # @property
    # def pos(self):
    #     return self._pos
    #
    # @pos.setter
    # def pos(self, pos):
    #     self._pos = pos

    def modify_direction_angle(self, n):
        self.direction_angle += n

    def center(self, x, y):
        self.rect.center = (x, y)

