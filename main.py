import pygame

pygame.init()
win = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("My game")

x = 50
y = 50
width = 50
height = 50
speed = 50

is_jump = False
jump_count = 10

run = True
while run:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    if keys[pygame.K_RIGHT] and x < 1200 - width:
        x += speed

    if keys[pygame.K_UP] and y > 0:
        y -= speed

    if keys[pygame.K_DOWN] and y < 800 - height:
        y += speed

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (50, 40, 60), (x, y, width, height))
    pygame.display.update()

pygame.quit()
