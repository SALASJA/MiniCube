import tkinter as tk
from MiniCube import MiniCube
from Controller import Controller
from View import View

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		Controller(MiniCube(), View(self))


def main():
	App().mainloop()

if __name__ == "__main__":
	main()