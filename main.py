import random 
from graphics import * 
from neurons import * 

SENSORIAL = 0 
TRANSMITTER = 1 
TERMINAL = 2 

win = GraphWin("NeuralNetworkGraph",600,600) 
brain = [] 

def was_click_perceived(x,y): 
	for i in range(len(brain)): 
		nr = brain[i].radius() 
		nx,ny = brain[i].get_coords()  

		if (( nx-nr <= x <= nx+nr ) and ( ny-nr <= y <= ny+nr )):
			if (brain[i].is_sensorial()):
				print "neuron "+str(i+1)+" perceived something!"
				return True

	print "no neuron perceived anything =(" 
	return False 

def get_click(): 
	click = win.getMouse() 
	x = click.getX() 
	y = click.getY() 
	point = Point(x,y) 
	point.draw(win) 
	return x,y

def draw_neurons(sensorials,terminals): 
	margin = 30 
	space = win.getWidth()-margin

	# draw sensorial neurons 
	interval = space/sensorials 
	x = margin*2 
	y = 50 
	for i in range(sensorials): 
		weight = random.uniform(0.0,1.0) 
		neuron = Neuron(x,y,SENSORIAL,weight) 
		neuron.draw(win) 
		brain.append(neuron) 
		x = x+interval 

	# draw terminal neurons 
	interval = space/terminals 
	x = margin*2 
	y = win.getHeight()-40 
	for i in range(terminals): 
		weight = random.uniform(0.0,1.0) 
		neuron = Neuron(x,y,TERMINAL,weight) 
		neuron.draw(win) 
		brain.append(neuron) 
		x = x+interval 


def main(): 
	point = Point(300,300) 
	point.draw(win) 

	draw_neurons(5,6) 
	while(True): 
		click = get_click() 
		was_click_perceived(click[0],click[1]) 

	win.close() 

main() 