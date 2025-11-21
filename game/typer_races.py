import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typer Races")
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
timer = pygame.time.Clock()
fps = 60

level = 0
active_string = "text string"
score = 0
high_score = 1
lives = 5

header_font = pygame.font.Font('assets/fonts/square.ttf', 50)
pause_font = pygame.font.Font('assets/fonts/1up.ttf', 38)
banner_font = pygame.font.Font('assets/fonts/1up.ttf', 28)
font = pygame.font.Font('assets/fonts/AldotheApache.ttf', 48)

class Button:
	def __init__(self, x_pos, y_pos, text, clicked, surf):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.text = text
		self.clicked = clicked
		self.surf = surf

	def draw(self):
		cir = pygame.draw.circle(self.surf, (45, 89, 135), (self.x_pos, self.y_pos), 35)
		if cir.collidepoint(pygame.mouse.get_pos()):
			butts = pygame.mouse.get_pressed()
			if butts[0]:
				pygame.draw.circle(self.surf, (190, 35, 35), (self.x_pos, self.y_pos), 35)
				self.clicked =True
			else:
				pygame.draw.circle(self.surf, (190, 89, 135), (self.x_pos, self.y_pos), 35)

		pygame.draw.circle(self.surf, 'white', (self.x_pos, self.y_pos), 35, 3)
		self.surf.blit(pause_font.render(self.text, True, 'white'), (self.x_pos - 15, self.y_pos - 25))
		

def draw_screen():
	pygame.draw.rect(screen, (32, 42, 68), [0, HEIGHT - 100, WIDTH, 100])
	pygame.draw.rect(screen, 'white', [0, 0, WIDTH, HEIGHT], 5)
	pygame.draw.line(screen, 'white', (250, HEIGHT - 100), (250, HEIGHT), 2)
	pygame.draw.line(screen, 'white', (700, HEIGHT - 100), (700, HEIGHT), 2)
	pygame.draw.line(screen, 'white', (0, HEIGHT - 100), (WIDTH, HEIGHT- 100), 2)
	pygame.draw.rect(screen, 'black', [0, 0, WIDTH, HEIGHT], 2)

	screen.blit(header_font.render(f'Level: {level}', True, 'white'), (10, HEIGHT -75))
	screen.blit(header_font.render(f'"{active_string}"', True, 'white'), (270, HEIGHT -75))
	pause_btn = Button(748, HEIGHT - 52, 'II', False, screen)
	pause_btn.draw()
	screen.blit(banner_font.render(f'Score: {score}', True, 'black'), (250, 10))
	screen.blit(banner_font.render(f'Best: {high_score}', True, 'black'), (550, 10))
	screen.blit(banner_font.render(f'Lives: {lives}', True, 'black'), (10, 10))
	return pause_btn.clicked()

run = True
while run:
	screen.fill('gray')
	timer.tick(fps)
	
	pause_butt = draw_screen()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: run = False

	pygame.display.flip()

pygame.quit()

#https://www.youtube.com/watch?v=3RDMRpUHFBE&t=8s