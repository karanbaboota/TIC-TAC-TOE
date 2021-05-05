import pygame

pygame.init()

#Creating the windoe
window = pygame.display.set_mode((600,400))

#ICON AND CAPTION
pygame.display.set_caption('Tic Tac Toe')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Images of X and O
cross = pygame.image.load('cross.png')
cross = pygame.transform.smoothscale(cross, (77,77))
iconX = pygame.transform.smoothscale(cross, (10,10))

circle = pygame.image.load('circle.png')
circle = pygame.transform.smoothscale(circle, (100,100))
iconO = pygame.transform.smoothscale(circle, (20,20))

#Font
font = pygame.font.Font('/System/Library/Fonts/Supplemental/Comic Sans MS.ttf', 32)

#Initializing basic variables
run = True
X = True
O = False

rec = [None]*9
filled = [False]*9
moves = 0

game = True
win_X = False
win_O = False
tie = False
result = False


def next_chance(X,O):
	if X:
		X = False
		O = True
	else:
		X = True
		O = False

	return X,O

def check(rec):
	if rec[0] == rec[1] == rec[2] and rec[0] is not None:
		return 1
	elif rec[3] == rec[4] == rec[5] and rec[3] is not None:
		return 2
	elif rec[6] == rec[7] == rec[8] and rec[6] is not None:
		return 3
	elif rec[0] == rec[3] == rec[6] and rec[0] is not None:
		return 4
	elif rec[1] == rec[4] == rec[7] and rec[1] is not None:
		return 5
	elif rec[2] == rec[5] == rec[8] and rec[2] is not None:
		return 6
	elif rec[0] == rec[4] == rec[8] and rec[0] is not None:
		return 7
	elif rec[2] == rec[4] == rec[6] and rec[2] is not None:
		return 8

	else:
		return 0

while run:
	window.fill((255,255,255))
	
	if game:
		#RECTANGLES
		rec1 = pygame.draw.rect(window, (255,255,255), (51,22,150,100))
		rec2 = pygame.draw.rect(window, (255,255,255), (201,22,200,100))
		rec3 = pygame.draw.rect(window, (255,255,255), (401,22,150,100))
		rec4 = pygame.draw.rect(window, (255,255,255), (51,122,150,160))
		rec5 = pygame.draw.rect(window, (255,255,255), (201,122,200,160))
		rec6 = pygame.draw.rect(window, (255,255,255), (401,122,150,160))
		rec7 = pygame.draw.rect(window, (255,255,255), (51,282,150,100))
		rec8 = pygame.draw.rect(window, (255,255,255), (201,282,200,100))
		rec9 = pygame.draw.rect(window, (255,255,255), (401,282,150,100))

		#Placing crosses and circles
		if rec[0] == 'X':
			window.blit(cross, (71,32))
		elif rec[0] == 'O':
			window.blit(circle, (61,22))

		if rec[1] == 'X':
			window.blit(cross, (261,32))
		elif rec[1] == 'O':
			window.blit(circle, (251,22))

		if rec[2] == 'X':
			window.blit(cross, (451,32))
		elif rec[2] == 'O':
			window.blit(circle, (441,22))

		if rec[3] == 'X':
			window.blit(cross, (71,162))
		elif rec[3] == 'O':
			window.blit(circle, (61,162))

		if rec[4] == 'X':
			window.blit(cross, (261,162))
		elif rec[4] == 'O':
			window.blit(circle, (251,162))

		if rec[5] == 'X':
			window.blit(cross, (451,162))
		elif rec[5] == 'O':
			window.blit(circle, (441,162))

		if rec[6] == 'X':
			window.blit(cross, (71,292))
		elif rec[6] == 'O':
			window.blit(circle, (61,292))

		if rec[7] == 'X':
			window.blit(cross, (261,292))
		elif rec[7] == 'O':
			window.blit(circle, (251,292))

		if rec[8] == 'X':
			window.blit(cross, (451,292))
		elif rec[8] == 'O':
			window.blit(circle, (441,292))

		#GRID
		pygame.draw.line(window, (0,0,0), (200,22), (200,383))
		pygame.draw.line(window, (0,0,0), (400,22), (400,383))
		pygame.draw.line(window, (0,0,0), (50,122), (550,122))
		pygame.draw.line(window, (0,0,0), (50,282), (550,282))

		#Setting the cursor
		if result == False:
			pygame.mouse.set_visible(False)
			pos = pygame.mouse.get_pos()
			if X:
				window.blit(iconX, (pos[0],pos[1]))			
			elif O: 
				window.blit(iconO, (pos[0],pos[1]))

		#CLICKABLE PART
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN and result == False:
				moves+=1
				pos = pygame.mouse.get_pos()

				if rec1.collidepoint(pos):
					if X and filled[0] == False:
						rec[0] = 'X'
						X,O = next_chance(X,O)
						filled[0] = True

					elif O and filled[0] == False:
						rec[0] = 'O'
						X,O = next_chance(X,O)
						filled[0] = True
				
				if rec2.collidepoint(pos):
					if X and filled[1] == False:
						rec[1] = 'X'
						X,O = next_chance(X,O)
						filled[1] = True

					elif O and filled[1] == False:
						rec[1] = 'O'
						X,O = next_chance(X,O)
						filled[1] = True

				if rec3.collidepoint(pos):
					if X and filled[2] == False:
						rec[2] = 'X'
						X,O = next_chance(X,O)
						filled[2] = True

					elif O and filled[2] == False:
						rec[2] = 'O'
						X,O = next_chance(X,O)
						filled[2] = True

				if rec4.collidepoint(pos):
					if X and filled[3] == False:
						rec[3] = 'X'
						X,O = next_chance(X,O)
						filled[3] = True

					elif O and filled[3] == False:
						rec[3] = 'O'
						X,O = next_chance(X,O)
						filled[3] = True

				if rec5.collidepoint(pos):
					if X and filled[4] == False:
						rec[4] = 'X'
						X,O = next_chance(X,O)
						filled[4] = True

					elif O and filled[4] == False:
						rec[4] = 'O'
						X,O = next_chance(X,O)
						filled[4] = True

				if rec6.collidepoint(pos):
					if X and filled[5] == False:
						rec[5] = 'X'
						X,O = next_chance(X,O)
						filled[5] = True

					elif O and filled[5] == False:
						rec[5] = 'O'
						X,O = next_chance(X,O)
						filled[5] = True

				if rec7.collidepoint(pos):
					if X and filled[6] == False:
						rec[6] = 'X'
						X,O = next_chance(X,O)
						filled[6] = True

					elif O and filled[6] == False:
						rec[6] = 'O'
						X,O = next_chance(X,O)
						filled[6] = True

				if rec8.collidepoint(pos):
					if X and filled[7] == False:
						rec[7] = 'X'
						X,O = next_chance(X,O)
						filled[7] = True

					elif O and filled[7] == False:
						rec[7] = 'O'
						X,O = next_chance(X,O)
						filled[7] = True

				if rec9.collidepoint(pos):
					if X and filled[8] == False:
						rec[8] = 'X'
						X,O = next_chance(X,O)
						filled[8] = True

					elif O and filled[8] == False:
						rec[8] = 'O'
						X,O = next_chance(X,O)
						filled[8] = True

		#Checking for win
		if moves >= 5:
			a = check(rec)

			if a!=0:
				if O:
					win_X = True
				elif X:
					win_O = True

			elif a==0 and moves == 9:
				tie = True

		# X won
		if win_X:
			result = True
			
			if a==1:
				pygame.draw.line(window, (255,0,0), (50,72), (555,72), width = 10)
			elif a==2:
				pygame.draw.line(window, (255,0,0), (50,202), (555,202), width = 10)
			elif a == 3:
				pygame.draw.line(window, (255,0,0), (50,332), (555,332), width = 10)
			elif a==4:
				pygame.draw.line(window, (255,0,0), (110,22), (110,383), width = 10)
			elif a==5:
				pygame.draw.line(window, (255,0,0), (300,22), (300,383), width = 10)
			elif a==6:
				pygame.draw.line(window, (255,0,0), (490,22), (490,383), width = 10)
			elif a==7:
				pygame.draw.line(window, (255,0,0), (20,20), (525,352), width = 10)
			elif a==8:
				pygame.draw.line(window, (255,0,0), (490,22), (80,383), width = 10)

			pygame.mouse.set_visible(True)

			win_box = pygame.draw.rect(window, (255,255,255), (165,100,250,80), border_radius = 50)
			win_box_outline = pygame.draw.rect(window, (255,0,0), (165,100,250,80), 5, border_radius = 50)

			win_text = font.render('X wins!', True, (0,0,0))
			window.blit(win_text, (238,115))

			
			play_again_box = pygame.draw.rect(window, (255,255,255), (165,250,250,80), border_radius = 50)
			play_again_box_outline = pygame.draw.rect(window, (255,0,0), (165,250,250,80), 5, border_radius = 50)
			
			hover_pos = pygame.mouse.get_pos()
			if play_again_box.collidepoint(hover_pos):
				play_again_box = pygame.draw.rect(window, (240,240,240), (165,250,250,80), border_radius = 50)
				play_again_box_outline = pygame.draw.rect(window, (255,0,0), (165,250,250,80), 5, border_radius = 50)

			play_again_text = font.render('Play again', True, (0,0,0))
			window.blit(play_again_text, (218,265))

			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					if play_again_box.collidepoint(pos):
						#Resetting the parameters
						win_X = False
						win_O = False
						tie = False
						result = False
						X = True
						O = False
						rec = [None]*9					
						filled = [False]*9		
						moves = 0


		#O won
		if win_O:
			result = True

			if a==1:
				pygame.draw.line(window, (255,0,0), (50,72), (555,72), width = 10)
			elif a==2:
				pygame.draw.line(window, (255,0,0), (50,202), (555,202), width = 10)
			elif a == 3:
				pygame.draw.line(window, (255,0,0), (50,332), (555,332), width = 10)
			elif a==4:
				pygame.draw.line(window, (255,0,0), (110,22), (110,383), width = 10)
			elif a==5:
				pygame.draw.line(window, (255,0,0), (300,22), (300,383), width = 10)
			elif a==6:
				pygame.draw.line(window, (255,0,0), (490,22), (490,383), width = 10)
			elif a==7:
				pygame.draw.line(window, (255,0,0), (20,20), (525,352), width = 10)
			elif a==8:
				pygame.draw.line(window, (255,0,0), (490,22), (80,383), width = 10)

			pygame.mouse.set_visible(True)

			win_box = pygame.draw.rect(window, (255,255,255), (165,100,250,80), border_radius = 50)
			win_box_outline = pygame.draw.rect(window, (255,0,0), (165,100,250,80), 5, border_radius = 50)

			win_text = font.render('O wins!', True, (0,0,0))
			window.blit(win_text, (238,115))

			
			play_again_box = pygame.draw.rect(window, (255,255,255), (165,250,250,80), border_radius = 50)
			play_again_box_outline = pygame.draw.rect(window, (255,0,0), (165,250,250,80), 5, border_radius = 50)
			
			hover_pos = pygame.mouse.get_pos()
			if play_again_box.collidepoint(hover_pos):
				play_again_box = pygame.draw.rect(window, (240,240,240), (165,250,250,80), border_radius = 50)
				play_again_box_outline = pygame.draw.rect(window, (255,0,0), (165,250,250,80), 5, border_radius = 50)

			play_again_text = font.render('Play again', True, (0,0,0))
			window.blit(play_again_text, (218,265))

			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					if play_again_box.collidepoint(pos):
						#Resetting the parameters
						win_X = False
						win_O = False
						tie = False
						result = False
						X = True
						O = False
						rec = [None]*9					
						filled = [False]*9		
						moves = 0


		#Tie
		if tie:
			result = True
			pygame.mouse.set_visible(True)

			win_box = pygame.draw.rect(window, (255,255,255), (165,100,250,80), border_radius = 50)
			win_box_outline = pygame.draw.rect(window, (255,0,0), (165,100,250,80), 5, border_radius = 50)

			win_text = font.render('Game tied!', True, (0,0,0))
			window.blit(win_text, (210,115))

			
			play_again_box = pygame.draw.rect(window, (255,255,255), (165,250,250,80), border_radius = 50)
			play_again_box_outline = pygame.draw.rect(window, (255,0,0), (165,250,250,80), 5, border_radius = 50)
			
			hover_pos = pygame.mouse.get_pos()
			if play_again_box.collidepoint(hover_pos):
				play_again_box = pygame.draw.rect(window, (240,240,240), (165,250,250,80), border_radius = 50)
				play_again_box_outline = pygame.draw.rect(window, (255,0,0), (165,250,250,80), 5, border_radius = 50)

			play_again_text = font.render('Play again', True, (0,0,0))
			window.blit(play_again_text, (218,265))

			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					if play_again_box.collidepoint(pos):
						#Resetting the parameters
						win_X = False
						win_O = False
						tie = False
						result = False
						X = True
						O = False
						rec = [None]*9					
						filled = [False]*9		
						moves = 0


	pygame.display.update()