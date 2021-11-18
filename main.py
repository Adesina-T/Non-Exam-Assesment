import pygame, sys
from pygame import mixer
import os
from settings import *
from level import Level
import random
from random import randrange
import time

#Setup
pygame.init()
x=100
y=100
screen = pygame.display.set_mode((screen_width,screen_height))
rec_width = screen_width /2
rec_height= screen_height /2
display = pygame.Surface((rec_width,rec_height))
window_size = (screen_width,screen_height)


clock = pygame.time.Clock()
level = Level(level_map,screen)
screen_shake = 0

def main_game_text():
    test_font = pygame.font.Font('C:/Users/Samue/Desktop/pcdynasty/fonts/greed.ttf', 50)
    text = test_font.render('Greed Island', False, 'Red')
    text_rect = text.get_rect(center=(780, 100))
    screen.blit(text, text_rect)

def main_bg():
    forest = pygame.image.load('C:/Users/Samue/Desktop/pcdynasty/graphics/forest.png').convert_alpha()
    forest = pygame.transform.scale(forest, (screen_width, screen_height))
    forest_rect = forest.get_rect()
    screen.blit(forest,forest_rect)







s=mixer.music.load('C:/Users/Samue/Desktop/New-Nea/Sounds/main.wav')
s=mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)





while True:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




    main_bg()
    main_game_text()
    level.run()
    #screen.blit(new,new_rect)


    pygame.display.update()
    clock.tick(60)
