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
			print "neuron "+str(i)+" perceived something!"
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

def draw_neuron(): 
	point = Point(200,200) 
	circle = Circle(point,20) 
	circle.draw(win) 
	neurons.append(circle) 

	point = Point(330,430) 
	circle = Circle(point,20) 
	circle.draw(win) 
	neurons.append(circle) 

	point = Point(120,540) 
	circle = Circle(point,20) 
	circle.draw(win) 
	neurons.append(circle) 

def main(): 
	point = Point(300,300) 
	point.draw(win) 

	draw_neuron() 
	while(True): 
		click = get_click() 
		was_click_perceived(click[0],click[1]) 

	win.close() 

main() 