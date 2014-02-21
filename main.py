from graphics import * 

win = GraphWin("NeuralNetworkGraph",600,600) 
neurons = [] 

def was_click_perceived(x,y): 
	for i in range(len(neurons)): 
		nr = neurons[i].getRadius()
		nc = neurons[i].getCenter() 
		nx = nc.getX() 
		ny = nc.getY() 

		if (( nx-nr <= x <= nx+nr ) and ( ny-nr <= y <= ny+nr )):
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

	# draw sensorial neurons 
	interval = (win.getWidth()-(margin))/sensorials 
	x = margin*2
	y = 50 

	for i in range(sensorials): 
		point = Point(x,y) 
		circle = Circle(point,20) 
		circle.draw(win) 
		neurons.append(circle) 
		x = x+interval 

	# draw terminal neurons 
	interval = (win.getWidth()-(margin))/terminals 
	x = margin*2
	y = win.getHeight()-40 
	for i in range(terminals): 
		point = Point(x,y) 
		circle = Circle(point,20) 
		circle.draw(win) 
		neurons.append(circle) 
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