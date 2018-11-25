import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))
# background
bg = pygame.image.load('./images/background.png')
screen.blit(bg, (0, 0))

# hero
hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (200, 200))


pygame.display.update()
# must do this, if you want the game render
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
