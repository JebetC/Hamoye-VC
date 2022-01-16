import pygame
pygame.init()

win = pygame.display.set_mode((600,600))

pygame.display.set_caption("My first pygame.")

screenwidth = 600
x=60
y=60
width=40
height=30
vel = 5

isJump = True
jumpCount = 10
run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False


	

	
	keys =pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > vel:
		x-=vel
	if keys[pygame.K_RIGHT] and x < (screenwidth-width-vel):
		x+=vel
	if not(isJump):
		if keys[pygame.K_LEFT] and y>vel:
			y-=vel
		if keys[pygame.K_RIGHT] and y <(screenwidth-height-vel):
			y+=vel
		if keys[pygame.K_SPACE]:
			isJump = True
	else:
		if jumpCount >=-10:
			neg = 1
			y-=(jumpCount*2)*0.5
			jumpCount-=1
		else:
			isJump=False
			jumpCount=10
    	 

   	


	win.fill((0,0,0))

	pygame.draw.rect(win,(0,255,0),(x,y,width,height))
	pygame.display.update()

pygame.quit()