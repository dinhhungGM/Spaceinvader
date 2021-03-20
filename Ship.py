from Bullet import *

class Ship:

    COOLDOWN = 30

    def __init__(self, x, y, vel, health=100):
        self.x = x
        self.y = y
        self.vel = vel
        self.health = health
        self.ship_img = None
        self.bullet_img = None
        self.bullets = []
        self.cool_down_counter = 0
    
    def shoot(self):
        if self.cool_down_counter == 0:
            bullet = Bullet(self.x + 10, self.y, self.bullet_img)
            self.bullets.append(bullet)
            self.cool_down_counter = 1
    
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(window)

    def move_bullets(self, obj, height, vel):
        self.cooldown()
        for bullet in self.bullets[:]:
            bullet.move(vel)
            if bullet.off_screen(height):
                self.bullets.remove(bullet)
            elif bullet.collision(obj):
                obj.health -= 10
                self.bullets.remove(bullet)

    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()