import pygame
# config.py

score_p1 = 0
score_p2 = 0
score_p3 = 0
score_p4 = 0



game_clock = pygame.time.Clock()
player_size = 60

# colours
Black = (100, 45, 15)
White = (255, 255, 255)
Red = (162, 8, 0)
Redd = (255, 87, 51)
Purple = (240, 152, 243)
Green = (0, 127, 33)
Yellow = (197, 199, 37)
Blue = (0, 0, 255)
angle_1 = 1
angle_2 = 1
angle_3 = 1
angle_4 = 1
# Bullet 1
bullet1appear = False
bullet1_y = 0
bullet1_x = 0
bullet1_dy = 7
bullet1_dx = 7
angle_1bullet = 0
bullet1_hit = 0
# Bullet 2
bullet2appear = False
bullet2_y = 0
bullet2_x = 0
bullet2_dy = 7
bullet2_dx = 7
angle_2bullet = 0
bullet2_hit = 0
# Bullet 3
bullet3appear = False
bullet3_y = 0
bullet3_x = 0
bullet3_dy = 7
bullet3_dx = 7
angle_3bullet = 0
bullet3_hit = 0
# Bullet 4
bullet4appear = False
bullet4_y = 0
bullet4_x = 0
bullet4_dy = 7
bullet4_dx = 7
angle_4bullet = 0
bullet4_hit = 0

#score
score_space = 70
# player 1 score
score_p1_font = pygame.font.SysFont('IMPACT', 50)
score_p1_text = score_p1_font.render('0', True, Green)
score_p1_text_rect = score_p1_text.get_rect()
score_p1_text_rect.center = (150, 30)

# player 2 score
score_p2_font = pygame.font.SysFont('IMPACT', 50)
score_p2_text = score_p2_font.render('0', True, Blue)
score_p2_text_rect = score_p2_text.get_rect()
score_p2_text_rect.center = (500, 30)

# player 3 xcore
score_p3_font = pygame.font.SysFont('IMPACT', 50)
score_p3_text = score_p3_font.render('0', True, Purple)
score_p3_text_rect = score_p3_text.get_rect()
score_p3_text_rect.center = (850, 30)

# player 4 score
score_p4_font = pygame.font.SysFont('IMPACT', 50)
score_p4_text = score_p4_font.render('0', True, Redd)
score_p4_text_rect = score_p4_text.get_rect()
score_p4_text_rect.center = (1150, 30)
