import pygame
import os
import time
import random
from Player import Player
from Enemy import Enemy
from Bullet import collide

WIDTH, HEIGHT = 1400, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceInvaders made by XuanHung")
background = pygame.image.load("Background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

pygame.init()


def main():

    clock = pygame.time.Clock()
    fps = 30
    gameOver = False
    level = 0
    lives = 5
    font = pygame.font.SysFont("comicsans", 50)

    
    player = Player(WIDTH // 2, HEIGHT, 10)
    player.y = HEIGHT - player.get_width()

    enemies = []
    wave_length = 5    

    lost = False

    lost_count = 0

    while not gameOver:
        clock.tick(fps)

        WIN.blit(background, (0, 0))
        
        lives_label = font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = font.render(f"Level: {level}", 1, (255, 255, 255))
        WIN.blit(lives_label, (30, 30))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 30, 30))
        player.draw(WIN)
        if lost:
            lost_label = font.render("You Lost !!", 1, (255, 0, 0))
            WIN.blit(lost_label, (WIDTH // 2 - lost_label.get_width() // 2, HEIGHT // 2))
       
 
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > fps * 3:
                gameOver = True
            else:
                continue


        if len(enemies) == 0:
            level += 1
            wave_length += 5
            fps += 1
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), \
                    random.randrange(-1500*level/5, -100), 20 , random.randrange(0, 8))
                enemies.append(enemy)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                gameOver = True

        ## Move
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x >= 0:
            player.x -= player.vel
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x <= WIDTH - player.get_height():
            player.x += player.vel
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y >= 0:
            player.y -= player.vel
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y <= HEIGHT -  player.get_width():
            player.y += player.vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        
        for enemy in enemies[:]:
            enemy.draw(WIN)
            enemy.move()
            enemy.move_bullets(player, HEIGHT, 10)

            ## probability to shoot
            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
            
            
            
        player.move_bullets(enemies, HEIGHT, -16)

        pygame.display.flip()

def main_menu():
    font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(background, (0, 0))
        title_label = font.render("Press the mouse to begin .... ", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH // 2 - title_label.get_width() // 2, HEIGHT // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        pygame.display.flip()
    

if __name__ == "__main__":
    main_menu()