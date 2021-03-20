from Ship import Ship, pygame

class Player(Ship):
    def __init__(self, x, y, vel, health=100):
        super().__init__(x, y, vel, health)
        self.ship_img = pygame.image.load("image/whiteship.png")
        self.bullet_img = pygame.image.load("image/laser1.png")
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
    def move_bullets(self, objs, height, vel):
        self.cooldown()
        for bullet in self.bullets[:]:
            bullet.move(vel)
            if bullet.off_screen(height):
                self.bullets.remove(bullet)
            else:
                for obj in objs[:]:
                    if bullet.collision(obj):
                        objs.remove(obj)
                        try:
                            self.bullets.remove(bullet)
                        except:
                            pass
    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health), 10))

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)
        
