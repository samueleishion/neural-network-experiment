import random 
from graphics import * 
from neurons import * 

WINDOW_X = 600 
WINDOW_Y = 600 
SENSORY_NEURONS = 5
TERMINAL_NEURONS = 6

## ===================================
## 	NO NEED TO EDIT BEYOND THIS POINT 
## ===================================

SENSORIAL = 0 
TRANSMITTER = 1 
TERMINAL = 2 

win = GraphWin("NeuralNetworkGraph",WINDOW_X,WINDOW_Y) 
brain = [] 

def was_click_perceived(x,y): 
	for i in range(len(brain)): 
		nr = brain[i].radius() 
		nx,ny = brain[i].get_coords()  

		if (( nx-nr <= x <= nx+nr ) and ( ny-nr <= y <= ny+nr )):
			if (brain[i].is_sensorial()):
				brain[i].light_up() 
				# print "neuron "+str(i+1)+" perceived something!"
				return True

	# print "no neuron perceived anything =(" 
	return False 

def get_click(): 
	click = win.getMouse() 
	x = click.getX() 
	y = click.getY() 
	point = Point(x,y) 
	point.draw(win) 
	return x,y

def connect_neurons(sensorials,terminals): 
	transmitters = len(brain)-sensorials-terminals 

	for i in range(sensorials): 
		for j in range(transmitters):
			rand = random.randint(0,2) 
			if(rand==2):
				brain[i].axon(brain[sensorials+j],win) 

	base = sensorials+transmitters
	for i in range(transmitters): 
		for j in range(terminals): 
			rand = random.randint(0,5) 
			if(rand==0): 
				brain[sensorials+i].axon(brain[base+j],win) 
	

def draw_neurons(sensorials,terminals): 
	margin = 30 
	space = win.getWidth()-margin

	# draw sensorial neurons 
	interval = space/sensorials 
	x = margin*2 
	y = 50 
	for i in range(sensorials): 
		weight = random.uniform(0.0,1.0) 
		neuron = Neuron(x,y,SENSORIAL,weight,i+1) 
		neuron.draw(win) 
		brain.append(neuron) 
		x = x+interval 

	# draw transmitter neurons 
	transmitters = sensorials+terminals 
	interval = space/transmitters 
	for i in range(transmitters): 
		x = random.randint(margin,win.getWidth()-margin) 
		y = random.randint(100,win.getHeight()-80)
		weight = random.uniform(0.0,1.0)
		neuron = Neuron(x,y,TRANSMITTER,weight) 
		neuron.draw(win) 
		brain.append(neuron) 

	# draw terminal neurons 
	interval = space/terminals 
	x = margin*2 
	y = win.getHeight()-40 
	for i in range(terminals): 
		weight = random.uniform(0.0,2.0) 
		neuron = Neuron(x,y,TERMINAL,weight,i+1) 
		neuron.draw(win) 
		brain.append(neuron) 
		x = x+interval 

	connect_neurons(sensorials,terminals) 


def main(): 
	draw_neurons(SENSORY_NEURONS,TERMINAL_NEURONS) 
	while(True): 
		click = get_click() 
		was_click_perceived(click[0],click[1]) 

	win.close() 

main() 
