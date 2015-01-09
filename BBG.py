import pygame, sys, random
from AI_Class1 import Ball
#from PlayerBall import PlayerBall

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height

bgcolor= r,b,g=20,20,20

screen = pygame.display.set_mode(size)

#player = PlayerBall([width/2, height/2])

balls = []
balls += [Ball("RSC/AI/images/ai.png", [4,5], [100, 125])]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    if len(balls) < 10:
        if random.randint(0, .25*60) == 0:
            balls += [Ball("RSC/AI/images/ai.png",
                      [random.randint(0,10), random.randint(0,10)],
                      [random.randint(100, width-100), random.randint(100, height-100)])
                      ]
            
    for ball in balls:
        ball.update(width, height)
        
    for bully in balls:
        for victem in balls:
            bully.collideBall(victem)
             
        
	
	for ball in balls:
		if not ball.living:
			balls.remove(ball)
    bgColor = r,g,b
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    #screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
