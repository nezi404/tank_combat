import pygame
import collision
from Background import screen_size
# Player info
player_1 = pygame.image.load("Images/Player1 - Sprite.png")
player_1_y = 200
player_1_x = 80
player_1_rect = player_1.get_rect()

player_2 = pygame.image.load("Images/Player2 - Sprite.png")
player_2_y = 200
player_2_x = screen_size[0] - 120
player_2_rect = player_2.get_rect()

player_3 = pygame.image.load("Images/Player3 - Sprite.png")
player_3_y = 650
player_3_x = screen_size[0] - 120
player_3_rect = player_3.get_rect()

player_4 = pygame.image.load("Images/Player4 - Sprite.png")
player_4_y = 650
player_4_x = 80
player_4_rect = player_4.get_rect() 
