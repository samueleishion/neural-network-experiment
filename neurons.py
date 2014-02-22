import random 
from graphics import * 
from time import sleep 

class Neuron: 
	def __init__(self,x,y,neuron_type,weight): 
		self.x = x 
		self.y = y 
		self.t = neuron_type 
		self.w = weight 
		self.axons = [] 

	def draw(self,win): 
		point = Point(self.x,self.y) 
		self.circle = Circle(point,20) 

		if(self.t==0): 
			self.circle.setOutline(color_rgb(150,0,0)) 
		elif(self.t==2): 
			self.circle.setOutline(color_rgb(0,0,150)) 

		self.circle.draw(win) 

	def radius(self): 
		return self.circle.getRadius() 

	def center(self): 
		return self.circle.getCenter() 

	def getX(self): 
		return self.circle.getCenter().getX() 

	def getY(self): 
		return self.circle.getCenter().getY() 

	def get_coords(self): 
		return self.getX(),self.getY() 

	def is_sensorial(self): 
		return self.t==0 

	def is_transmitter(self): 
		return self.t==1 

	def is_terminal(self): 
		return self.t==2 

	def get_color(self,gb):
		if(self.is_sensorial()):
			return color_rgb(255,gb,gb) 
		elif(self.is_terminal()):
			return color_rgb(gb,gb,255) 
		else:
			return color_rgb(255,255,gb) 

	def light_up(self): 
		gb = 0
		self.circle.setFill(self.get_color(gb)) 

		if(not self.is_terminal()):
			for i in range(len(self.axons)): 
				rand = random.randint(0,1)
				transmission = random.uniform(0.7,1.3) 
				if(rand==0): 
					# print "neuron sending "+str(transmission*self.w)
					self.axons[i].send(transmission*self.w)  
				# else: 
					# print "neuron didn't send anything"

		while(gb<=255):
			self.circle.setFill(self.get_color(gb)) 
			sleep(0.03) 
			gb += 51 

	def axon(self,other,win):
		self.axons.append(other) 
		ox,oy = other.get_coords() 
		tx,ty = self.get_coords() 

		p1 = Point(tx,ty) 
		p2 = Point(ox,oy) 

		line = Line(p1,p2) 
		line.setFill(color_rgb(200,200,200)) 
		line.draw(win) 

	def send(self,transmission): 
		# print "my weight: "+str(self.w) 
		if(transmission>0.001): 
			self.light_up() 
