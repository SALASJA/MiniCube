class Controller:
	def __init__(self, model, view):
		self.model = model
		self.view = view
		self._assign_callbacks()
		self.model.set_formatted(False)
		self.view["parent"].focus_set()
		self._draw()
		
	def _assign_callbacks(self):
		commands =  {"Return": self.execute,
		             "w":lambda: self.execute("B"),
		             "e":lambda: self.execute("D"),
		             "r":lambda: self.execute("R"),
		             "s":lambda: self.execute("B'"),
		             "d":lambda: self.execute("D'"),
		             "f":lambda: self.execute("R'"),
		             "Tab":self.toggle_keyboard_mode}
		self.view["parent"].bind("<Key>", lambda e: commands[e.keysym]() if e.keysym in commands else print(e))
		self.view["reset_button"]["command"] = self.reset
		self.view["execute_button"]["command"] = self.execute
		self.view["undo_button"]["command"] = self.undo
		self.view["reload_button"]["command"] = self.reload
	
	def toggle_keyboard_mode(self):	
		if str(self.view["canvas"].focus_get()) == ".!entry":
			self.view["canvas"].focus()
			self.view["statusbar"]["text"] = "keyboard mode on, click back on entry to turn off"
	
	def reset(self):
		print(self.model.reset())
		self._draw()
	
	def execute(self, value = None): 
		keyboard_mode = str(self.view["canvas"].focus_get()) != ".!entry"
		print(str(self.view["canvas"].focus_get()), keyboard_mode, value)
		if not keyboard_mode and value != None:
			return
			
		try:
			instructions = self.view["data"].get()
			print(self.model.execute(value if keyboard_mode else instructions))
			print(self.model.get_recent_operations())
			self.view["statusbar"]["text"] = "executed {:s}".format(value if keyboard_mode else instructions)
		except:
			self.view["statusbar"]["text"] = "failed to execute instructions!"
		self._draw()
	
	def undo(self):
		print(self.model.undo())
		print(self.model.get_recent_operations())
		self._draw()
		self.view["statusbar"]["text"] = "reverted to previous state"
		
		
	def _draw(self):
		self.view["canvas"].render(self.model["F"],top=True)
		self.view["canvas"].render(self.model["B"],top=False)
	
	def reload(self):
		if self.model.load_file("algorithms.txt"):
			self.view["statusbar"]["text"] = "algorithms.txt has been loaded"
		else:
			self.view["statusbar"]["text"] = "File not found or error in algorithms.txt file"
		print(self.model)
		self._draw()
		
	