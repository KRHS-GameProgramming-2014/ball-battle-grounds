import pygame

class Player():
    def __init__(self, pnum, screensize):
		if pnum == 1:
			pos = [100,100]
			self.upImages = [pygame.image.load("rsc/Player/MU.png"),
                             pygame.image.load("rsc/Player/MU2.png")]
			self.downImages = [pygame.image.load("rsc/Player/MD.png"),
							   pygame.image.load("rsc/Player/MD2.png")]
			self.leftImages = [pygame.image.load("rsc/Player/ML.png"),
							   pygame.image.load("rsc/Player/ML2.png")]
			self.rightImages = [pygame.image.load("rsc/Player/MR.png"),
								pygame.image.load("rsc/Player/MR2.png")]
			self.facing = "right"
			self.images = self.rightImages
		else:
			pos = [screensize[0]-100, screensize[1]-100]
			self.upImages = [pygame.image.load("rsc/Player/MU.png"),
							 pygame.image.load("rsc/Player/MU2.png")]
			self.downImages = [pygame.image.load("rsc/Player/MD.png"),
							   pygame.image.load("rsc/Player/MD2.png")]
			self.leftImages = [pygame.image.load("rsc/Player/ML.png"),
							   pygame.image.load("rsc/Player/ML2.png")]
			self.rightImages = [pygame.image.load("rsc/Player/MR.png"),
								pygame.image.load("rsc/Player/MR2.png")]
			self.facing = "left"
			self.images = self.leftImages
        
			self.changed = False
        
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.maxSpeed = 10
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.gusting = False
        self.gustCount = 0
        self.maxGustCount = 10
        self.belchCoolDown = 0
        self.belchCoolDownMax = 100
        self.radius = 20
        self.didBounceX = False
        self.didBounceY = False
        self.health = 20
        self.maxHealth = 20
        self.nodamage = 0
        self.living = True
        
    
    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)
        self.animate()
        self.facingChanged = False
   
    def move(self):
        self.rect = self.rect.move(self.speed)
        
        if 0 < self.gustCount < self.maxGustCount:
            self.gustCount += 1
            self.gust.go(self)
        elif self.gustCount >= self.maxGustCount:
            self.gustCount = 0
            self.gusting = False
        
    def attack(self, atk):
        if atk == "gust" and self.gustCount == 0 and self.gustCoolDown == 0:
			self.gusting = True
			self.gust.go(self)
			self.belchCount += 1

    def collideWall(self, width, height):
        if not self.didBounceX:
          
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = 0
                self.didBounceX = True
              
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = 0
                self.didBounceY = True
            
    
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.facingChanged = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        
        if self.changed:    
            if self.facing == "up":
                self.images = self.upImages
            elif self.facing == "down":
                self.images = self.downImages
            elif self.facing == "right":
                self.images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.facing = "left"
            self.changed = TrueQ
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0

"""
class PlayerBall(Ball):
	def __init__(self, pos):
		Ball.__init__(self, "images/Player/pballbu.png", [0,0], pos)
		self.upImages = [pygame.image.load("images/Player/pballru.png"),
						 pygame.image.load("images/Player/pballgu.png"),
						 pygame.image.load("images/Player/pballbu.png")]
		self.downImages = [pygame.image.load("images/Player/pballrd.png"),
						   pygame.image.load("images/Player/pballgd.png"),
						   pygame.image.load("images/Player/pballbd.png")]
		self.leftImages = [pygame.image.load("images/Player/pballrl.png"),
						   pygame.image.load("images/Player/pballgl.png"),
						   pygame.image.load("images/Player/pballbl.png")]
		self.rightImages = [pygame.image.load("images/Player/pballrr.png"),
						    pygame.image.load("images/Player/pballgr.png"),
						    pygame.image.load("images/Player/pballbr.png")]
		self.facing = "up"
		self.changed = False
		self.images = self.upImages
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.25
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 10
			
	def update(self, width, height):
		Ball.update(self, width, height)
		self.animate()
		self.Changed = False
		
	def collideWall(self, width, height):
		if not self.didBounceX:
			
			if self.rect.left < 0 or self.rect.right > width:
				self.speedx = 0
				self.didBounceX = True
				
		if not self.didBounceY:
			if self.rect.top < 0 or self.rect.bottom > height:
				self.speedy = 0
				self.didBounceY = True
				
	
	def animate(self):
		if self.waitCount < self.maxWait:
			self.waitCount += 1
		else:
			self.waitCount = 0
			self.facingChanged = True
			if self.frame < self.maxFrame:
				self.frame += 1
			else:
				self.frame = 0
		
		if self.changed:	
			if self.facing == "up":
				self.images = self.upImages
			elif self.facing == "down":
				self.images = self.downImages
			elif self.facing == "right":
				self.images = self.rightImages
			elif self.facing == "left":
				self.images = self.leftImages
			
			self.image = self.images[self.frame]
	
	def go(self, direction):
		if direction == "up":
			self.facing = "up"
			self.changed = True
			self.speedy = -self.maxSpeed
		elif direction == "stop up":
			self.speedy = 0
		elif direction == "down":
			self.facing = "down"
			self.changed = True
			self.speedy = self.maxSpeed
		elif direction == "stop down":
			self.speedy = 0
			
		if direction == "right":
			self.facing = "right"
			self.changed = True
			self.speedx = self.maxSpeed
		elif direction == "stop right":
			self.speedx = 0
		elif direction == "left":
			self.facing = "left"
			self.changed = True
			self.speedx = -self.maxSpeed
		elif direction == "stop left":
			self.speedx = 0
"""
