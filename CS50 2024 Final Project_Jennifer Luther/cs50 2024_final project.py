import pygame
import random
import time
import sys

#initialize pygame
pygame.init()

#create variables for pygame window
window_WIDTH = 700
window_HEIGHT = 400

#generate game window
main_Screen = pygame.display.set_mode((window_WIDTH, window_HEIGHT))

#change window icon
img = pygame.image.load('C:\Users\jenni\hello\CS50 2024 Final Project_Jennifer Luther\Microsoft.png')
pygame.display.set_icon(img)

#set pygame window caption
pygame.display.set_caption('Just Another Snake Game')

#set clock
clock = pygame.time.Clock()

#define color variables
rose = (255, 207, 223)
blue = (12, 10, 208)
black = (0, 0, 0)
red = (255, 0, 0)
violet = (74, 26, 191)

#create snake speed
vel = 10

#create snake body
snake_spawn = [200, 80]

snake_size = [[100, 50],
              [90, 50]]

food_spawn = [random.randrange(1, (window_WIDTH//10)) * 10,
                  random.randrange(1, (window_HEIGHT//10)) * 10]

food = True

#create variables for the direction
direction = 'LEFT'
new_direction = direction

#def score function
#initialize score to 0
score = 0

def display_score(choice, color, font, size):

    #Create font object for score
    total_score = pygame.font.SysFont(font, size)

    #create a text surface object
    #text will be drawon on here
    score_bg = total_score.render('Score: ' + str(score), True, color)

    score_rect = score_bg.get_rect()

    #create the display window for score/blit()
    main_Screen.blit(score_bg, score_rect)

#def game over function
def game_over():

    #Create font object for game over font
    gameOver_font = pygame.font.SysFont('arial', 40)

    #create a text surface
    gameOver_surface = gameOver_font.render('FINAL SCORE : ' +str(score), True, black,)

    #create an object for text surface
    gameOver_bg = gameOver_surface.get_rect()

    #center text
    gameOver_bg.center = (window_WIDTH//2, window_HEIGHT//2)

    #draw surface object/text to the screen.
    main_Screen.blit(gameOver_surface, gameOver_bg)
    pygame.display.flip()

    #to exit game hit x-button on window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    #quit program
    quit()

#Main Function
running = True
while running:
    #include key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                new_direction = 'UP'
            if event.key == pygame.K_DOWN:
                new_direction  = 'DOWN'
            if event.key == pygame.K_RIGHT:
                new_direction = 'RIGHT'
            if event.key == pygame.K_LEFT:
                new_direction = 'LEFT'
            elif event.key == pygame.K_q:
                sys.exit()

    #prevent snake from moving in the same direction when
    #two keys are pressed simultaneously
    if new_direction == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if new_direction == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if new_direction == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if new_direction == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    #snake move mechanics
    #[1] = y-axis moving at velocity of 10
    #[0] = x-axis moving at velocity of 10
    if direction == 'UP':
        snake_spawn[1] -= 10
    if direction == 'DOWN':
        snake_spawn[1] += 10
    if direction == 'LEFT':
        snake_spawn[0] -= 10
    if direction == 'RIGHT':
        snake_spawn[0] += 10

    #growth/append mechanism
    # snake and food must collide to increase score
    #by 10 pts
    snake_size.insert(0, list(snake_spawn))
    if snake_spawn[0] == food_spawn[0] and snake_spawn[1] == food_spawn[1]:
        score += 10
        food = False
    else:
        snake_size.pop()

    if not food:
        food_spawn = [random.randrange(1, (window_WIDTH//10)) * 10,
                  random.randrange(1, (window_HEIGHT//10)) * 10]
        
    food = True
    main_Screen.fill(rose)

    for pos in snake_size:
        pygame.draw.rect(main_Screen, blue,
                         pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(main_Screen, red, pygame.Rect(
            food_spawn[0], food_spawn[1], 10, 10
        ))

    #if snake collides with wall,
    #results in game over.
    #set game over conditions
    if snake_spawn[0] < 0 or snake_spawn[0] > window_WIDTH-10:
        game_over()
    if snake_spawn[1] < 0 or snake_spawn[1] > window_HEIGHT-10:
        game_over()

    for block in snake_size[1:]:
        if snake_spawn[0] == block[0] and snake_spawn[1] == block[1]:
            game_over()

    #display score
    display_score(1, violet, 'comicsansms', 18)

    #refresh the game screen
    pygame.display.update()
    clock.tick(vel)