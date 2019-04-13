import pygame
import time
import random

pygame.init()  # Checks if the module was initialized successfully

white = (255, 255, 255)
black = (0, 0, 0)
brown = (170, 105, 57)
red = (204, 40, 40)
light_brown = (255, 199, 157)
# colour = (red, green, blue)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
# The paramiter must be a tuple (width, height).

pygame.display.set_caption('home alone')  # Title of the window


clock = pygame.time.Clock()

block_size = 20


font = pygame.font.SysFont(None, 25)
font2 = pygame.font.SysFont('felixtitling', 50)


def snake(block_size, snakeList):  # The head of the snake
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, brown, [XnY[0], XnY[1],
                                              block_size, block_size])
    # .draw paramiters: (position, colour, [x-axis, y-axis, width, height])


def text_objects(text, color, font):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def homescreen():
    gameDisplay.fill(brown)
    textSurf, textRect = text_objects("home alone", white, font2)
    textSurf2, textRect2 = text_objects("press c to play", white, font)
    textRect.center = (display_width / 2), (display_height / 2)
    textRect2.center = (display_width / 2), (display_height / 2) + 40
    gameDisplay.blit(textSurf, textRect)
    gameDisplay.blit(textSurf2, textRect2)
    pygame.display.update()

    gameExit = False
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    gameLoop()
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                    gameOver = False
            if event.type == pygame.QUIT:
                gameExit = True

    pygame.quit()
    quit()


def endgame_screen(points):
    points = str(points)
    screen_text = font.render("game over, press c to play again or q to quit",
                              True, white)  # True here stands for anti-aliasing
    your_score = font.render("your score: " + points, True, white)
    divider = font.render("____________________________________________", True, white)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    gameDisplay.blit(your_score, [display_width/2, (display_height/2)+25])
    gameDisplay.blit(divider, [(display_width/2), (display_height/2)+40])


def score(score):
    score = str(score)
    screen_text = font.render("score: " + score, True, white)
    divider = font.render("____________________________________________", True, white)
    gameDisplay.blit(screen_text, [display_width-200, 50])
    gameDisplay.blit(divider, [display_width-200, 50+20])


def gameLoop():
    FPS = 10  # Frames per second = the speed of the snake
    points = 0
    level = 0
    gameExit = False
    gameOver = False

    lead_x = display_width/2  # Resolution/2 = the middle of the screen
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    # lead = The Position of the head of the snake
    randAppleX = round(random.randrange(20, display_width-20-block_size)/block_size)*block_size
    randAppleY = round(random.randrange(20, display_height-20-block_size)/block_size)*block_size

    snakeList = []
    snakeLength = 1

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(brown)
            endgame_screen(points)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:  # "If a key is pressed"
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        lead_x_change = -block_size
                        lead_y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    lead_x_change = block_size
                    lead_y_change = 0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        lead_x_change = block_size
                        lead_y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(light_brown)  # Background colour

        # apple
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        score(points)

        if level == 10:
            FPS += 1
            level = 0

        pygame.display.update()
        # .update() refreshes only the necessary parts
        # .flip() refreshes the entire display

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(20, display_width -
                                                20-block_size)/block_size)*block_size
            randAppleY = round(random.randrange(20, display_height -
                                                20-block_size)/block_size)*block_size
            snakeLength += 1
            points += 1
            level += 1

        clock.tick(FPS)

    pygame.quit()
    quit()


homescreen()
