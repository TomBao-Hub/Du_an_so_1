import pygame as pg

pg.init()
Screen = pg.display.set_mode((600, 400))
Font = pg.font.Font(None, 20)
Text = Font.render("WELCOME TO THE GAME ADVENTURE!", True, (255, 255, 255))

Loop = True
while Loop:
    for event in pg.event.get():
        if event.type == pg.QUIT: Loop = False

    Screen.fill((0, 0, 0))
    Screen.blit(Text, (5, 5))
    pg.display.flip()