import pygame

class Ship:

    def __init__(self, x, y, vel, health=100):
        self.x = x
        self.y = y
        self.vel = vel
        self.health = health
        self.ship_img = None
        self.bullet_img = None
        self.bullets = []
        self.cool_down_counter = 0
    
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))