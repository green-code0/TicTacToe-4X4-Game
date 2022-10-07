import pygame
from pygame.locals import *

# it must be here to initial and save screen
pygame.init()

# size the screen
screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TictacToe")

# define variable
line_width = 6
markers = []
clicked = False
pos = []
player = 1
winner = 0
gameover = False

# define colors
red = (200, 50, 50)
green = (50, 200, 50)
blue = (50, 50, 200)

# define font
font = pygame.font.SysFont(None, 40)

# create play again rect
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)


def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 4):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)

for x in range(4):
    row = [0] * 4
    markers.append(row)


def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15,),
                                 (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85,),
                                 (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1

def Check_winner():
    global winner
    global gameover

    y_pos = 0
    for x in markers:
        # check column 4 X 4
        if sum(x) == 4:
            winner = 1
            gameover = True
        if sum(x) == -4:
            winner = 2
            gameover = True

        #  check row 4 x 4
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] + markers[3][y_pos] == 4:
            winner = 1
            gameover = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] + markers[3][y_pos] == -4:
            winner = 2
            gameover = True
        y_pos += 1


    # check trace 4 x 4
    if markers[0][0] + markers[1][1] + markers[2][2] + markers[3][3] == 4 or markers[3][0] + markers[2][1] + markers[1][2] + markers[0][3] == 4:
        winner = 1
        gameover = True
    if markers[0][0] + markers[1][1] + markers[2][2] + markers[3][3] == -4 or markers[3][0] + markers[2][1] + markers[1][2] + markers[0][3] == -4:
        winner = 2
        gameover = True

    # check trace 3 x 3 (top-left)
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or  markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        gameover = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or  markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        gameover = True

    # check trace 3 x 3 (top-right)
    if markers[1][0] + markers[2][1] + markers[3][2] == 3 or  markers[1][2] + markers[2][1] + markers[3][0] == 3:
        winner = 1
        gameover = True
    if markers[1][0] + markers[2][1] + markers[3][2] == -3 or  markers[1][2] + markers[2][1] + markers[3][0] == -3:
        winner = 2
        gameover = True


    # check trace 3 x 3 (bottom-left)
    if markers[0][1] + markers[1][2] + markers[2][3] == 3 or  markers[0][3] + markers[1][2] + markers[2][1] == 3:
        winner = 1
        gameover = True
    if markers[0][1] + markers[1][2] + markers[2][3] == -3 or  markers[0][3] + markers[1][2] + markers[2][1] == -3:
        winner = 2
        gameover = True

    # check trace 3 x 3 (bottom-right)
    if markers[1][1] + markers[2][2] + markers[3][3] == 3 or  markers[1][3] + markers[2][2] + markers[3][1] == 3:
        winner = 1
        gameover = True
    if markers[1][1] + markers[2][2] + markers[3][3] == -3 or  markers[1][3] + markers[2][2] + markers[3][1] == -3:
        winner = 2
        gameover = True

     # check column 3 X 3 , check row 3 X 3
    for c in range(0,4):
        top3 = left3 = 0
        for x in range(0, 3):
            top3 += markers[c][x]
            left3 += markers[x][c]
        if top3 == 3 or left3 == 3:
            winner = 1
            gameover = True
        if top3 == -3 or left3 == -3:
            winner = 2
            gameover = True
        bottom3 = right3 = 0
        for x in range(1, 4):
            bottom3 += markers[c][x]
            right3 += markers[x][c]
        if bottom3 == 3 or right3 == 3:
             winner = 1
             gameover = True
        if bottom3 == -3 or right3 == -3:
             winner = 2
             gameover = True

def draw_winner(winner):
    win_text = ' player ' + str(winner) + '  wins!'
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 220, 50), )
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = ' play again'
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))

run = True
while run:

    draw_grid()
    draw_markers()


    # add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if gameover == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    Check_winner()

    if gameover == True:
        draw_winner(winner)
        # check for mouseclick to see if user has clicked on play again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                markers = []
                pos = []
                player = 1
                winner = 0
                gameover = False
                for x in range(4):
                    row = [0] * 4
                    markers.append(row)

    pygame.display.update()

pygame.quit()

