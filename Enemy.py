from Ship import Ship, pygame
from Bullet import Bullet

class Enemy(Ship):

    Enemy_Img = [pygame.image.load(f"image/enemy{i}.png") for i in range(2, 11)]
    

    def __init__(self, x, y, vel, index, heath=100):
        super().__init__(x, y, vel, heath)
        self.ship_img = self.Enemy_Img[index]
        self.bullet_img = pygame.image.load("image/enemy11.png")
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self):
        self.y += self.vel
    
    def shoot(self):
        if self.cool_down_counter == 0:
            bullet = Bullet(self.x + 20, self.y, self.bullet_img)
            self.bullets.append(bullet)
            self.cool_down_counter = 1
    
    


        