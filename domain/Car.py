import pygame


class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.direction_angle = 0  # 0 -> 360 will represent the angle
        self.image_dict =\
        {0:r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_0.png',
         30: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_330.png',
         60: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_300.png',#this
         90: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_270.png',
         120: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_240.png',
         150: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_210.png',#this
         180: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_180.png',
         210: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_150.png',#this
         240: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_120.png',
         270: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_90.png',
         300: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_60.png',
         330: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_30.png',
         360: r'C:\Users\Latitude\Documents\GitHub\SpeedBumps\domain\car_images2\car_0.png',
         }

        self.image = pygame.Surface((35, 35))
        self.image = pygame.image.load(self.image_dict[self.direction_angle])
        # self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()


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



