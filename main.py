import pygame
import os
import time
import random
from ship import Ship

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceInvaders made by XuanHung")
background = pygame.image.load("Background.jpg")

PLAYER_IMG = pygame.image.load("image/whiteship.png")
ENEMY_IMG = pygame.image.load("image/enemy8.png")


pygame.init()

def draw_text(font_render: pygame.font.Font.render, position: tuple):
    WIN.blit(font_render, position)

if __name__ == "__main__":
    clock = pygame.time.Clock()
    fps = 30
    gameOver = False
    level = 1
    lives = 5
    font = pygame.font.SysFont("comicsans", 50)

    lives_label = font.render(f"Lives: {lives}", 1, (255, 255, 255))
    level_label = font.render(f"Level: {level}", 1, (255, 255, 255))
    
    player = Ship(WIDTH // 2, HEIGHT - PLAYER_IMG.get_width(), 10)
    player.ship_img = PLAYER_IMG


    while not gameOver:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
        WIN.blit(background, (0, 0))
        WIN.blit(lives_label, (30, 30))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 30, 30))
        player.draw(WIN)

        ## Move
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x >= 0:
            player.x -= player.vel
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x <= WIDTH - PLAYER_IMG.get_width():
            player.x += player.vel
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y >= 0:
            player.y -= player.vel
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y <= HEIGHT -  PLAYER_IMG.get_height():
            player.y += player.vel
        

        pygame.display.flip()