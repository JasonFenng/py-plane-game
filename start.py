import pygame
from plane_sprites import GameSprite

pygame.init()

screen = pygame.display.set_mode((480, 700))
# background
bg = pygame.image.load('./images/background.png')
screen.blit(bg, (0, 0))

# hero
hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (200, 200))
hero_rect = pygame.Rect(200, 200, 102, 126)

# enemy
enemy = GameSprite('./images/enemy1.png')
enemy1 = GameSprite('./images/enemy1.png', 2)
enemy_group = pygame.sprite.Group(enemy, enemy1)

clock = pygame.time.Clock()

# game loop
while True:
    # 60 fps
    # clock.tick(60)
    
    hero_rect.y -= 2
    if hero_rect.y <= -126:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # let sprite call update method, update their position
    enemy_group.update()
    # draw sprite_group, show all sprites
    enemy_group.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
