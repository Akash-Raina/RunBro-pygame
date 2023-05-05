import pygame
from sys import exit
from random import randint

def displaytime(): 
    current = pygame.time.get_ticks() - start_time
    title_surface = title_font.render(f'Score : {int(current/1000)}', False, (64, 64, 64))
    title_rect = title_surface.get_rect(center = (400, 80))
    screen.blit(title_surface, title_rect)
    return current

def enemy_movement(enemy_list):
    if enemy_list:
        for enemy in enemy_list:
            enemy.x -= 5
            if enemy.bottom == 300: screen.blit(snail_surface, enemy)
            else: screen.blit(fly_surface, enemy)

        enemy_list = [eneemy for eneemy in enemy_list if eneemy.x > -100]
        return enemy_list
    else : return []

def collisions(player_pos, collision_list):

    if enemy_list:
        for collision in collision_list:
            if player_pos.colliderect(collision): return False
    return True


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("RunBro")
game_active = False
start_time = 0
score = 0
# Background
ground_surface = pygame.image.load("Graphics/ground.png").convert()
sky_surface = pygame.image.load("Graphics/Sky.png").convert()

# Title
title_font = pygame.font.Font("Font/Pixeltype.ttf", 65)
#title_surface = title_font.render("RunBro", False, (64, 64, 64))
#title_rect = title_surface.get_rect(center = (400, 80))

# Player_surface
player_surface = pygame.image.load("Graphics/Player/player_stand.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))
player_gravity = 0

# Enemy_surface 
snail_surface = pygame.image.load("Graphics/Snail/snail1.png").convert_alpha()  
fly_surface = pygame.image.load("Graphics/Fly/Fly1.png").convert_alpha()
enemy_list = []

# Timer
event_timer = pygame.USEREVENT + 1
pygame.time.set_timer(event_timer, 1500)

# Intro Screen
player_stand = pygame.image.load("Graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# Intro Font
intro_font_surface = title_font.render("RunBro", False, (64, 64, 64))
intro_font_rect = intro_font_surface.get_rect(center = (400, 90))

# Click Command Font
click_surface = title_font.render("Press 'SPACE' to start the game ", False, (64, 64, 64))
click_rect = click_surface.get_rect(center = (420, 330))

# Clock
clock = pygame.time.Clock()

while(True): 

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:

            if event.type == event_timer:
                if randint(0,2): enemy_list.append(snail_surface.get_rect(midbottom = (randint(900, 1100), 300)))
                else: enemy_list.append(fly_surface.get_rect(midbottom = (randint(900, 1100), 210)))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom >= 300:
                        player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        # Background_surface
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))

        # Title_surface 
        # pygame.draw.rect(screen,'#c0e8ec', title_rect)
        #screen.blit(title_surface, title_rect)
        score = int(displaytime()/1000)

        # Player_surface
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # Enemy Movement
        enemy_list = enemy_movement(enemy_list)

        # Collision
        game_active = collisions(player_rect, enemy_list)
         
    
    else:

        # Restart
        enemy_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0
        
        # Bg-color
        screen.fill((94, 129, 162))

        # Player Scaled Image
        screen.blit(player_stand, player_stand_rect)

        # Score
        text_score_surface = title_font.render(f"Score : {score}", False, (64,64,64))
        text_score_rect = text_score_surface.get_rect(center = (400, 330))
        
        # Title
        screen.blit(intro_font_surface, intro_font_rect)

        # Click command
        if score != 0:screen.blit(text_score_surface, text_score_rect)
        else:screen.blit(click_surface, click_rect)
    
    pygame.display.update()
    clock.tick(60)   
