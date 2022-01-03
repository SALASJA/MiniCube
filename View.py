import tkinter as tk
import turtle as t
from Grid import ColorGrid


class MiniCubeCanvas(tk.Frame):
	def __init__(self, parent = None, **kwargs):
		super().__init__(parent)
		self.top_canvas = ColorGrid(self,4,4, 200, 200)
		self.top_canvas.pack()
		self.bottom_canvas = ColorGrid(self,4,4, 200, 200)
		self.bottom_canvas.pack()
		
	def render(self, data, top = True):
		if top:
			self.top_canvas.render(data)
		else:
			self.bottom_canvas.render(data)
	
class View:
	def __init__(self, parent):
		self.canvas = MiniCubeCanvas(parent)
		self.canvas.pack()
		self.var = tk.StringVar()
		self.entry = tk.Entry(parent, textvariable = self.var)
		self.entry.pack(fill=tk.X,anchor=tk.W)
		frame = tk.Frame(parent)
		self.execute = tk.Button(frame, text="Execute")
		self.execute.pack(side=tk.LEFT)
		self.undo = tk.Button(frame, text="Undo")
		self.undo.pack(side=tk.LEFT)
		self.reset = tk.Button(frame, text="Reset")
		self.reset.pack(side=tk.LEFT)
		self.reload_algorithms = tk.Button(frame, text="Reload Algorithms file")
		self.reload_algorithms.pack(side=tk.LEFT)
		frame.pack()
		self.statusbar = tk.Label(parent, text="",bd=1, relief=tk.SUNKEN)
		self.statusbar.pack(side=tk.BOTTOM,fill=tk.X, anchor=tk.W)
		self.parent = parent
		self.widgets = {"parent":self.parent,
						"entry":self.entry,
						"canvas":self.canvas,
						"data": self.var,
						"execute_button": self.execute,
						"undo_button": self.undo,
						"reset_button": self.reset,
						"reload_button": self.reload_algorithms,
						"statusbar":self.statusbar}
	
	def __getitem__(self, key):
		if key not in self.widgets:
			return None
		return self.widgets[key]


		