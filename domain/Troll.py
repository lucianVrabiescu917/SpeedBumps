import random
import time

import pygame


class Troll(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.direction_angle = 0  # 0 -> 360 will represent the angle
        self.image_dict = \
        {
         0:r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_0.png',
         30: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_0.png',
         60: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_0.png',
         90: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_90.png',
         120: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_0.png',
         150: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_0.png',
         180: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_180.png',
         210: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_0.png',
         240: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_0.png',
         270: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_270.png',
         300: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_0.png',
         330: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_0.png',
         360: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\troll_images\troll_0.png',

        }

        self.image = pygame.Surface((25, 25))
        self.image = pygame.image.load(self.image_dict[self.direction_angle])

        self.rect = self.image.get_rect()

        #start time of the troll movement
        self.elapsing_time_start = 0
        #for how long should the troll move in that direction before changing it
        self.elapsing_time = 0

    def modify_direction_image(self):
        self.image = pygame.image.load(self.image_dict[self.direction_angle])

    def modify_direction_angle(self, n):
        n += self.direction_angle
        if n < 0:
            n = 360 - abs(n)
        elif n >= 360:
            n = n - 360
        self.direction_angle = n

    def center(self, x, y):
        self.rect.center = (x, y)

    def near_border(self):
        # if self.rect.centerx >= 1150 or self.rect.centerx <= 55 or self.rect.centery <= 50 or self.rect.centery >= 790:
        #     return 270
        if self.rect.centerx >= 1175:
            return 180
        elif self.rect.centerx <= 45:
            return 30
        elif self.rect.centery <= 25:
            return 90
        elif self.rect.centery >= 775:
            return 270
        return False


    def change_direction_times(self):
        if int(time.time()) - self.elapsing_time_start >= self.elapsing_time or self.near_border():
            if self.near_border():
                self.direction_angle = self.near_border()
            else:
                self.modify_direction_angle(random.choice([i*30 for i in range(12)]))
            self.modify_direction_image()
            self.elapsing_time_start = int(time.time())
            self.elapsing_time = random.randint(2, 3)







