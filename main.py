import pygame
from random import randint

pygame.init()

# a function to set the high score
def setHighScore(newHighScore):
	global HIGH_SCORE
	HIGH_SCORE = newHighScore
	FILE = open("assets/HighScore.txt",'w')
	FILE.write(str(newHighScore))
	FILE.close()

# a function to get the high score
def getHighScore():
	global HIGH_SCORE
	try:
		FILE = open("assets/HighScore.txt",'r')
		HIGH_SCORE = int(FILE.read())
		FILE.close()
	except:
		FILE = open("assets/HighScore.txt",'w')
		FILE.write('0')
		FILE.close()
		FILE = open("assets/HighScore.txt",'r')
		HIGH_SCORE = int(FILE.read())
		FILE.close()
	
getHighScore()

# declaring variables
X = 1200
Y = 720
COIN_X = 50
COIN_Y = 40
SB_X = 50
SB_Y = 40
CAR_X = 200
CAR_Y = 100
HEAD_X = 100
HEAD_Y = 100
WHEEL_X = 40
WHEEL_Y = 40
CONTROL_R_X = 150
CONTROL_R_Y = 105
CONTROL_L_X = 150
CONTROL_L_Y = 105
CONTROL_B_X = 90
CONTROL_B_Y = 130
RUN = True
FPS = 50
CLOCK = pygame.time.Clock()
SCORE = 0
FONT = pygame.font.SysFont("georgia",70,True)
SCORE_TEXT = FONT.render(f"Score : {SCORE}",10,(205,156,201))
FONT2 = pygame.font.SysFont("georgia",10,True)
DEVELOPER_TEXT = FONT2.render("Developed By Omanshu",10,(0,50,255))
FONT3 = pygame.font.SysFont("georgia",30,True)
HIGH_SCORE_TEXT = FONT3.render(f"High Score : {HIGH_SCORE}",10,(160,120,220))

# loading images
BG = pygame.transform.scale(pygame.image.load("assets/images/bg.jpg"),(X,Y))
COIN = pygame.transform.scale(pygame.image.load("assets/images/coin.png"),(COIN_X,COIN_Y))
SB = pygame.transform.scale(pygame.image.load("assets/images/danger.png"),(SB_X,SB_Y))# SB -> Sign Board
CAR_RIGHT = pygame.transform.scale(pygame.image.load("assets/images/carRight.png"),(CAR_X,CAR_Y))
CAR_LEFT = pygame.transform.scale(pygame.image.load("assets/images/carLeft.png"),(CAR_X,CAR_Y))
HEAD_RIGHT = pygame.transform.scale(pygame.image.load("assets/images/headRight.png"),(HEAD_X,HEAD_Y))
HEAD_LEFT = pygame.transform.scale(pygame.image.load("assets/images/headLeft.png"),(HEAD_X,HEAD_Y))
WHEEL = pygame.transform.scale(pygame.image.load("assets/images/wheel.png"),(WHEEL_X,WHEEL_Y))
CONTROL_R = pygame.transform.scale(pygame.image.load("assets/images/right.png"),(CONTROL_R_X,CONTROL_R_Y))
CONTROL_L = pygame.transform.scale(pygame.image.load("assets/images/left.png"),(CONTROL_L_X,CONTROL_L_Y))
CONTROL_B = pygame.transform.scale(pygame.image.load("assets/images/break.png"),(CONTROL_B_X,CONTROL_B_Y))

# loading audios
ENGINE_SOUND = pygame.mixer.Sound("assets/audios/EngineSound.ogg")
COIN_SOUND = pygame.mixer.Sound("assets/audios/Coin.wav")

# creating the window
WIN = pygame.display.set_mode((X,Y))

# setting the caption of the window
pygame.display.set_caption("Highway Heist!")

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
		self.SPEED = randint(1,20)/20
		
	def fall(self):
		if self.Y >= Y-SB_Y:
			self.X = randint(0,X-SB_X)
			self.Y = 0
			self.SPEED = randint(1,20)/20
		WIN.blit(SB,(self.X,self.Y))
		self.Y += self.SPEED
		# uncomment the next line to view the hitbox of the sign board
		#pygame.draw.rect(WIN,(0,255,50),(self.X,self.Y,SB_X,SB_Y),1)
		self.SPEED += 0.15

# creating a class 'car'		
class car:
	
	def __init__(self):
		self.X = 0
		self.Y = 470
		self.LEFT = False
		self.RIGHT = False
		self.SPEED = 10
		self.PREV = "RIGHT"
		self.ANGLE = 10
		self.WHEEL = pygame.transform.scale(pygame.transform.rotate(WHEEL,0),(WHEEL_X,WHEEL_Y))
		self.SOUND_TIMER = 0
		
	def move(self):
		global WHEEL
		if self.RIGHT:
			if self.SOUND_TIMER == 0:
				ENGINE_SOUND.play()
				self.SOUND_TIMER = 5
			self.SOUND_TIMER -= 1
			self.PREV = "RIGHT"
			WIN.blit(CAR_RIGHT,(self.X,self.Y))
			WIN.blit(pygame.transform.rotate(WHEEL,self.ANGLE),(self.X+20,self.Y+65))
			WIN.blit(pygame.transform.rotate(WHEEL,self.ANGLE),(self.X+123,self.Y+65))
			WIN.blit(HEAD_RIGHT,(self.X+27,self.Y-35))
			if self.X <= X-CAR_X:
				if self.ANGLE <= 0:
					self.ANGLE = 360
				else:
					self.ANGLE -= 10
				self.X += self.SPEED
		elif self.LEFT:
			if self.SOUND_TIMER == 0:
				ENGINE_SOUND.play()
				self.SOUND_TIMER = 5
			self.SOUND_TIMER -= 1
			self.PREV = "LEFT"
			WIN.blit(CAR_LEFT,(self.X,self.Y))
			WIN.blit(pygame.transform.rotate(WHEEL,self.ANGLE),(self.X+37,self.Y+65))
			WIN.blit(pygame.transform.rotate(WHEEL,self.ANGLE),(self.X+140,self.Y+65))
			WIN.blit(HEAD_LEFT,(self.X+75,self.Y-35))
			if self.X >= 0:
				if self.ANGLE >= 360:
					self.ANGLE = 0
				else:
					self.ANGLE += 10
				self.X -= self.SPEED
		else:
			if self.PREV == "RIGHT":
				WIN.blit(CAR_RIGHT,(self.X,self.Y))
				WIN.blit(pygame.transform.rotate(WHEEL,self.ANGLE),(self.X+20,self.Y+65))
				WIN.blit(pygame.transform.rotate(WHEEL,self.ANGLE),(self.X+123,self.Y+65))
				WIN.blit(HEAD_RIGHT,(self.X+27,self.Y-35))
			else:
				WIN.blit(CAR_LEFT,(self.X,self.Y))
				WIN.blit(pygame.transform.rotate(WHEEL,self.ANGLE),(self.X+37,self.Y+65))
				WIN.blit(pygame.transform.rotate(WHEEL,self.ANGLE),(self.X+140,self.Y+65))
				WIN.blit(HEAD_LEFT,(self.X+75,self.Y-35))

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

# creating an object of class 'car'
CAR1 = car()

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
	
def displayControlsAndText():
	global SCORE_TEXT
	WIN.blit(CONTROL_L,(100,580))
	WIN.blit(CONTROL_R,(970,580))
	WIN.blit(CONTROL_B,(550,580))
	SCORE_TEXT = FONT.render(f"Score : {SCORE}",10,(205,156,201))
	WIN.blit(SCORE_TEXT,(810,30))
	WIN.blit(DEVELOPER_TEXT,(10,10))
	HIGH_SCORE_TEXT = FONT3.render(f"High Score : {HIGH_SCORE}",10,(160,120,220))
	WIN.blit(HIGH_SCORE_TEXT,(840,5))
	
def checkEvents():
	global RUN
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			MX,MY = pygame.mouse.get_pos()
			if MX >= 90 and MX <= 260 and MY >= 570 and MY <= 700:
				CAR1.RIGHT = False
				CAR1.LEFT = True
			elif MX >= 960 and MX <= 1130 and MY >= 570 and MY <= 700:
				CAR1.LEFT = False
				CAR1.RIGHT = True
			elif MX >= 540 and MX <= 650 and MY >= 570 and MY <= 720:
				CAR1.LEFT = False
				CAR1.RIGHT = False
				
def checkCollision():
	global SCORE
	if COIN1.Y >= CAR1.Y and COIN1.Y+COIN_Y <= CAR1.Y+CAR_Y and COIN1.X >= CAR1.X and COIN1.X <= CAR1.X+CAR_X:
		COIN_SOUND.play()
		SCORE += 10
		COIN1.Y = 0
		COIN1.X = randint(0,X-COIN_X)
	if COIN2.Y >= CAR1.Y and COIN2.Y+COIN_Y <= CAR1.Y+CAR_Y and COIN2.X >= CAR1.X and COIN2.X <= CAR1.X+CAR_X:
		COIN_SOUND.play()
		SCORE += 10
		COIN2.Y = 0
		COIN2.X = randint(0,X-COIN_X)
	if COIN3.Y >= CAR1.Y and COIN3.Y+COIN_Y <= CAR1.Y+CAR_Y and COIN3.X >= CAR1.X and COIN3.X <= CAR1.X+CAR_X:
		COIN_SOUND.play()
		SCORE += 10
		COIN3.Y = 0
		COIN3.X = randint(0,X-COIN_X)
	if COIN4.Y >= CAR1.Y and COIN4.Y+COIN_Y <= CAR1.Y+CAR_Y and COIN4.X >= CAR1.X and COIN4.X <= CAR1.X+CAR_X:
		COIN_SOUND.play()
		SCORE += 10
		COIN4.Y = 0
		COIN4.X = randint(0,X-COIN_X)
	if COIN5.Y >= CAR1.Y and COIN5.Y+COIN_Y <= CAR1.Y+CAR_Y and COIN5.X >= CAR1.X and COIN5.X <= CAR1.X+CAR_X:
		COIN_SOUND.play()
		SCORE += 10
		COIN5.Y = 0
		COIN5.X = randint(0,X-COIN_X)
	if SB1.Y >= CAR1.Y and SB1.Y+SB_Y <= CAR1.Y+CAR_Y and SB1.X >= CAR1.X and SB1.X <= CAR1.X+CAR_X:
		SCORE -= 50
		SB1.Y = 0
		SB1.X = randint(0,X-SB_X)
	if SB2.Y >= CAR1.Y and SB2.Y+SB_Y <= CAR1.Y+CAR_Y and SB2.X >= CAR1.X and SB2.X <= CAR1.X+CAR_X:
		SCORE -= 50
		SB2.Y = 0
		SB2.X = randint(0,X-SB_X)
	if SB3.Y >= CAR1.Y and SB3.Y+SB_Y <= CAR1.Y+CAR_Y and SB3.X >= CAR1.X and SB3.X <= CAR1.X+CAR_X:
		SCORE -= 50
		SB3.Y = 0
		SB3.X = randint(0,X-SB_X)
	if SB4.Y >= CAR1.Y and SB4.Y+SB_Y <= CAR1.Y+CAR_Y and SB4.X >= CAR1.X and SB4.X <= CAR1.X+CAR_X:
		SCORE -= 50
		SB4.Y = 0
		SB4.X = randint(0,X-SB_X)
	if SB5.Y >= CAR1.Y and SB5.Y+SB_Y <= CAR1.Y+CAR_Y and SB5.X >= CAR1.X and SB5.X <= CAR1.X+CAR_X:
		SCORE -= 50
		SB5.Y = 0
		SB5.X = randint(0,X-SB_X)
	if SCORE > HIGH_SCORE:
		setHighScore(SCORE)

def UpdateGameWindow():
	newFrame()
	displayCoins()
	displaySignBoards()
	CAR1.move()
	displayControlsAndText()
	pygame.display.update()

while RUN:
	CLOCK.tick(FPS)
	checkEvents()
	checkCollision()
	UpdateGameWindow()

pygame.quit()
# Developed By Omanshu