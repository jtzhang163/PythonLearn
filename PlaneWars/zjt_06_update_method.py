import pygame

pygame.init()

#create game's window
screen = pygame.display.set_mode((480,700))

#paint background image
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
# pygame.display.update()

#paint hero image
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150,500))
pygame.display.update()

#game loop
while True:
    pass

pygame.quit()