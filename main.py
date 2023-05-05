import pygame
from random import randint

pygame.init()

# declaring variables
X = 1200
Y = 720
COIN_X = 50
COIN_Y = 40
SB_X = 50
SB_Y = 40
RUN = True
FPS = 30
CLOCK = pygame.time.Clock()

# loading images
BG = pygame.transform.scale(pygame.image.load("assets/images/bg.jpg"),(X,Y))
COIN = pygame.transform.scale(pygame.image.load("assets/images/coin.png"),(COIN_X,COIN_Y))
SB = pygame.transform.scale(pygame.image.load("assets/images/danger.png"),(SB_X,SB_Y))# SB -> Sign Board

# creating the window
WIN = pygame.display.set_mode((X,Y))

pygame.display.set_caption("Car Controlling Game!")

# creating a class 'coin'
class coin:
	
	def __init__(self):
		self.X = randint(0,X-COIN_X)
		self.Y = randint(0,Y-COIN_Y-20)
		self.SPEED = randint(1,20)/40
	
	def fall(self):
		if self.Y >= Y-COIN_Y:
			self.X = randint(0,X-COIN_X)
			self.Y = 0
			self.SPEED = randint(1,20)/40
		WIN.blit(COIN,(self.X,self.Y))
		self.Y += self.SPEED
		# uncomment the next line to view the hitbox of the coin
		#pygame.draw.rect(WIN,(0,255,50),(self.X,self.Y,COIN_X,COIN_Y),1)
		self.SPEED += 0.1

# creating a class 'sb'		
class sb:
	
	def __init__(self):
		self.X = randint(0,X-SB_X)
		self.Y = randint(0,400)
		self.SPEED = randint(1,20)/30
		
	def fall(self):
		if self.Y >= Y-SB_Y:
			self.X = randint(0,X-SB_X)
			self.Y = 0
			self.SPEED = randint(1,20)/30
		WIN.blit(SB,(self.X,self.Y))
		self.Y += self.SPEED
		# uncomment the next line to view the hitbox of the sign board
		#pygame.draw.rect(WIN,(0,255,50),(self.X,self.Y,SB_X,SB_Y),1)
		self.SPEED += 0.15

# creating objects of class 'coin'
COIN1 = coin()
COIN2 = coin()
COIN3 = coin()
COIN4 = coin()
COIN5 = coin()

# creating objects of class 'sb'
SB1 = sb()
SB2 = sb()
SB3 = sb()
SB4 = sb()
SB5 = sb()

def newFrame():
	WIN.fill((0,0,0))
	pygame.draw.rect(WIN,(0,255,0),(0,0,X+3,Y+3),3)
	WIN.blit(BG,(0,0))
	
def displayCoins():
	COIN1.fall()
	COIN2.fall()
	COIN3.fall()
	COIN4.fall()
	COIN5.fall()
	
def displaySignBoards():
	SB1.fall()
	SB2.fall()
	SB3.fall()
	SB4.fall()
	SB5.fall()

def UpdateGameWindow():
	newFrame()
	displayCoins()
	displaySignBoards()
	pygame.display.update()

while RUN:
	CLOCK.tick(FPS)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN = False
			
	UpdateGameWindow()

pygame.quit()