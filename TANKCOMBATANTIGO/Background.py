import pygame
import config
import  tanks
import collision
pygame.init()
screenInf = pygame.display.Info()
screen_size = [screenInf.current_w, screenInf.current_h]
screen = pygame.display.set_mode(screen_size)


# Drawing the objects
if config.background_option == 1:
    # Drawing the objects
    drawGroup = pygame.sprite.Group()

    # Border walls
    border = pygame.sprite.Sprite(drawGroup)
    borderDetail1 = pygame.sprite.Sprite(drawGroup)
    borderDetail2 = pygame.sprite.Sprite(drawGroup)

    # Obstacles
    obsMidCorner1 = pygame.sprite.Sprite(drawGroup)
    obsMidCorner2 = pygame.sprite.Sprite(drawGroup)
    obsMidCorner3 = pygame.sprite.Sprite(drawGroup)
    obsMidCorner4 = pygame.sprite.Sprite(drawGroup)

    sideBarrier1 = pygame.sprite.Sprite(drawGroup)
    sideBarrier2 = pygame.sprite.Sprite(drawGroup)

    sideCube1 = pygame.sprite.Sprite(drawGroup)
    sideCube2 = pygame.sprite.Sprite(drawGroup)

    sideWallLeft1 = pygame.sprite.Sprite(drawGroup)
    sideWallLeft2 = pygame.sprite.Sprite(drawGroup)
    sideWallRight1 = pygame.sprite.Sprite(drawGroup)
    sideWallRight2 = pygame.sprite.Sprite(drawGroup)


    def draw_objects(obj, w, h, x_pos, y_pos, data, ang):
        obj.image = pygame.image.load(data)
        obj.image = pygame.transform.scale(obj.image, [w, h])
        obj.rect = pygame.Rect(x_pos, y_pos, w, h)
        obj.image = pygame.transform.rotate(obj.image, ang)


    def draw_background():
        # Drawing the border walls
        draw_objects(border, 1366, 720, 0, 60, "Images/Border.png", 0)
        draw_objects(borderDetail1, 50, 70, 683, 76, "Images/Obstacle_side_cube.png", 0)
        draw_objects(borderDetail2, 50, 70, 683, 692, "Images/Obstacle_side_cube.png", 0)

        # Drawing the obstacles
        draw_objects(obsMidCorner1, 100, 100, 520, 260, "Images/Obstacle_mid_corner.png", 180)
        draw_objects(obsMidCorner2, 100, 100, 800, 260, "Images/Obstacle_mid_corner_flip.png", 180)
        draw_objects(obsMidCorner3, 100, 100, 520, 480, "Images/Obstacle_mid_corner_flip.png", 0)
        draw_objects(obsMidCorner4, 100, 100, 800, 480, "Images/Obstacle_mid_corner.png", 0)

        # draw_objects(sideBarrier1, 100, 300, 150, 320, "Images/Obstacle_side_barrier.png", 0) originals
        # draw_objects(sideBarrier2, 100, 300, 1300, 320, "Images/Obstacle_side_barrier.png", 180)

        draw_objects(sideBarrier1, 100, 300, 100, screen_size[1] // 2 - 100, "Images/Obstacle_side_barrier.png", 0)
        draw_objects(sideBarrier2, 100, 300, 1170, screen_size[1] // 2 - 100, "Images/Obstacle_side_barrier.png", 180)

        draw_objects(sideCube1, 75, 75, 280, 384, "Images/Obstacle_side_cube.png", 0)
        draw_objects(sideCube2, 75, 75, 1000, 384, "Images/Obstacle_side_cube.png", 0)

        draw_objects(sideWallLeft1, 90, 40, 270, 180, "Images/Obstacle_side_cube.png", 0)
        draw_objects(sideWallRight1, 90, 40, 1000, 180, "Images/Obstacle_side_cube.png", 0)
        draw_objects(sideWallLeft2, 90, 40, 270, 620, "Images/Obstacle_side_cube.png", 0)
        draw_objects(sideWallRight2, 90, 40, 1000, 620, "Images/Obstacle_side_cube.png", 0)


if config.background_option == 2:
    drawGroup = pygame.sprite.Group()

    border = pygame.sprite.Sprite(drawGroup)
    borderDetail1 = pygame.sprite.Sprite(drawGroup)
    borderDetail2 = pygame.sprite.Sprite(drawGroup)


    sideBarrier1 = pygame.sprite.Sprite(drawGroup)
    sideBarrier2 = pygame.sprite.Sprite(drawGroup)


    def draw_objects(obj, w, h, x_pos, y_pos, data, ang):
        obj.image = pygame.image.load(data)
        obj.image = pygame.transform.scale(obj.image, [w, h])
        obj.rect = pygame.Rect(x_pos, y_pos, w, h)
        obj.image = pygame.transform.rotate(obj.image, ang)


    def draw_background():
        draw_objects(border, 1361, 710, 5, 60, "Images/Border.png", 0)
        draw_objects(borderDetail1, 50, 100, 655, 184, "Images/Obstacle_side_cube.png", 0)
        draw_objects(borderDetail2, 50, 100, 655, 550, "Images/Obstacle_side_cube.png", 0)

        draw_objects(sideBarrier1, 100, 300, 100, 320, "Images/Obstacle_side_barrier.png", 0)
        draw_objects(sideBarrier2, 100, 300, 1170, 320, "Images/Obstacle_side_barrier.png", 180)
