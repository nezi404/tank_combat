from math import *
import keyboard
import tanks
import pygame
import config
pygame.init()

border_x = 10
border_y = 60

def move_p1():
    keys = pygame.key.get_pressed()

    if keys:
        global player_1_y, player_1_x, angle_1, player_2_y, player_2_x, angle_2, bullet1appear, bullet2appear, bullet1_x, bullet1_y, bullet2_x, bullet2_y

        if keys[pygame.K_w]:
            moveFowardp1 = 1
        else:
            moveFowardp1 = 0
        if keys[pygame.K_UP]:
            moveFowardp2 = 1
        else:
            moveFowardp2 = 0
        if keys[pygame.K_t]:
            moveFowardp3 = 1
        else:
            moveFowardp3 = 0
        if keys[pygame.K_i]:
            moveFowardp4 = 1
        else:
            moveFowardp4 = 0

        # Green player movement
        if keys[pygame.K_d] and moveFowardp1 == 0:
            config.angle_1 += 5 * -1
        if keys[pygame.K_a] and moveFowardp1 == 0:
            config.angle_1 += 5
        if keys[pygame.K_w] and moveFowardp1 == 1:
            tanks.player_1_y -= 5 * cos(radians(config.angle_1))
            tanks.player_1_x -= 5 * sin(radians(config.angle_1))
        if keys[pygame.K_s] and config.bullet1appear == False:
            config.bullet1appear = True
            config.bullet1_y = tanks.player_1_y
            config.bullet1_x = tanks.player_1_x

        # Blue player movement
        if keys[pygame.K_RIGHT] and moveFowardp2 == 0:
            config.angle_2 += 5 * -1
        if keys[pygame.K_LEFT] and moveFowardp2 == 0:
            config.angle_2 += 5
        if keys[pygame.K_UP] and moveFowardp2 == 1:
            tanks.player_2_y -= 5 * cos(radians(config.angle_2))
            tanks.player_2_x -= 5 * sin(radians(config.angle_2))
        if keys[pygame.K_DOWN] and config.bullet2appear == False:
            config.bullet2_y = tanks.player_2_y
            config.bullet2_x = tanks.player_2_x
            config.bullet2appear = True

        # Purple player movement
        if keys[pygame.K_h] and moveFowardp3 == 0:
            config.angle_3 += 5 * -1
        if keys[pygame.K_f] and moveFowardp3 == 0:
            config.angle_3 += 5
        if keys[pygame.K_t] and moveFowardp3 == 1:
            tanks.player_3_y -= 5 * cos(radians(config.angle_3))
            tanks.player_3_x -= 5 * sin(radians(config.angle_3))
        if keys[pygame.K_g] and config.bullet3appear == False:
            config.bullet3_y = tanks.player_3_y
            config.bullet3_x = tanks.player_3_x
            config.bullet3appear = True

        # Red player movement
        if keys[pygame.K_l] and moveFowardp4 == 0:
            config.angle_4 += 5 * -1
        if keys[pygame.K_j] and moveFowardp4 == 0:
            config.angle_4 += 5
        if keys[pygame.K_i] and moveFowardp4 == 1:
            tanks.player_4_y -= 5 * cos(radians(config.angle_4))
            tanks.player_4_x -= 5 * sin(radians(config.angle_4))
        if keys[pygame.K_k] and config.bullet2appear == False:
            config.bullet4_y = tanks.player_4_y
            config.bullet4_x = tanks.player_4_x
            config.bullet4appear = True







run = True

while run:
    import Background
    Background.screen.fill(config.Black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # drawing objects
    Background.draw_background()

    center1 = 0
    center2 = 0

    # Angle that the green player's bullet must go
    if not config.bullet1appear:
        config.angle_1bullet = config.angle_1
    if config.bullet1appear:
        if config.bullet1_hit == 0:
            bullet1_dy = -7
            bullet1_dx = 7
        config.bullet1_y -= config.bullet1_dy * cos(radians(config.angle_1bullet)) * 3
        config.bullet1_x -= config.bullet1_dx * sin(radians(config.angle_1bullet)) * 3
        bullet1 = pygame.Rect(config.bullet1_x + 40, config.bullet1_y + 40, 6, 6)
        pygame.draw.rect(Background.screen, config.White, bullet1)

    # Angle that the blue player's bullet must go
    if not config.bullet2appear:
        config.angle_2bullet = config.angle_2
    # Green player's bullet's movement if it is triggered
    if config.bullet2appear:
        if config.bullet2_hit == 0:
            config.bullet2_dy = 7
            config.bullet2_dx = 7
        config.bullet2_y -= config.bullet2_dy * cos(radians(config.angle_2bullet)) * 3
        config.bullet2_x -= config.bullet2_dx * sin(radians(config.angle_2bullet)) * 3

        config.bullet2 = pygame.Rect(config.bullet2_x + 50, config.bullet2_y + 40, 6, 6)
        pygame.draw.rect(Background.screen, "red", config.bullet2)

    # Check how many times the "balls" bounced
    if config.bullet1_hit == 6:
        config.bullet1appear = False
        config.bullet1_hit = 0
    if config.bullet2_hit == 6:
        config.bullet2appear = False
        config.bullet2_hit = 0
    if config.bullet3_hit == 6:
        config.bullet3appear = False
        config.bullet3_hit = 0
    if config.bullet4_hit == 6:
        config.bullet4appear = False
        config.bullet4_hit = 0
    # Green tank bullet collision
    # With the blue tank
    if tanks.player_2_x + 80 >= config.bullet1_x >= tanks.player_2_x and tanks.player_2_y + 80 >= config.bullet1_y >= tanks.player_2_y or tanks.player_2_x - 80 >= config.bullet1_x >= tanks.player_2_x and tanks.player_2_y - 80 >= config.bullet1_y >= tanks.player_2_y:
        config.bullet1_hit = 0
        config.bullet1_x = tanks.player_1_x
        config.bullet1_y = tanks.player_1_x
        config.bullet1appear = False
        config.score_p1 += 1
        player2_damaged = pygame.Rect(tanks.player_2_x, tanks.player_2_y, 120, 120)
        pygame.draw.rect(Background.screen, config.Red, player2_damaged)
        config.score_p1_text = config.score_p1_font.render(f'{config.score_p1}', True, config.Green)

    # with the purple tank
    if tanks.player_3_x + 80 >= config.bullet1_x >= tanks.player_3_x and tanks.player_3_y + 80 >= config.bullet1_y >= tanks.player_3_y or tanks.player_3_x - 80 >= config.bullet1_x >= tanks.player_3_x and tanks.player_2_y - 80 >= config.bullet1_y >= tanks.player_2_y:
        config.bullet1_hit = 0
        config.bullet1_x = tanks.player_1_x
        config.bullet1_y = tanks.player_1_x
        config.bullet1appear = False
        config.score_p1 += 1
        player3_damaged = pygame.Rect(tanks.player_3_x, tanks.player_3_y, 120, 120)
        pygame.draw.rect(Background.screen, config.Red, player3_damaged)
        config.score_p1_text = config.score_p1_font.render(f'{config.score_p1}', True, config.Green)
    # with the red player
    if tanks.player_4_x + 80 >= config.bullet1_x >= tanks.player_4_x and tanks.player_4_y + 80 >= config.bullet1_y >= tanks.player_4_y or tanks.player_4_x - 80 >= config.bullet1_x >= tanks.player_4_x and tanks.player_4_y - 80 >= config.bullet1_y >= tanks.player_4_y:
        config.bullet1_hit = 0
        config.bullet1_x = tanks.player_1_x
        config.bullet1_y = tanks.player_1_x
        config.bullet1appear = False
        config.score_p1 += 1
        player4_damaged = pygame.Rect(tanks.player_4_x, tanks.player_4_y, 120, 120)
        pygame.draw.rect(Background.screen, config.Red, player4_damaged)
        config.score_p1_text = config.score_p1_font.render(f'{config.score_p1}', True, config.Green)

    # Blue tank bullet collision
    # with the green tank
    if tanks.player_1_x + 80 >= config.bullet2_x >= tanks.player_1_x and tanks.player_1_y + 80 >= config.bullet2_y >= tanks.player_1_y or tanks.player_1_x - 80 >= config.bullet2_x >= tanks.player_1_x and tanks.player_1_y - 80 >= config.bullet2_y >= tanks.player_1_y:
        config.bullet2_hit = 0
        config.bullet2_x = tanks.player_2_x
        config.bullet2_y = tanks.player_2_y
        config.bullet2appear = False
        config.score_p2 += 1
        player1_damaged = pygame.Rect(tanks.player_1_x, tanks.player_1_y, 120, 120)
        pygame.draw.rect(Background.screen, config.Red, player1_damaged)
        config.score_p2_text = config.score_p1_font.render(f'{config.score_p2}', True, config.Blue)
        # with the purple tank
    if tanks.player_3_x + 80 >= config.bullet2_x >= tanks.player_3_x and tanks.player_3_y + 80 >= config.bullet2_y >= tanks.player_3_y or tanks.player_3_x - 80 >= config.bullet2_x >= tanks.player_3_x and tanks.player_2_y - 80 >= config.bullet2_y >= tanks.player_2_y:
        config.bullet1_hit = 0
        config.bullet2_x = tanks.player_2_x
        config.bullet2_y = tanks.player_2_x
        config.bullet2appear = False
        config.score_p2 += 1
        player3_damaged = pygame.Rect(tanks.player_3_x, tanks.player_3_y, 120, 120)
        pygame.draw.rect(Background.screen, config.Red, player3_damaged)
        config.score_p2_text = config.score_p2_font.render(f'{config.score_p2}', True, config.Blue)
    # with the red player
    if tanks.player_4_x + 80 >= config.bullet2_x >= tanks.player_4_x and tanks.player_4_y + 80 >= config.bullet2_y >= tanks.player_4_y or tanks.player_4_x - 80 >= config.bullet2_x >= tanks.player_4_x and tanks.player_4_y - 80 >= config.bullet2_y >= tanks.player_4_y:
        config.bullet2_hit = 0
        config.bullet2_x = tanks.player_2_x
        config.bullet2_y = tanks.player_2_x
        config.bullet2appear = False
        config.score_p2 += 1
        player4_damaged = pygame.Rect(tanks.player_4_x, tanks.player_4_y, 120, 120)
        pygame.draw.rect(Background.screen, config.Red, player4_damaged)
        config.score_p2_text = config.score_p2_font.render(f'{config.score_p2}', True, config.Blue)

    # Purple tank bullet collision
    # with the green tank
    if tanks.player_1_x + 80 >= config.bullet3_x >= tanks.player_1_x and tanks.player_1_y + 80 >= config.bullet3_y >= tanks.player_1_y or tanks.player_1_x - 80 >= config.bullet3_x >= tanks.player_1_x and tanks.player_1_y - 80 >= config.bullet3_y >= tanks.player_1_y:
        config.bullet3_hit = 0
        config.bullet3_x = tanks.player_3_x
        config.bullet3_y = tanks.player_3_y
        config.bullet3appear = False
        config.score_p3 += 1
        player1_damaged = pygame.Rect(tanks.player_1_x, tanks.player_1_y, 120, 120)
        pygame.draw.rect(Background.screen, config.Red, player1_damaged)
        config.score_p3_text = config.score_p3_font.render(f'{config.score_p3}', True, config.Purple)

    # With the blue tank********parei agui
    if tanks.player_2_x + 80 >= config.bullet1_x >= tanks.player_2_x and tanks.player_2_y + 80 >= config.bullet1_y >= tanks.player_2_y or tanks.player_2_x - 80 >= config.bullet1_x >= tanks.player_2_x and tanks.player_2_y - 80 >= config.bullet1_y >= tanks.player_2_y:
        config.bullet1_hit = 0
        config.bullet1_x = tanks.player_1_x
        config.bullet1_y = tanks.player_1_x
        config.bullet1appear = False
        config.score_p1 += 1
        player2_damaged = pygame.Rect(tanks.player_2_x, tanks.player_2_y, 120, 120)
        pygame.draw.rect(Background.screen, config.Red, player2_damaged)
        config.score_p1_text = config.score_p1_font.render(f'{config.score_p1}', True, config.Green)

    if config.bullet1appear:
        if config.bullet1_hit == 0:
            bullet1_dy = 7
            bullet1_dx = 7
        config.bullet1_y -= config.bullet1_dy * cos(radians(config.angle_1bullet)) * 3
        config.bullet1_x -= config.bullet1_dx * sin(radians(config.angle_1bullet)) * 3
        bullet1 = pygame.Rect(config.bullet1_x + 40, config.bullet1_y + 40, 6, 6)
        pygame.draw.rect(Background.screen, config.White, bullet1)


    #####
    # Angle that the purple player's bullet must go
    if not config.bullet3appear:
        config.angle_3bullet = config.angle_3
    # Green player's bullet's movement if it is triggered
    if config.bullet3appear:
        if config.bullet3_hit == 0:
            config.bullet3_dy = 7
            config.bullet2_dx = 7
        config.bullet3_y -= config.bullet3_dy * cos(radians(config.angle_3bullet)) * 3
        config.bullet3_x -= config.bullet3_dx * sin(radians(config.angle_2bullet)) * 3

        config.bullet3 = pygame.Rect(config.bullet3_x + 50, config.bullet3_y + 40, 6, 6)
        pygame.draw.rect(Background.screen, "red", config.bullet3)

    if not config.bullet4appear:
        config.angle_4bullet = config.angle_4
    # Green player's bullet's movement if it is triggered
    if config.bullet4appear:
        if config.bullet4_hit == 0:
            config.bullet4_dy = 7
            config.bullet4_dx = 7
        config.bullet4_y -= config.bullet4_dy * cos(radians(config.angle_4bullet)) * 3
        config.bullet4_x -= config.bullet4_dx * sin(radians(config.angle_4bullet)) * 3

        config.bullet4 = pygame.Rect(config.bullet4_x + 50, config.bullet4_y + 40, 6, 6)
        pygame.draw.rect(Background.screen, config.Red , config.bullet4)


    # PLAYER 3 bullet collision score
    if tanks.player_2_x + 80 >= config.bullet1_x >= tanks.player_2_x and tanks.player_2_y + 80 >= config.bullet1_y >= tanks.player_2_y or tanks.player_2_x - 80 >= config.bullet1_x >= tanks.player_2_x and tanks.player_2_y - 80 >= config.bullet1_y >= tanks.player_2_y:
        config.bullet3_hit = 0
        config.bullet3_x = tanks.player_3_x
        config.bullet3_y = tanks.player_3_x
        config.bullet3appear = False
        config.score_p3 += 1
        player3_damaged = pygame.Rect(tanks.player_3_x, tanks.player_3_y, 120, 120)
        pygame.draw.rect(Background.screen, config.Red, player3_damaged)
        config.score_p3_text = config.score_p3_font.render(f'{config.score_p3}', True, config.Purple)
    # PLAYER 4 bullet collision score
    if tanks.player_1_x + 80 >= config.bullet2_x >= tanks.player_1_x and tanks.player_1_y + 80 >= config.bullet2_y >= tanks.player_1_y or tanks.player_1_x - 80 >= config.bullet2_x >= tanks.player_1_x and tanks.player_1_y - 80 >= config.bullet2_y >= tanks.player_1_y:
        config.bullet4_hit = 0
        config.bullet4_x = tanks.player_4_x
        config.bullet4_y = tanks.player_4_y
        config.bullet4appear = False
        config.score_p4 += 1
        player4_damaged = pygame.Rect(tanks.player_4_x, tanks.player_4_y, 120, 120)
        pygame.draw.rect(Background.screen, config.Red, player4_damaged)
        config.score_p4_text = config.score_p4_font.render(f'{config.score_p4}', True, config.Redd)

    import collision

    #**************nao retorna
    tanks.player_1_x, tanks.player_1_y = collision.detect_collision_player(tanks.player_1_x, tanks.player_1_y)
    tanks.player_2_x, tanks.player_2_y = collision.detect_collision_player(tanks.player_2_x, tanks.player_2_y)
    tanks.player_3_x, tanks.player_3_y = collision.detect_collision_player(tanks.player_3_x, tanks.player_3_y)
    tanks.player_4_x, tanks.player_4_y = collision.detect_collision_player(tanks.player_4_x, tanks.player_4_y)

    config.bullet1_x, config.bullet1_y = collision.detect_collision_ball1(config.bullet1_x, config.bullet1_y)

    collision.limit_borders_up(tanks.player_1_y, config.score_space + 5, tanks.player_2_y, config.score_space + 5)
    collision.limit_borders_down(tanks.player_1_y, 670, tanks.player_2_y, 670)
    collision.limit_borders_left(tanks.player_1_x, 25, tanks.player_2_x, 25)
    collision.limit_borders_right(tanks.player_1_x, 1260, tanks.player_2_x, 1260)
    collision.limit_borders_up2(tanks.player_3_y, config.score_space + 5, tanks.player_4_y, config.score_space + 5)
    collision.limit_borders_down2(tanks.player_3_y, 670, tanks.player_4_y, 670)
    collision.limit_borders_left2(tanks.player_3_x, 25, tanks.player_4_x, 25)
    collision.limit_borders_right2(tanks.player_3_x, 1260, tanks.player_4_x, 1260)

    move_p1()

    config.bullet1_x, config.bullet1_y = collision.detect_collision_ball1(config.bullet1_x, config.bullet1_y)

    collision.limit_borders_upbullet2(config.bullet1_y, config.score_space + 5, config.bullet2_y, config.score_space + 5)
    collision.limit_borders_downbullet2(config.bullet1_y, 670, config.bullet2_y, 670)
    collision.limit_borders_leftbullet2(config.bullet1_x, 25, config.bullet2_x, 25)
    collision.limit_borders_rightbullet2(config.bullet1_x, 1260, config.bullet2_x, 1260)

    collision.limit_borders_upbullet(config.bullet3_y, config.score_space + 5, config.bullet4_y, config.score_space + 5)
    collision.limit_borders_downbullet(config.bullet3_y, 670, config.bullet4_y, 670)
    collision.limit_borders_leftbullet(config.bullet3_x, 25, config.bullet4_x, 25)
    collision.limit_borders_rightbullet(config.bullet3_x, 1260, config.bullet4_x, 1260)

    # show elements on screen
    surf = pygame.transform.rotate(tanks.player_1, config.angle_1)
    surf2 = pygame.transform.rotate(tanks.player_2, config.angle_2)
    surf3 = pygame.transform.rotate(tanks.player_3, config.angle_3)
    surf4 = pygame.transform.rotate(tanks.player_4, config.angle_4)
    Background.screen.blit(surf, (tanks.player_1_x, tanks.player_1_y))
    Background.screen.blit(surf2, (tanks.player_2_x, tanks.player_2_y))
    Background.screen.blit(surf3, (tanks.player_3_x, tanks.player_3_y))
    Background.screen.blit(surf4, (tanks.player_4_x, tanks.player_4_y))
    Background.screen.blit(config.score_p1_text, config.score_p1_text_rect)
    Background.screen.blit(config.score_p2_text, config.score_p2_text_rect)
    Background.screen.blit(config.score_p3_text, config.score_p3_text_rect)
    Background.screen.blit(config.score_p4_text, config.score_p4_text_rect)

    collision.detect_collision_player(tanks.player_1_x, tanks.player_1_y)
    collision.detect_collision_player(tanks.player_2_x, tanks.player_2_y)
    collision.detect_collision_player(tanks.player_3_x, tanks.player_3_y)
    collision.detect_collision_player(tanks.player_4_x, tanks.player_4_y)
    config.game_clock.tick(60)
    Background.drawGroup.draw(Background.screen)
    pygame.display.update()