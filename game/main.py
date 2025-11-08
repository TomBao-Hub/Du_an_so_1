import pygame

pygame.init()

Screen = pygame.display.set_mode((600, 400))

Loop = True
while Loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: Loop = False

    mouse_pos = pygame.mouse.get_pos()

    Screen.fill((0, 0, 0))
    pygame.draw.line(Screen, (255, 0, 0), (mouse_pos[0], 0), (mouse_pos[0], 400), 1)
    pygame.draw.line(Screen, (0, 0, 255), (0, mouse_pos[1]), (600, mouse_pos[1]), 1)
    pygame.display.flip()

pygame.quit()
