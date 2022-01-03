import tkinter as tk
import turtle as t

class Grid(tk.Canvas):
	def __init__(self, parent, rows, cols, width, height, margin=100, **kwargs):
		tk.Canvas.__init__(self, parent, width=width + margin,height=height + margin, **kwargs)
		self.margin = margin
		self.height = height
		self.width = width
		self.rows = rows
		self.cols = cols
		self.screen = t.TurtleScreen(self)
		self.screen.tracer(0,0)
		self.screen.bgcolor("black")
		self.turt = t.RawTurtle(self.screen)
		self.turt.hideturtle()
		self.drawGrid()
		
	def drawGrid(self, clear=True):
		if clear:
			self.turt.clear()
		
		self.turt.color("black")
		x = -self.width/2
		y = self.height/2
		cell_width = self.width/self.cols
		cell_height = self.height/self.rows
		
		#rows
		for i in range(self.rows + 1):
			self.turt.penup()
			self.turt.goto(x,y - i * cell_height)
			self.turt.pendown()
			self.turt.goto(x + self.width, y - i * cell_height)
		
		#rows
		for j in range(self.cols + 1):
			self.turt.penup()
			self.turt.goto(x + j * cell_width,y)
			self.turt.pendown()
			self.turt.goto(x + j * cell_width, y - self.height)
			
		self.screen.update()

class ColorGrid(Grid):
	def __init__(self, parent, rows, cols, width, height,**kwargs):
		super().__init__(parent, rows, cols, width, height,**kwargs)
		self.COLORS = {" ":"black","R":"red", "B":"blue", "G":"green", "O":"orange", "Y":"yellow", "W":"white",
					   "red":"red", "blue":"blue", "green":"green", "orange":"orange", "yellow":"yellow", "white":"white"}
	
	def render(self, data):
		self.drawGrid()
		for i in range(self.rows):
			for j in range(self.cols):
				self.renderCell(i,j, data[i][j])
		self.screen.update()
	
	def renderCell(self,row,col, color):
		x = -self.width/2
		y = self.height/2
		cell_width = self.width/self.cols
		cell_height = self.height/self.rows
				
		p = (x + col * cell_width, y - row * cell_height)
		self.drawCell(p, cell_width, cell_height, self.COLORS[color])
		
		
		
	def drawCell(self,position, cell_width, cell_height, color_string):
		self.turt.penup()
		self.turt.goto(position)
		self.turt.pendown()
		self.turt.color(color_string)
		self.turt.begin_fill()
		dimensions = [cell_width,cell_height]
		for i in range(4):
			self.turt.forward(dimensions[i % 2])
			self.turt.right(90)
		self.turt.end_fill()
		
		self.turt.penup()
		self.turt.goto(position)
		self.turt.pendown()
		self.turt.color("black")
		dimensions = [cell_width,cell_height]
		for i in range(4):
			self.turt.forward(dimensions[i % 2])
			self.turt.right(90)