from graphics import * 

class Neuron: 
	def __init__(self,x,y,neuron_type,weight): 
		self.x = x 
		self.y = y 
		self.t = neuron_type 
		self.w = weight 

	def draw(self,win): 
		point = Point(self.x,self.y) 
		self.circle = Circle(point,20) 
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