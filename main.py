import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Avoid the car")

x = 400
y = 300
speed = 5

background = pygame.image.load('venv/assets/images/background.png')

open_window = True

while open_window:

    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_window = False

    commands = pygame.key.get_pressed()

    if commands[pygame.K_UP]:
        y -= speed
    if commands[pygame.K_DOWN]:
        y += speed
    if commands[pygame.K_RIGHT]:
        x += speed
    if commands[pygame.K_LEFT]:
        x -= speed

    window.blit(background, (0, 0))

    pygame.draw.circle(window, (0, 255, 0), (x, y), 50)
    pygame.display.update()

pygame.quit()
