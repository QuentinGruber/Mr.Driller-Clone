from os import path
import pygame


class Character:        # Important : directions list : Up = 1; Right = 2; Down = 3; Left = 4
    """Character class"""

    def __init__(self, posX, posY):
        self.__posX = posX
        self.__posY = posY
        self.__texturePath = path.join("Assets", "Textures", "Character", "testpink.png")

    def display(self, surface):

        image = pygame.image.load(self.__texturePath)
        surface.blit(image, (self.__posX * 64 + 26, self.__posY * 64 + 12))

    def move(self, surface, direction, level):

        if direction == 1 and self.__posY > 0:      # Up
            level[self.__posY][self.__posX].display(surface)
            self.__posY -= 1
            self.display(surface)

        elif direction == 2 and self.__posX < len(level[0])-1:        # Right
            level[self.__posY][self.__posX].display(surface)
            self.__posX += 1
            self.display(surface)

        elif direction == 3 and self.__posX > 0:        # Left
            level[self.__posY][self.__posX].display(surface)
            self.__posX -= 1
            self.display(surface)

    def breakBlock(self, surface, direction, level):

        if direction == 1 and self.__posY > 0 and level[self.__posY-1][self. __posX].hpAccess() > 0:      # Up
            level[self.__posY-1][self. __posX].hit(surface)




def drawBG():
    redBlock = pygame.image.load(path.join("Assets", "Textures", "Blocks", "1", "1_s.png")).convert()
    cyanBlock = pygame.image.load(os.path.join("Assets", "Textures", "Blocks", "2", "2_s.png")).convert()
    pinkBlock = pygame.image.load(os.path.join("Assets", "Textures", "Blocks", "3", "3_s.png")).convert()
    purpleBlock = pygame.image.load(os.path.join("Assets", "Textures", "Blocks", "4", "4_s.png")).convert()

    BG = []
    for i in range(3):
        BG.append(redBlock)
        BG.append(cyanBlock)
        BG.append(pinkBlock)
        BG.append(purpleBlock)

    return BG