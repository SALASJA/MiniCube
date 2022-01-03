class Controller:
	def __init__(self, model, view):
		self.model = model
		self.view = view
		self._assign_callbacks()
		self.model.set_formatted(False)
		self.view["parent"].bind("<Return>", lambda e: self.execute())
		self.view["parent"].focus_set()
		self._draw()
		
	def _assign_callbacks(self):
		self.view["reset_button"]["command"] = self.reset
		self.view["execute_button"]["command"] = self.execute
		self.view["undo_button"]["command"] = self.undo
		self.view["reload_button"]["command"] = self.reload
	
	def reset(self):
		print(self.model.reset())
		self._draw()
	
	def execute(self):
		try:
			instructions = self.view["data"].get()
			print(self.model.execute(instructions))
			self.view["statusbar"]["text"] = "executed {:s}".format(instructions)
		except:
			self.view["statusbar"]["text"] = "failed to execute instructions!"
		self._draw()
	
	def undo(self):
		print(self.model.undo())
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
		
	