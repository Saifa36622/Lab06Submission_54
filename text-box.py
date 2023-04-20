import sys 
import pygame as pg
pg.init()

win_x = 800
win_y = 400

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text = font.render('FRA 142', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (100,100)

screen = pg.display.set_mode((win_x, win_y))

while (1):
    screen.fill((255, 255, 255))
    screen.blit(text, textRect)
    pg.display.update()
    pg.time.delay(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
