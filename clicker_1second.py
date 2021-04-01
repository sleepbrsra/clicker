import pygame as pg
import  sys, pygame
from pygame.locals import *


pg.init()
screen = pg.display.set_mode((600, 400))
fps_clock = pg.time.Clock()
FPS = 60
GRAY = pg.Color('gray12')
WHITE = pg.Color('red')
pygame.display.set_caption('cps for demons')
FONT = pg.font.Font(None, 42)

clicks = 0
start_time = 0
passed_time = 0
run_me = True

while run_me:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_me = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button.
                # Start the timer if it's stopped.
                if start_time == 0:
                    start_time = pg.time.get_ticks()
                if passed_time < 1:  # Count the clicks.
                    clicks += 1
            # Press the right mouse button to reset the timer and clicks.
            elif event.button == 3:
                start_time = 0
                passed_time = 0
                clicks = 0

    if passed_time < 1 and start_time != 0:
        # Calculate the passed time. / 1000 to convert it to seconds.
        passed_time = (pg.time.get_ticks() - start_time) / 1000

    time_surface = FONT.render('Time: {}'.format(passed_time), True, WHITE)
    clicks_surface = FONT.render('Clicks: {}'.format(clicks), True, WHITE)

    screen.fill(GRAY)
    screen.blit(time_surface, (30, 30))
    screen.blit(clicks_surface, (30, 70))
    pg.display.flip()
    fps_clock.tick(FPS)

pg.quit()