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

# create clock object
clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)

#game loop
while True:
    clock.tick(60)#loop rate

    event_list = pygame.event.get()

    if len(event_list) > 0:
        print(event_list)

    hero_rect.y -= 1

    if hero_rect.y <= 0:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    pygame.display.update()

pygame.quit()