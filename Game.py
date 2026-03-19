

import pygame

from Menu import Menu
from code.const import WIN_WITH, WIN_HEIGTH


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WITH , WIN_HEIGTH))


    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

        #While True:
        # check for all event
        #for event in pygame.event.get():
           # if event.type == pygame.QUIT:
               # pygame.quit()  # fevha a janela
               # quit()