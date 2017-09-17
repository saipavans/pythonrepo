width = 4
rows = 2
columns = 2

def draw_grid(rows, columns):
	horizontalLine = ("+" + ("-" * width)) * columns + "+" + "\n"
	verticalLinePart = (((("/" + " " * width)) * columns + "/") + "\n")*width
	output = ((horizontalLine + (verticalLinePart)) * rows) + horizontalLine 
	print(output)

draw_grid(4,4)  
