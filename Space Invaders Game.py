#!/usr/bin/env python
import pygame
import time
import random
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
running = True
background = pygame.image.load('Starry Sky Space Invaders 2.png')

# background sound
mixer.music.load('Background.mp3')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerX = 370
playerY = 480
playerX_change = 0

# Pause and Play Icons
pause = pygame.image.load('pause.png')
play = pygame.image.load('play-button.png')

def player(x, y):
    screen.blit(playerImg, (x, y))


# Bullet

# Ready = Invisible bullet
# Fire = Moving bullet
bulletImg = pygame.image.load('SI Fireball.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    global bulletImg
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))


def is_collision(enx, eny, bx, by):
    global bullet_state
    if bullet_state == "ready":
        return False
    distance = math.sqrt(math.pow((enx - bx), 2) + math.pow((eny - by), 2))
    if distance < 27:
        return True
    else:
        return False


def initiate_freeplay():
    # globals
    global running
    global bulletImg
    global bulletX
    global bulletY
    global screen
    global bullet_state
    global playerImg
    global playerX_change
    global playerX
    global playerY
    global score_value
    global game_activated
    global game_mode_picked
    global pause
    global play

    # Pick Difficulty
    difficulty_chosen = False
    while running and not difficulty_chosen:
        screen.blit(background, (0, 0))
        font = pygame.font.Font('ethnocentric rg it.ttf', 32)
        pick_difficulty_text = font.render("Pick your difficulty!", True, (255, 255, 255))
        screen.blit(pick_difficulty_text, (180, 280))
        _1 = font.render("1", True, (255, 255, 255))
        _2 = font.render("2", True, (255, 255, 255))
        _3 = font.render("3", True, (255, 255, 255))
        screen.blit(_1, (332, 340))
        screen.blit(_2, (394, 340))
        screen.blit(_3, (466, 340))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_b:
                    game_activated = False
                    game_mode_picked = False
                    return
                if event.key == pygame.K_1:
                    e_num = 3
                    e_speed = 3
                    difficulty_chosen = True
                    difficulty = 1
                if event.key == pygame.K_2:
                    e_num = 6
                    e_speed = 5
                    difficulty = 2
                    difficulty_chosen = True
                if event.key == pygame.K_3:
                    e_num = 8
                    e_speed = 6
                    difficulty = 3
                    difficulty_chosen = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if 330 < mouseY < 382:
                    if 322 < mouseX < 374:
                        e_num = 3
                        e_speed = 3
                        difficulty_chosen = True
                        difficulty = 1
                    if 384 < mouseX < 446:
                        e_num = 6
                        e_speed = 5
                        difficulty = 2
                        difficulty_chosen = True
                    if 456 < mouseX < 508:
                        e_num = 8
                        e_speed = 6
                        difficulty = 3
                        difficulty_chosen = True


    # diffuclty
    diff_text = font.render(f'{difficulty}', True, (255, 255, 255))

    def show_difficulty():
        screen.blit(diff_text, (758, 10))

    # Enemy

    enemyImg = pygame.image.load('ufo.png')
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = e_num

    for i in range(num_of_enemies):
        enemyX.append(random.randint(10, 726))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(e_speed)
        enemyY_change.append(30)

    def draw_enemy(x, y):
        while not 0 < x < 736:
            x += random.randint(-10, 10)
        screen.blit(enemyImg, (x, y))

    # Score
    score_value = 0
    font = pygame.font.Font('ethnocentric rg it.ttf', 32)
    textX = 10
    textY = 10

    def show_score(x, y, color):
        global score_value
        score = font.render(f"Score: {score_value}", True, color)
        screen.blit(score, (x, y))


    # Game Loop
    while running and game_activated:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 255))
        # background image
        screen.blit(background, (0, 0))
        screen.blit(pause, (10, 526))
        show_difficulty()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return
            # if keystroke is pressed, check direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerX_change = -3
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerX_change = 3
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound('Laser-Sound-Effect.mp3')
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_UP:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound('Laser-Sound-Effect.mp3')
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_w:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound('Laser-Sound-Effect.mp3')
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_q:
                    lost = font.render("You Lost!", True, (0, 0, 0))
                    screen.blit(lost, (300, 280))
                    color = (0, 0, 0)
                    show_difficulty()
                    show_score(300, 320, color)
                    player(playerX, playerY)
                    pygame.display.update()
                    pygame.mixer.music.stop()
                    end_sound = mixer.Sound('You-Lose.mp3')
                    end_sound.play()
                    time.sleep(3)
                    game_activated = False
                    game_mode_picked = False
                    mixer.music.load('Background.mp3')
                    mixer.music.play(-1)
                    return
                if event.key == pygame.K_p:
                    paused = True
                    while paused:
                        screen.blit(play, (10, 526))
                        pygame.display.update()
                        for press in pygame.event.get():
                            if press.type == pygame.KEYDOWN:
                                if press.key == pygame.K_p:
                                    paused = False
                            if press.type == pygame.MOUSEBUTTONDOWN:
                                mouseX, mouseY = pygame.mouse.get_pos()
                                if mouseY > 516:
                                    if mouseX < 84:
                                        paused = False
                if event.key == pygame.K_b:
                    game_activated = False
                    game_mode_picked = False
                    return
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerX_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerX_change = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseY < 450:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound('Laser-Sound-Effect.mp3')
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                else:
                    if mouseX > playerX:
                        playerX_change = 3
                    else:
                        playerX_change = -3
                if mouseY > 516 and mouseX < 84:
                    paused = True
                    while paused:
                        screen.blit(play, (10, 526))
                        pygame.display.update()
                        for press in pygame.event.get():
                            if press.type == pygame.KEYDOWN:
                                if press.key == pygame.K_p:
                                    paused = False
                            if press.type == pygame.MOUSEBUTTONDOWN:
                                mouseX, mouseY = pygame.mouse.get_pos()
                                if mouseY > 516:
                                    if mouseX < 84:
                                        paused = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseY > 450:
                    playerX_change = 0


        # bullet movement
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
            if bulletY < 0:
                bulletY = 480
                bullet_state = "ready"

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
            for _ in range(15):
                playerX += 3
                player(playerX, playerY)
                pygame.display.update()
                time.sleep(0.01)
        if playerX >= 736:
            playerX = 736
            for _ in range(15):
                playerX -= 3
                player(playerX, playerY)
                enemyX += enemyX_change
                pygame.display.update()
                time.sleep(0.01)

        for i in range(num_of_enemies):
            enemyX[i] += enemyX_change[i]
            if enemyY[i] >= 480:
                lost = font.render("You Lost!", True, (0, 0, 0))
                screen.blit(lost, (300, 280))
                color = (0, 0, 0)
                show_score(300, 320, color)
                player(playerX, playerY)
                pygame.display.update()
                pygame.mixer.music.stop()
                end_sound = mixer.Sound('You-Lose.mp3')
                end_sound.play()
                time.sleep(3)
                game_activated = False
                game_mode_picked = False
                mixer.music.load('Background.mp3')
                mixer.music.play(-1)
                return
            if enemyX[i] <= 0:
                enemyX[i] = 0
                enemyX_change[i] = e_speed
                enemyY[i] += enemyY_change[i]
            if enemyX[i] >= 730:
                enemyX[i] = 730
                enemyX_change[i] = -1 * e_speed
                enemyY[i] += enemyY_change[i]

            # Collision
            if is_collision(enemyX[i], enemyY[i], bulletX, bulletY):
                bulletY = 480
                bullet_state = 'ready'
                explosion_sound = mixer.Sound('Explosion (1).mp3')
                explosion_sound.set_volume(2.0)
                explosion_sound.play()
                score_value += 100
                enemyX[i] = random.randint(10, 726)
                enemyY[i] = random.randint(50, 150)

        player(playerX, playerY)
        for i in range(num_of_enemies):
            draw_enemy(enemyX[i], enemyY[i])
        color = (255, 255, 255)
        show_score(textX, textY, color)
        pygame.display.update()


# Levels Mode

level_list = {}

level_list[1] = {
    "enemies": 1,
    "enemy_speed": 3,
    "minscore": 500
}
level_list[2] = {
    "enemies": 2,
    "enemy_speed": 3,
    "minscore": 1000
}
level_list[3] = {
    "enemies": 2,
    "enemy_speed": 4,
    "minscore": 1200
}
level_list[4] = {
    "enemies": 3,
    "enemy_speed": 4,
    "minscore": 1200
}
level_list[5] = {
    "enemies": 3,
    "enemy_speed": 5,
    "minscore": 1500
}
level_list[6] = {
    "enemies": 4,
    "enemy_speed": 5,
    "minscore": 1800
}
level_list[7] = {
    "enemies": 5,
    "enemy_speed": 5,
    "minscore": 2000
}
level_list[8] = {
    "enemies": 5,
    "enemy_speed": 5,
    "minscore": 2300
}
level_list[9] = {
    "enemies": 6,
    "enemy_speed": 5,
    "minscore": 2500
}
level_list[10] = {
    "enemies": 7,
    "enemy_speed": 6,
    "minscore": 2500
}
level_list[11] = {
    "enemies": 7,
    "enemy_speed": 6,
    "minscore": 2700
}
level_list[11] = {
    "enemies": 8,
    "enemy_speed": 6,
    "minscore": 2700
}
level_list[12] = {
    "enemies": 8,
    "enemy_speed": 6,
    "minscore": 3000
}
level_list[13] = {
    "enemies": 10,
    "enemy_speed": 6,
    "minscore": 3000
}
level_list[14] = {
    "enemies": 9,
    "enemy_speed": 6,
    "minscore": 3300
}
level_list[15] = {
    "enemies": 10,
    "enemy_speed": 6,
    "minscore": 4000
}

def initiate_levels(level):
    # globals
    global running
    global bulletImg
    global bulletX
    global bulletY
    global screen
    global bullet_state
    global playerImg
    global playerX_change
    global playerX
    global playerY
    global score_value
    global level_list
    global game_activated
    global game_mode_picked
    global lives
    global play

    minscore = level_list[level]["minscore"]
    score_value = 0

    # Enemy

    enemyImg = pygame.image.load('ufo.png')
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = level_list[level]["enemies"]

    for i in range(num_of_enemies):
        enemyX.append(random.randint(10, 726))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(level_list[level]["enemy_speed"])
        enemyY_change.append(30)

    def draw_enemy(x, y):
        while not 0 < x < 736:
            x += random.randint(-10, 10)
        screen.blit(enemyImg, (x, y))

    # Score
    score_value = 0
    font = pygame.font.Font('ethnocentric rg it.ttf', 32)
    textX = 10
    textY = 10

    #level
    level_text = font.render(f'{level}', True, (255, 255, 255))

    def show_level():
        if level < 10:
            screen.blit(level_text, (758, 10))
        else:
            screen.blit(level_text, (726, 10))

    def show_lives():
        global lives
        lives_text = font.render(f'{lives}', True, (0, 0, 0))
        screen.blit(lives_text, (758, 558))

    def show_score(x, y, color):
        global score_value
        global minscore
        global level_list
        minscore = level_list[level]["minscore"]
        score = font.render(f"Score: {score_value}/{minscore}", True, color)
        screen.blit(score, (x, y))


    # Game Loop
    while running and game_activated:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 255))
        # background image
        screen.blit(background, (0, 0))
        screen.blit(pause, (10, 526))
        show_level()
        show_lives()
        if score_value >= minscore:
            # start_time = time.time()
            screen.blit(background, (0, 0))
            victory = font.render(f"Wave {level} cleared!", True, (255, 255, 255))
            screen.blit(victory, (200, 10))
            screen.blit(playerImg, (368, 480))
            # for event in pygame.event.get():
            #     mouseX, mouseY = pygame.mouse.get_pos()
            #     if mouseY > 516 and mouseX < 84:
            #         paused = True
            #         while paused:
            #             screen.blit(play, (10, 526))
            #             pygame.display.update()
            #             for press in pygame.event.get():
            #                 if press.type == pygame.KEYDOWN:
            #                     if press.key == pygame.K_p:
            #                         paused = False
            #                 if press.type == pygame.MOUSEBUTTONDOWN:
            #                     mouseX, mouseY = pygame.mouse.get_pos()
            #                     if mouseY > 516:
            #                         if mouseX < 84:
            #                             paused = False
            pygame.display.update()
            time.sleep(3)
            if level < len(level_list):
                initiate_levels(level + 1)
            else:
                # start_time = time.time()
                screen.blit(background, (0, 0))
                complete = font.render("All Waves Cleared!", True, (255, 255, 255))
                screen.blit(complete, (200, 10))
                screen.blit(playerImg, (368, 480))
                # for event in pygame.event.get():
                #     mouseX, mouseY = pygame.mouse.get_pos()
                #     if mouseY > 516 and mouseX < 84:
                #         paused = True
                #         while paused:
                #             screen.blit(play, (10, 526))
                #             pygame.display.update()
                #             for press in pygame.event.get():
                #                 if press.type == pygame.KEYDOWN:
                #                     if press.key == pygame.K_p:
                #                         paused = False
                #                 if press.type == pygame.MOUSEBUTTONDOWN:
                #                     mouseX, mouseY = pygame.mouse.get_pos()
                #                     if mouseY > 516:
                #                         if mouseX < 84:
                #                             paused = False
                pygame.display.update()
                time.sleep(3)
                game_activated = False
                game_mode_picked = False
        if not game_activated:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return
            # if keystroke is pressed, check direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerX_change = -3
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerX_change = 3
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound('Laser-Sound-Effect.mp3')
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_UP:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound('Laser-Sound-Effect.mp3')
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_w:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound('Laser-Sound-Effect.mp3')
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_q:
                    lives -= 1
                    if lives <= 0:
                        lost = font.render("You Lost!", True, (0, 0, 0))
                        screen.blit(lost, (300, 280))
                        color = (0, 0, 0)
                        show_score(300, 320, color)
                        show_level()
                        lives = 0
                        show_lives()
                        player(playerX, playerY)
                        pygame.display.update()
                        pygame.mixer.music.stop()
                        end_sound = mixer.Sound('You-Lose.mp3')
                        end_sound.play()
                        time.sleep(3)
                        game_activated = False
                        game_mode_picked = False
                        mixer.music.load('Background.mp3')
                        mixer.music.play(-1)
                        return
                    else:
                        initiate_levels(level)
                if event.key == pygame.K_p:
                    paused = True
                    while paused:
                        screen.blit(play, (10, 526))
                        pygame.display.update()
                        for press in pygame.event.get():
                            if press.type == pygame.KEYDOWN:
                                if press.key == pygame.K_p:
                                    paused = False
                            if press.type == pygame.MOUSEBUTTONDOWN:
                                mouseX, mouseY = pygame.mouse.get_pos()
                                if mouseY > 516:
                                    if mouseX < 84:
                                        paused = False
                if event.key == pygame.K_b:
                    game_activated = False
                    game_mode_picked = False
                    return
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerX_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerX_change = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseY < 450:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound('Laser-Sound-Effect.mp3')
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                else:
                    if mouseX > playerX:
                        playerX_change = 3
                    else:
                        playerX_change = -3
                if mouseY > 516 and mouseX < 84:
                    paused = True
                    while paused:
                        screen.blit(play, (10, 526))
                        pygame.display.update()
                        for press in pygame.event.get():
                            if press.type == pygame.KEYDOWN:
                                if press.key == pygame.K_p:
                                    paused = False
                            if press.type == pygame.MOUSEBUTTONDOWN:
                                mouseX, mouseY = pygame.mouse.get_pos()
                                if mouseY > 516:
                                    if mouseX < 84:
                                        paused = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseY > 450:
                    playerX_change = 0


        # bullet movement
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
            if bulletY < 0:
                bulletY = 480
                bullet_state = "ready"

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
            for _ in range(15):
                playerX += 3
                player(playerX, playerY)
                pygame.display.update()
                time.sleep(0.01)
        if playerX >= 736:
            playerX = 736
            for _ in range(15):
                playerX -= 3
                player(playerX, playerY)
                enemyX += enemyX_change
                pygame.display.update()
                time.sleep(0.01)

        for i in range(num_of_enemies):
            enemyX[i] += enemyX_change[i]
            if enemyY[i] >= 480:
                lives -= 1
                if lives <= 0:
                    lost = font.render("You Lost!", True, (0, 0, 0))
                    screen.blit(lost, (300, 280))
                    color = (0, 0, 0)
                    show_score(300, 320, color)
                    show_level()
                    player(playerX, playerY)
                    pygame.display.update()
                    lives = 0
                    show_lives()
                    pygame.display.update()
                    pygame.mixer.music.stop()
                    end_sound = mixer.Sound('You-Lose.mp3')
                    end_sound.play()
                    time.sleep(3)
                    game_activated = False
                    game_mode_picked = False
                    mixer.music.load('Background.mp3')
                    mixer.music.play(-1)
                    return
                else:
                    initiate_levels(level)
            if enemyX[i] <= 0:
                enemyX[i] = 0
                enemyX_change[i] = -1 * enemyX_change[i]
                enemyY[i] += enemyY_change[i]
            if enemyX[i] >= 730:
                enemyX[i] = 730
                enemyX_change[i] = -1 * enemyX_change[i]
                enemyY[i] += enemyY_change[i]

            # Collision
            if is_collision(enemyX[i], enemyY[i], bulletX, bulletY):
                bulletY = 480
                bullet_state = 'ready'
                explosion_sound = mixer.Sound('Explosion (1).mp3')
                explosion_sound.set_volume(2.0)
                explosion_sound.play()
                score_value += 100
                enemyX[i] = random.randint(10, 726)
                enemyY[i] = random.randint(50, 150)

        player(playerX, playerY)
        for i in range(num_of_enemies):
            draw_enemy(enemyX[i], enemyY[i])
        color = (255, 255, 255)
        show_score(textX, textY, color)
        pygame.display.update()


# Picking Game Mode

playerImg2 = pygame.image.load('space-invaders.png')
playerImg2 = pygame.transform.scale(playerImg2, (64, 64))
playerImg1 = pygame.image.load('space-invaders-player.png')
font = pygame.font.Font('ethnocentric rg it.ttf', 32)
game_mode_picked = False
while running and not game_mode_picked:
    lives = 3
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_1:
                game_mode_picked = True
                game_activated = True
                playerImg = playerImg1
                initiate_freeplay()
            if event.key == pygame.K_2:
                game_mode_picked = True
                game_activated = True
                playerImg = playerImg2
                initiate_levels(1)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            if 260 < mouseX < 500:
                if 255 < mouseY < 340:
                    game_mode_picked = True
                    game_activated = True
                    playerImg = playerImg1
                    initiate_freeplay()
                elif 340 < mouseY < 410:
                    game_mode_picked = True
                    game_activated = True
                    lives = 3
                    playerImg = playerImg2
                    initiate_levels(1)
    screen.blit(playerImg1, (260, 258))
    screen.blit(playerImg2, (260, 342))
    white = (255, 255, 255)
    freeplay_text = font.render("Freeplay", True, white)
    levels_text = font.render("Waves", True, white)
    choose_text = font.render("Choose a Mode:", True, white)
    screen.blit(freeplay_text, (340, 265))
    screen.blit(levels_text, (340, 349))
    screen.blit(choose_text, (280, 20))
    pygame.display.update()

#Quitting

pygame.display.quit()
pygame.quit()
