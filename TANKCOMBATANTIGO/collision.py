import config
import tanks

if config.background_option == 1:

    def detect_collision_player(player_x, player_y):

        # Side Wall Left Collision
        if 160 <= player_y <= 165 and 679 <= player_x <= 780:
            player_y = 165
        if player_y < 160 and 665 <= player_x <= 675:
            player_x = 665
        if player_y < 160 and 785 <= player_x <= 790:
            player_x = 790

        # Bottom Border Square
        if 670 <= player_y and 670 <= player_x <= 780:
            player_y = 660

        if 670 < player_y and 675 >= player_x >= 665:
            player_x = 665
        if 670 < player_y and 790 >= player_x >= 785:
            player_x = 790

        # Top Left Curve

        # Collision in the top
        if 170 <= player_y <= 199 and 440 <= player_x <= 570:
            player_y = 170

        # Collision in the left
        if 200 <= player_y <= 325 and 425 <= player_x <= 439:
            player_x = 425

        # Collision in the bottom 1
        if 330 <= player_y <= 350 and 440 <= player_x <= 510:
            player_y = 350

        # Collision in the bottom 2
        if 290 <= player_y < 310 and 510 <= player_x <= 580:
            player_y = 310

        # Collision in the right 1
        if 185 <= player_y < 280 and 570 <= player_x <= 610:
            player_x = 610

        # Collision in the right 2
        if 325 >= player_y >= 290 and 540 >= player_x >= 500:
            player_x = 540

        # Top Right Curve

        # Collision in the top
        if 200 >= player_y >= 160 and 880 >= player_x >= 750:
            player_y = 160

        # Collision in the right
        if 315 > player_y >= 200 and 890 >= player_x >= 870:
            player_x = 890

        # Collision in the left 1
        if 315 - 50 >= player_y > 200 and 900 - 155 >= player_x >= 870 - 155:
            player_x = 870 - 155

        # Collision in the left 2
        if 325 >= player_y > 265 and 800 >= player_x >= 770:
            player_x = 770

        # Collision in the bottom 1
        if 295 >= player_y > 265 and 800 >= player_x >= 740:
            player_y = 295

        # Collision in the bottom 2
        if 340 >= player_y > 325 and 880 >= player_x >= 790:
            player_y = 340

        # Bottom Left Corner
        if 485 >= player_y > 480 and 590 >= player_x >= 490:
            player_y = 480
        if 635 >= player_y > 480 and 500 >= player_x >= 485:
            player_x = 485 - 100
        if 635 >= player_y >= 630 and 640 >= player_x >= 500:
            player_y = 635

        if 635 >= player_y > 530 and 650 >= player_x >= 640:
            player_x = 650 - 100

        if 535 >= player_y >= 530 and 640 >= player_x >= 500:
            player_y = 530
        if 635 >= player_y > 480 and 600 >= player_x >= 590:
            player_x = 600

        # Bottom Right Corner
        if 485 >= player_y > 480 and 950 >= player_x >= 880:
            player_y = 480
        if 635 >= player_y > 480 and 970 >= player_x >= 965:
            player_x = 970
        if 635 >= player_y >= 630 and 950 >= player_x >= 810:
            player_y = 635
        if 635 >= player_y > 480 and 885 >= player_x >= 880:
            player_x = 880
        if 635 >= player_y > 530 and 815 >= player_x >= 810:
            player_x = 810
        if 525 >= player_y >= 520 and 950 >= player_x >= 810:
            player_y = 520

        # Mid-Left Square  ***

        # Collision in the left
        if 440 >= player_y >= 340 and 265 >= player_x >= 200:
            player_x = 200

        # Collision in the right
        if 440 >= player_y >= 340 and 355 >= player_x >= 340:
            player_x = 355

        # Collision in the top
        if 300 >= player_y >= 295 and 325 >= player_x >= 225:
            player_y = 295

        # Collision in the bot
        if 465 >= player_y >= 460 and 325 >= player_x >= 225:
            player_y = 465

        # Mid-Right Square
        if 485 >= player_y >= 355 and 1025 <= player_x <= 1030:
            player_x = 1025
        if 485 >= player_y >= 355 and 1155 <= player_x <= 1160:
            player_x = 1160
        if 350 >= player_y >= 345 and 1160 >= player_x >= 1025:
            player_y = 345
        if 490 >= player_y >= 485 and 1160 >= player_x >= 1025:
            player_y = 490
        # Top Wall Left
        if 205 >= player_y >= 110 and 180 <= player_x <= 185:
            player_x = 180
        if 205 >= player_y >= 200 and 180 <= player_x <= 330:
            player_y = 205
        if 205 >= player_y >= 110 and 325 <= player_x <= 330:
            player_x = 330
        if 105 >= player_y >= 100 and 180 <= player_x <= 330:
            player_y = 100

        # Top Wall Right
        if 205 >= player_y >= 110 and 1095 <= player_x <= 1105:
            player_x = 1095
        if 205 >= player_y >= 200 and 1095 <= player_x <= 1250:
            player_y = 205
        if 205 >= player_y >= 110 and 1230 <= player_x <= 1250:
            player_x = 1250
        if 105 >= player_y >= 100 and 1095 <= player_x <= 1250:
            player_y = 100

        # Bottom-Left Wall
        if 735 >= player_y >= 655 and 190 <= player_x <= 200:
            player_x = 190
        if 740 >= player_y >= 735 and 190 <= player_x <= 330:
            player_y = 740
        if 735 >= player_y >= 655 and 340 <= player_x <= 345:
            player_x = 345
        if 640 >= player_y >= 635 and 190 <= player_x <= 330:
            player_y = 635

        # Bottom-Right Wall
        if 735 >= player_y >= 655 and 1095 <= player_x <= 1105:
            player_x = 1095
        if 740 >= player_y >= 735 and 1095 <= player_x <= 1250:
            player_y = 740
        if 735 >= player_y >= 655 and 1230 <= player_x <= 1250:
            player_x = 1250
        if 640 >= player_y >= 635 and 1095 <= player_x <= 1250:
            player_y = 635

        # Left Barrier  ***

        # Collision in barrier inside
        if 250 <= player_y <= 480 and 85 <= player_x <= 90:
            player_x = 80

        # Collision in barrier outside
        if 240 <= player_y <= 570 and 165 <= player_x <= 185:
            player_x = 185

        # Collision in corner top left
        if 240 <= player_y <= 270 and 15 <= player_x <= 70:
            player_x = 15

        # Collision in corner bot left
        if 500 <= player_y <= 590 and 20 <= player_x <= 30:
            player_x = 20

        # Collision in corner top outside
        if 200 <= player_y <= 245 and 30 <= player_x <= 155:
            player_y = 200

        # Collision in corner top inside
        if 320 <= player_y <= 335 and 30 <= player_x <= 155:
            player_y = 335

        # Collision in corner bot outside
        if 585 <= player_y <= 595 and 30 <= player_x <= 155:
            player_y = 595
        if 495 <= player_y <= 500 and 25 <= player_x <= 155:
            player_y = 495

        # Right Barrier
        if 250 <= player_y <= 590 and 1070 <= player_x <= 1075:
            player_x = 1070
        if 250 <= player_y <= 590 and 1180 <= player_x <= 1185:
            player_x = 1185
        if 250 <= player_y <= 340 and 1235 <= player_x <= 1260:
            player_x = 1260
        if 500 <= player_y <= 590 and 1235 <= player_x <= 1260:
            player_x = 1260
        if 235 <= player_y <= 240 and 1115 <= player_x <= 1230:
            player_y = 235
        if 595 <= player_y <= 610 and 1115 <= player_x <= 1260:
            player_y = 610
        if 340 <= player_y <= 345 and 1115 <= player_x <= 1260:
            player_y = 345
        if 495 <= player_y <= 500 and 1115 <= player_x <= 1260:
            player_y = 495

        return player_x, player_y
def detect_collision_ball1(ball_x, ball_y):
    import KOMBATTANK

    # Top Border Square
    if 160 >= ball_y and 780 >= ball_x >= 670:
        bounce1y()
    if ball_y < 160 and 710 >= ball_x >= 700:
        bounce1x()
    if ball_y < 160 and 790 >= ball_x >= 785:
        bounce1x()

    # Bottom Border Square
    if ball_y >= 680 and 780 >= ball_x >= 670:
        bounce1y()
    if 670 < ball_y and 710 >= ball_x >= 700:
        bounce1x()
    if 670 < ball_y and 790 >= ball_x >= 785:
        bounce1x()

    # Top Left Curve
    if ball_y >= 180 and 640 >= ball_x >= 500:
        bounce1y()
    if 315 >= ball_y > 160 and ball_x >= 520:
        bounce1x()
    if 315 >= ball_y > 300 and 590 >= ball_x >= 500:
        bounce1y()
    if 270 >= ball_y > 260 and 650 >= ball_x >= 500:
        bounce1y()
    if 315 >= ball_y > 160 and 600 >= ball_x >= 590:
        bounce1x()
    if 250 >= ball_y > 160 and 650 >= ball_x >= 640:
        bounce1x()

    # Top right Curve
    if 165 >= ball_y >= 160 and 950 >= ball_x >= 810:
        bounce1y()
    if 250 >= ball_y > 160 and 815 >= ball_x >= 810:
        bounce1x()
    if 315 >= ball_y > 300 and 950 >= ball_x >= 885:
        bounce1y()
    if 270 >= ball_y > 260 and 950 >= ball_x >= 810:
        bounce1y()
    if 315 >= ball_y > 160 and 970 >= ball_x >= 960:
        bounce1x()
    if 315 >= ball_y > 160 and 900 >= ball_x >= 870:
        bounce1x()

    # Bottom Left Corner
    if 485 >= ball_y > 480 and 590 >= ball_x >= 490:
        bounce1y()
    if 635 >= ball_y > 480 and 500 >= ball_x >= 485:
        bounce1x()
    if 635 >= ball_y >= 630 and 640 >= ball_x >= 500:
        bounce1y()
    if 635 >= ball_y > 530 and 650 >= ball_x >= 640:
        bounce1x()
    if 535 >= ball_y >= 530 and 640 >= ball_x >= 500:
        bounce1y()
    if 635 >= ball_y > 480 and 600 >= ball_x >= 590:
        bounce1x()

    # Bottom Right Corner
    if 485 >= ball_y > 480 and 950 >= ball_x >= 880:
        bounce1y()
    if 635 >= ball_y > 480 and 970 >= ball_x >= 965:
        bounce1x()
    if 635 >= ball_y >= 630 and 950 >= ball_x >= 810:
        bounce1y()
    if 635 >= ball_y > 480 and 885 >= ball_x >= 880:
        bounce1x()
    if 635 >= ball_y > 530 and 815 >= ball_x >= 810:
        bounce1x()
    if 525 >= ball_y >= 520 and 950 >= ball_x >= 810:
        bounce1y()

    # Mid-Left Square
    if 485 >= ball_y >= 355 and 305 >= ball_x >= 300:
        bounce1x()
    if 485 >= ball_y >= 355 and 425 >= ball_x >= 420:
        bounce1x()
    if 350 >= ball_y >= 345 and 425 >= ball_x >= 300:
        bounce1y()
    if 490 >= ball_y >= 485 and 425 >= ball_x >= 300:
        bounce1y()

    # Mid-Right Square
    if 485 >= ball_y >= 355 and 1025 <= ball_x <= 1030:
        bounce1x()
    if 485 >= ball_y >= 355 and 1155 <= ball_x <= 1160:
        bounce1x()
    if 350 >= ball_y >= 345 and 1160 >= ball_x >= 1025:
        bounce1y()
    if 490 >= ball_y >= 485 and 1160 >= ball_x >= 1025:
        bounce1y()

    # Top Wall Left
    if 205 >= ball_y >= 110 and 180 <= ball_x <= 185:
        bounce1x()
    if 205 >= ball_y >= 200 and 180 <= ball_x <= 330:
        bounce1y()
    if 205 >= ball_y >= 110 and 325 <= ball_x <= 330:
        bounce1x()
    if 105 >= ball_y >= 100 and 180 <= ball_x <= 330:
        bounce1y()

    # Top Wall Right
    if 205 >= ball_y >= 110 and 1095 <= ball_x <= 1105:
        bounce1x()
    if 205 >= ball_y >= 200 and 1095 <= ball_x <= 1250:
        bounce1y()
    if 205 >= ball_y >= 110 and 1230 <= ball_x <= 1250:
        bounce1x()
    if 105 >= ball_y >= 100 and 1095 <= ball_x <= 1250:
        bounce1y()

    # Bottom-Left Wall
    if 735 >= ball_y >= 655 and 190 <= ball_x <= 200:
        bounce1x()
    if 740 >= ball_y >= 735 and 190 <= ball_x <= 330:
        bounce1y()
    if 735 >= ball_y >= 655 and 340 <= ball_x <= 345:
        bounce1x()
    if 640 >= ball_y >= 635 and 190 <= ball_x <= 330:
        bounce1y()

    # Bottom-Right Wall
    if 735 >= ball_y >= 655 and 1095 <= ball_x <= 1105:
        bounce1x()
    if 740 >= ball_y >= 735 and 1095 <= ball_x <= 1250:
        bounce1y()
    if 735 >= ball_y >= 655 and 1230 <= ball_x <= 1250:
        bounce1x()
    if 640 >= ball_y >= 635 and 1095 <= ball_x <= 1250:
        bounce1y()

    # Left Barrier
    if 250 <= ball_y <= 590 and 130 <= ball_x <= 135:
        bounce1x()
    if 250 <= ball_y <= 590 and 220 <= ball_x <= 225:
        bounce1x()
    if 250 <= ball_y <= 340 and 70 <= ball_x <= 75:
        bounce1x()
    if 500 <= ball_y <= 590 and 70 <= ball_x <= 75:
        bounce1x()
    if 240 <= ball_y <= 245 and 85 <= ball_x <= 210:
        bounce1y()
    if 310 <= ball_y <= 345 and 85 <= ball_x <= 210:
        bounce1y()
    if 595 <= ball_y <= 605 and 85 <= ball_x <= 210:
        bounce1y()
    if 495 <= ball_y <= 500 and 85 <= ball_x <= 210:
        bounce1y()

    # Right Barrier
    if 250 <= ball_y <= 590 and 1215 <= ball_x <= 1220:
        bounce1x()
    if 250 <= ball_y <= 590 and 1320 <= ball_x <= 1325:
        bounce1x()
    if 250 <= ball_y <= 340 and 1385 <= ball_x <= 1390:
        bounce1x()
    if 500 <= ball_y <= 590 and 1385 <= ball_x <= 1390:
        bounce1x()
    if 235 <= ball_y <= 240 and 1215 <= ball_x <= 1390:
        bounce1y()
    if 595 <= ball_y <= 600 and 1215 <= ball_x <= 1390:
        bounce1y()
    if 340 <= ball_y <= 345 and 1215 <= ball_x <= 1390:
        bounce1y()
    if 495 <= ball_y <= 500 and 1215 <= ball_x <= 1390:
        bounce1y()

    return ball_x, ball_y




if config.background_option == 2:
    def detect_collision_player(player_x, player_y):

        # Left Barrier
        if 250 <= player_y <= 590 and 85 <= player_x <= 90:
            player_x = 80
        if 250 <= player_y <= 590 and 160 <= player_x <= 175:
            player_x = 175
        if 250 <= player_y <= 340 and 25 <= player_x <= 30:
            player_x = 25
        if 500 <= player_y <= 590 and 25 <= player_x <= 30:
            player_x = 25
        if 240 <= player_y <= 245 and 25 <= player_x <= 155:
            player_y = 240
        if 310 <= player_y <= 345 and 25 <= player_x <= 155:
            player_y = 345
        if 595 <= player_y <= 605 and 25 <= player_x <= 155:
            player_y = 605
        if 495 <= player_y <= 500 and 25 <= player_x <= 155:
            player_y = 495

        # Right Barrier
        if 250 <= player_y <= 590 and 1070 <= player_x <= 1075:
            player_x = 1070
        if 250 <= player_y <= 590 and 1180 <= player_x <= 1185:
            player_x = 1185
        if 250 <= player_y <= 340 and 1235 <= player_x <= 1260:
            player_x = 1260
        if 500 <= player_y <= 590 and 1235 <= player_x <= 1260:
            player_x = 1260
        if 235 <= player_y <= 240 and 1115 <= player_x <= 1230:
            player_y = 235
        if 595 <= player_y <= 610 and 1115 <= player_x <= 1260:
            player_y = 610
        if 340 <= player_y <= 345 and 1115 <= player_x <= 1260:
            player_y = 345
        if 495 <= player_y <= 500 and 1115 <= player_x <= 1260:
            player_y = 495

        # Upper rectangle
        if 184 - config.player_size <= player_y <= 234 and 655 - config.player_size <= player_x <= 670 :
            player_x = 655 - config.player_size
        if 184 - config.player_size <= player_y <= 234 and 705 <= player_x <= 655 + config.player_size :
            player_x = 705 + config.player_size
        if 184 - config.player_size <= player_y <= 190 and 655 - config.player_size <= player_x <= 705:
            player_y =180 - config.player_size
        if  274<= player_y <=284 + config.background_option  and 655 - config.player_size <= player_x <=705 :
            player_y =284

        # Bottom rectangle

        if 550 - config.player_size <= player_y <= 650 and 655 - config.player_size <= player_x <= 670 :
            player_x = 655 - config.player_size
        if 550 - config.player_size <= player_y <= 650 and 705 <= player_x <= 655 + config.player_size :
            player_x = 705 + config.player_size
        if 550 - config.player_size <= player_y <= 556 and 655 - config.player_size <= player_x <= 705:
            player_y =550 - config.player_size
        if 550 <= player_y <=650 + config.background_option  and 655 - config.player_size <= player_x <=705 :
            player_y =650
        return player_x, player_y


    def detect_collision_ball1(ball_x, ball_y):
        import KOMBATTANK
         # Left Barrier
        if 250 <= ball_y <= 590 and 85 <= ball_x <= 90:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 250 <= ball_y <= 590 and 160 <= ball_x <= 175:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 250 <= ball_y <= 340 and 25 <= ball_x <= 30:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 500 <= ball_y <= 590 and 25 <= ball_x <= 30:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 240 <= ball_y <= 245 and 25 <= ball_x <= 160:
            if ball_y == config.bullet1_y:
                bounce1y()
            elif ball_y == config.bullet2_y:
                bounce2y()
            elif ball_y == config.bullet3_y:
                bounce3y()
            else:
                bounce4y()
        if 310 <= ball_y <= 345 and 25 <= ball_x <= 155:
            if ball_y == config.bullet1_y:
                bounce1y()
            elif ball_y == config.bullet2_y:
                bounce2y()
            elif ball_y == config.bullet3_y:
                bounce3y()
            else:
                bounce4y()
        if 595 <= ball_y <= 605 and 25 <= ball_x <= 155:
            if ball_y == config.bullet1_y:
                bounce1y()
            elif ball_y == config.bullet2_y:
                bounce2y()
            elif ball_y == config.bullet3_y:
                bounce3y()
            else:
                bounce4y()
        if 495 <= ball_y <= 500 and 25 <= ball_x <= 155:
            if ball_y == config.bullet1_y:
                bounce1y()
            elif ball_y == config.bullet2_y:
                bounce2y()
            elif ball_y == config.bullet3_y:
                bounce3y()
            else:
                bounce4y()

        # Right Barrier
        if 250 <= ball_y <= 590 and 1215 <= ball_x <= 1220:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 250 <= ball_y <= 590 and 1320 <= ball_x <= 1325:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 250 <= ball_y <= 340 and 1385 <= ball_x <= 1390:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 500 <= ball_y <= 590 and 1375 <= ball_x <= 1390:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 235 <= ball_y <= 240 and 1200 <= ball_x <= 1390:
            if ball_y == config.bullet1_y:
                bounce1y()
            elif ball_y == config.bullet2_y:
                bounce2y()
            elif ball_y == config.bullet3_y:
                bounce3y()
            else:
                bounce4y()
        if 595 <= ball_y <= 600 and 1215 <= ball_x <= 1390:
            bounce1y()
        if 340 <= ball_y <= 345 and 1215 <= ball_x <= 1390:
            if ball_y == config.bullet1_y:
                bounce1y()
            elif ball_y == config.bullet2_y:
                bounce2y()
            elif ball_y == config.bullet3_y:
                bounce3y()
            else:
                bounce4y()
        if 495 <= ball_y <= 500 and 1215 <= ball_x <= 1390:
            if ball_y == config.bullet1_y:
                bounce1y()
            elif ball_y == config.bullet2_y:
                bounce2y()
            elif ball_y == config.bullet3_y:
                bounce3y()
            else:
                bounce4y()

        # Upper rectangle
        if 184 <= ball_y <= 234 and 655 - config.player_size <= ball_x <= 670:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 184 - config.player_size <= ball_y <= 234 and 705 <= ball_x <= 655 + config.player_size:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 184 - config.player_size <= ball_y <= 190 and 655 - config.player_size <= ball_x <= 705:
            if ball_y == config.bullet1_y:
                bounce1y()
            elif ball_y == config.bullet2_y:
                bounce2y()
            elif ball_y == config.bullet3_y:
                bounce3y()
            else:
                bounce4y()
        if 274 <= ball_y <= 284 + config.background_option and 655 - config.player_size <= ball_x <= 705:
            if ball_y == config.bullet1_y:
                bounce1y()
            elif ball_y == config.bullet2_y:
                bounce2y()
            elif ball_y == config.bullet3_y:
                bounce3y()
            else:
                bounce4y()

        # Bottom rectangle

        if 550 <= ball_y <= 650 and 655 <= ball_x <= 670:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 550 <= ball_y <= 650 and 705 <= ball_x <= 655:
            if ball_y == config.bullet1_y:
                bounce1x()
            elif ball_y == config.bullet2_y:
                bounce2x()
            elif ball_y == config.bullet3_y:
                bounce3x()
            else:
                bounce4x()
        if 550 <= ball_y <= 556 and 655 <= ball_x <= 705:
            if ball_y == config.bullet1_y:
                bounce1y()
            elif ball_y == config.bullet2_y:
                bounce2y()
            elif ball_y == config.bullet3_y:
                bounce3y()
            else:
                bounce4y()
        if 550 <= ball_y <= 650 and 655 <= ball_x <= 705:
            if ball_y == config.bullet1_y:
                bounce1y()
            elif ball_y == config.bullet2_y:
                bounce2y()
            elif ball_y == config.bullet3_y:
                bounce3y()
            else:
                bounce4y()
        return ball_x, ball_y


# makes sure the player won't go through the border
def limit_borders_up(player1, walls, player2, walls2):
    global player_1_y, player_2_y
    if player1 <= walls:
        tanks.player_1_y = walls  ## it requires tanks.
    if player2 <= walls2:
        tanks.player_2_y = walls2
    return  tanks.player_2_y, tanks.player_1_y  # it requires return tanks.coor to make effect

def limit_borders_down(player1, walls, player2, wall2):
    global player_1_y, player_2_y
    if player1 >= walls:
        tanks.player_1_y = walls
    if player2 >= wall2:
        tanks.player_2_y = wall2
    return tanks.player_1_y, tanks.player_2_y


def limit_borders_left(player1, walls, player2, wall2):
    global player_1_x, player_2_x
    if player1 <= walls:
        tanks.player_1_x = walls
    if player2 <= wall2:
        tanks.player_2_x = wall2
        return tanks.player_1_x, tanks.player_2_x


def limit_borders_right(player1, wall, player2, wall2):
    global player_1_x, player_2_x
    if player1 >= wall:
        tanks.player_1_x = wall
    if player2 >= wall2:
        tanks.player_2_x = wall2

        return tanks.player_1_x, tanks.player_2_x

def limit_borders_up2(player1, walls, player2, walls2):
    global player_3_y, player_4_y
    if player1 <= walls:
        tanks.player_3_y = walls  ## it requires .tanks.
    if player2 <= walls2:
        tanks.player_4_y = walls2
    return  tanks.player_3_y, tanks.player_4_y  # it requires return tanks.coor to make effect

def limit_borders_down2(player1, walls, player2, wall2):
    global player_3_y, player_4_y
    if player1 >= walls:
        tanks.player_3_y = walls
    if player2 >= wall2:
        tanks.player_4_y = wall2
    return tanks.player_3_y, tanks.player_4_y


def limit_borders_left2(player1, walls, player2, wall2):
    global player_3_x, player_4_x
    if player1 <= walls:
        tanks.player_3_x = walls
    if player2 <= wall2:
        tanks.player_4_x = wall2
        return tanks.player_3_x, tanks.player_4_x


def limit_borders_right2(player1, wall, player2, wall2):
    global player_3_x, player_4_x
    if player1 >= wall:
        tanks.player_3_x = wall
    if player2 >= wall2:
        tanks.player_4_x = wall2

        return tanks.player_3_x, tanks.player_4_x


def bounce1y():
    import config
    global bullet1_dx, bullet1_dy, bullet1_hit
    config.bullet1_dy *= -1
    config.bullet1_dx *= 1
    config.bullet1_hit += 1
    return config.bullet1_hit



def bounce1x():
    import config
    global bullet1_dx, bullet1_dy, bullet1_hit
    config.bullet1_dy *= 1
    config.bullet1_dx *= -1
    config.bullet1_hit += 1
    return config.bullet1_hit



def bounce2y():
    import config
    global bullet2_dx, bullet2_dy, bullet2_hit
    config.bullet2_dy *= -1
    config.bullet2_dx *= 1
    config.bullet2_hit += 1
    return config.bullet2_hit


def bounce2x():
    import config
    global bullet2_dx, bullet2_dy, bullet2_hit
    config.bullet2_dy *= 1
    config.bullet2_dx *= -1
    config.bullet2_hit += 1
    return config.bullet2_hit


def bounce3y():
    import config
    global bullet3_dx, bullet3_dy, bullet3_hit
    config.bullet3_dy *= -1
    config.bullet3_dx *= 1
    config.bullet3_hit += 1
    return config.bullet3_hit



def bounce3x():
    import config
    global bullet3_dx, bullet3_dy, bullet3_hit
    config.bullet3_dy *= 1
    config.bullet3_dx *= -1
    config.bullet3_hit += 1
    return config.bullet3_hit



def bounce4y():
    import config
    global bullet4_dx, bullet4_dy, bullet4_hit
    config.bullet4_dy *= -1
    config.bullet4_dx *= 1
    config.bullet4_hit += 1
    return config.bullet4_hit


def bounce4x():
    import config
    global bullet4_dx, bullet4_dy, bullet4_hit
    config.bullet4_dy *= 1
    config.bullet4_dx *= -1
    config.bullet4_hit += 1
    return config.bullet4_hit

def limit_borders_upbullet2(player1, walls, player2, walls2):
    global bullet1_y, bullet2_y
    if player1 <= walls:
        bullet1_y = walls
        bounce1y()
    if player2 <= walls2:
        bullet2_y = walls2
        bounce2y()


def limit_borders_downbullet2(player1, walls, player2, wall2):
    global bullet1_y, bullet2_y
    if player1 >= walls:
        bullet1_y = walls
        bounce1y()
    if player2 >= wall2:
        bullet2_y = wall2
        bounce2y()


def limit_borders_leftbullet2(player1, walls, player2, wall2):
    global bullet1_x, bullet2_x
    if player1 <= walls:
        bullet1_x = walls
        bounce1x()
    if player2 <= wall2:
        bullet2_x = wall2
        bounce2x()


def limit_borders_rightbullet2(player1, wall, player2, wall2):
    global bullet1_x, bullet2_x
    if player1 >= wall:
        bullet1_x = wall
        bounce1x()
    if player2 >= wall2:
        bullet2_x = wall2
        bounce2x()


def limit_borders_upbullet(player1, walls, player2, walls2):
    global bullet3_y, bullet4_y
    if player1 <= walls:
        bullet3_y = walls
        bounce3y()
    if player2 <= walls2:
        bullet4_y = walls2
        bounce4y()


def limit_borders_downbullet(player1, walls, player2, wall2):
    global bullet3_y, bullet4_y
    if player1 >= walls:
        bullet4_y = walls
        bounce3y()
    if player2 >= wall2:
        bullet4_y = wall2
        bounce4y()


def limit_borders_leftbullet(player1, walls, player2, wall2):
    global bullet3_x, bullet4_x
    if player1 <= walls:
        bullet3_x = walls
        bounce3x()
    if player2 <= wall2:
        bullet4_x = wall2
        bounce4x()


def limit_borders_rightbullet(player1, wall, player2, wall2):
    global bullet3_x, bullet4_x
    if player1 >= wall:
        bullet3_x = wall
        bounce3x()
    if player2 >= wall2:
        bullet4_x = wall2
        bounce4x()
