import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Avoid the car")

open_window = True

while open_window:

    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_window = False

    pygame.draw.circle(window, (0, 255, 0), (400, 300), 50)
    pygame.display.update()

pygame.quit()
