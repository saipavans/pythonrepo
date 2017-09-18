import turtle

def draw_polygon(turtle_obj, length, number_of_sides):
	angle=360/number_of_sides
	for i in range (number_of_sides):
		turtle_obj.fd(length)
		turtle_obj.lt(angle)

def draw_circle(turtle_obj, radius):
	sides = 100
	length = (int) (2 * 3.14 * radius)
	draw_polygon(turtle_obj, radius, sides)

def draw_circle_refined(turtle_obj, radius, arc_angle):
	sides=100
	sides_refined=(int) ((arc_angle/360) * sides)
	angle=360/sides
	length = (int) (2 * 3.14 * radius)
	for i in range(sides_refined):
		turtle_obj.fd(length)
		turtle_obj.lt(angle)


turtle_handle = turtle.Turtle()
turtle_handle.delay=10000
#draw_polygon(turtle_handle,200,5)
draw_circle_refined(turtle_handle, 1, 180)


turtle.mainloop()


