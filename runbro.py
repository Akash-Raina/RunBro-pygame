import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("RunBro")

# Background
ground_surface = pygame.image.load("Graphics/ground.png").convert()
sky_surface = pygame.image.load("Graphics/Sky.png").convert()

# Title
title_font = pygame.font.Font("Font/Pixeltype.ttf", 65)
title_surface = title_font.render("RunBro", False, (64, 64, 64))
title_rect = title_surface.get_rect(center = (400, 80))

# Player_surface
player_surface = pygame.image.load("Graphics/Player/player_stand.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))

# Snail_surface 
snail_surface = pygame.image.load("Graphics/Snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

# Clock
clock = pygame.time.Clock()

while(True):

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            exit()

    # Background_surface
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))

    # Title_surface 
    pygame.draw.rect(screen,'#c0e8ec', title_rect)
    screen.blit(title_surface, title_rect)

    # Player_surface
    screen.blit(player_surface, player_rect)

    # Snail_surface
    screen.blit(snail_surface,snail_rect)

    pygame.display.update()
    clock.tick(60)
