from os import path
import pygame
from level import render


class Character:        # Important : directions list : Up = 1; Right = 2; Down = 3; Left = 4
    """Character class"""

    def __init__(self, posX, posY, currentBotLine):
        self.__posX = posX
        self.__posY = posY
        self.__blocksFallen = 0
        self.__climb = 0
        self.__bg = path.join("Assets", "Textures", "Background", "bg.png")
        self.__texturePath = path.join("Assets", "Textures", "Character", "testpink.png")

    def blocksFallenAcc(self):
        return self.__blocksFallen

    def climbAcc(self):
        return self.__climb

    def display(self, surface):

        image = pygame.image.load(self.__texturePath)
        surface.blit(image, (self.__posX * 64 + 26, (self.__posY * 64 + 12) - self.__blocksFallen * 64))

    def backDownCleanup(self, surface):
        image = pygame.image.load(self.__bg)
        surface.blit(image, (self.__posX * 64 + 26, (self.__posY * 64 + 12) - self.__blocksFallen * 64 - 64))
        self.display(surface)

    def move(self, surface, direction, level):

        # Right

        if direction == 2 and self.__posX < len(level[0]) - 1 and self.__posX < len(level[0]) - 1 \
                and level[self.__posY][self.__posX + 1].hpAccess() == 0:

            level[self.__posY][self.__posX].display(surface, 0, self.__blocksFallen)
            self.__posX += 1
            self.display(surface)

        # Right Climb

        elif direction == 2 and self.__posX < len(level[0]) - 1 and self.__posX < len(level[0]) - 1 \
                and level[self.__posY][self.__posX + 1].hpAccess() != 0 \
                and level[self.__posY - 1][self.__posX].hpAccess() == 0 \
                and level[self.__posY - 1][self.__posX + 1].hpAccess() == 0:

            level[self.__posY][self.__posX].display(surface, 0, self.__blocksFallen)
            self.__posX += 1
            self.__posY -= 1
            self.__climb += 1
            self.display(surface)

        # Left

        elif direction == 3 and self.__posX > 0 \
                and level[self.__posY][self.__posX - 1].hpAccess() == 0:

            level[self.__posY][self.__posX].display(surface, 0, self.__blocksFallen)
            self.__posX -= 1
            self.display(surface)

        # Left Climb

        elif direction == 3 and self.__posX > 0 \
            and level[self.__posY][self.__posX - 1].hpAccess() != 0 \
                and level[self.__posY - 1][self.__posX].hpAccess() == 0 \
                and level[self.__posY - 1][self.__posX - 1].hpAccess() == 0:

            level[self.__posY][self.__posX].display(surface, 0, self.__blocksFallen)
            self.__posX -= 1
            self.__posY -= 1
            self.__climb += 1
            self.display(surface)

    def breakBlock(self, surface, direction, level, currentBotLine):

        # Right

        if direction == 2 \
                and self.__posX < len(level[0])-1 \
                and level[self.__posY][self. __posX+1].hpAccess() > 0:
            level[self.__posY][self. __posX+1].hit(surface)

        # Down

        elif direction == 3 \
                and self.__posY < currentBotLine \
                and level[self.__posY+1][self. __posX].hpAccess() > 0:
            level[self.__posY+1][self. __posX].hit(surface)

        # Left

        elif direction == 4 \
                and self.__posX > 0 \
                and level[self.__posY][self. __posX-1].hpAccess() > 0:
            level[self.__posY][self. __posX-1].hit(surface)

    def fall(self, surface, level):

        if self.__posY < len(level)-2 and level[self.__posY+1][self.__posX].hpAccess() == 0:
            if self.__climb == 0:
                self.__blocksFallen += 1
                self.__posY += 1
            else:
                self.__climb -= 1
                self.__posY += 1
            return self.__blocksFallen

