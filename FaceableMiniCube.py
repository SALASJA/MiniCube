from SimpleMiniCube import SimpleMiniCube

class FaceableMiniCube(SimpleMiniCube):
	def __init__(self):
		super().__init__()
		self.mode = None
		self.formatted = True
	
	def set_formatted(self, formatted):
		self.formatted = formatted
	
	def __str__(self):
		if self.mode == "D":
			return self.downFaceString()
		elif self.mode == "U":
			return self.upFaceString()
		elif self.mode == "R":
			return self.rightFaceString()
		elif self.mode == "L":
			return self.leftFaceString()
		elif self.mode == "F":
			return self.frontFaceString()
		elif self.mode == "B":
			return self.backFaceString()
		return self.fullCubeString(self._state)
	
	def set_str_mode(self, mode):
		self.mode = mode
	
	def __getitem__(self,value):
		rotation = 0
		if len(value) == 2:
			rotation = int(value[1])
			value = value[0]
		
		result = self.fullCubeString(self._state)
		if value == "D":
			result = self.downFaceString(rotation)
		elif value == "U":
			result = self.upFaceString(rotation)
		elif value == "R":
			result = self.rightFaceString(rotation)
		elif value == "L":
			result = self.leftFaceString(rotation)
		elif value == "F":
			result = self.frontFaceString(rotation)
		elif value == "B":
			result = self.backFaceString(rotation)
		
		if not self.formatted:
			result = result.replace(" ","").rstrip().split("\n")
			result[0] = " " + result[0] + " "
			result[3] = " " + result[3] + " "
		return result
	
	
	def downFaceString(self, rotation = 0):
		positions = [[None ,(3,2),(3,3), None], 
					 [(3,1),(4,2),(4,3),(3,4)],
					 [(3,0),(5,2),(5,3),(3,5)],
					 [None ,(6,2),(6,3), None]]
		edges1 = [(0,1),(1,3),(3,2),(2,0)]
		edges2 = [(0,2),(2,3),(3,1),(1,0)]
		center = [(1,1),(1,2),(2,2),(2,1)]
		for i in range(rotation):
			self._transform(positions, edges1, False)
			self._transform(positions, edges2, False)
			self._transform(positions, center, False)
		return self.faceString(positions)
	
	#havnt finish the other ones below here 
	def upFaceString(self, rotation = 0):
		positions = [[None ,(7,2),(7,3), None], 
					 [(2,0),(0,2),(0,3),(2,4)],
					 [(2,1),(1,2),(1,3),(2,5)],
					 [None ,(2,2),(2,3), None]]
		edges1 = [(0,1),(1,3),(3,2),(2,0)]
		edges2 = [(0,2),(2,3),(3,1),(1,0)]
		center = [(1,1),(1,2),(2,2),(2,1)]
		for i in range(rotation):
			self._transform(positions, edges1, False)
			self._transform(positions, edges2, False)
			self._transform(positions, center, False)
		return self.faceString(positions)
	
	def rightFaceString(self, rotation = 0):
		positions = [[None ,(1,3),(0,3), None], 
					 [(2,3),(2,4),(2,5),(7,3)],
					 [(3,3),(3,4),(3,5),(6,3)],
					 [None ,(4,3),(5,3), None]]
		edges1 = [(0,1),(1,3),(3,2),(2,0)]
		edges2 = [(0,2),(2,3),(3,1),(1,0)]
		center = [(1,1),(1,2),(2,2),(2,1)]
		for i in range(rotation):
			self._transform(positions, edges1, False)
			self._transform(positions, edges2, False)
			self._transform(positions, center, False)
		return self.faceString(positions)
	
	def leftFaceString(self, rotation = 0):
		positions = [[None ,(0,2),(1,2), None], 
					 [(7,2),(2,0),(2,1),(2,2)],
					 [(6,2),(3,0),(3,1),(3,2)],
					 [None ,(5,2),(4,2), None]]
		edges1 = [(0,1),(1,3),(3,2),(2,0)]
		edges2 = [(0,2),(2,3),(3,1),(1,0)]
		center = [(1,1),(1,2),(2,2),(2,1)]
		for i in range(rotation):
			self._transform(positions, edges1, False)
			self._transform(positions, edges2, False)
			self._transform(positions, center, False)
		return self.faceString(positions)
	
	def frontFaceString(self, rotation = 0):
		positions = [[None ,(1,2),(1,3), None], 
					 [(2,1),(2,2),(2,3),(2,4)],
					 [(3,1),(3,2),(3,3),(3,4)],
					 [None ,(4,2),(4,3), None]]
		edges1 = [(0,1),(1,3),(3,2),(2,0)]
		edges2 = [(0,2),(2,3),(3,1),(1,0)]
		center = [(1,1),(1,2),(2,2),(2,1)]
		for i in range(rotation):
			self._transform(positions, edges1, False)
			self._transform(positions, edges2, False)
			self._transform(positions, center, False)
		return self.faceString(positions)
	
	def backFaceString(self, rotation = 0):
		positions = [[None ,(5,2),(5,3), None], 
					 [(3,0),(6,2),(6,3),(3,5)],
					 [(2,0),(7,2),(7,3),(2,5)],
					 [None ,(0,2),(0,3), None]]
		edges1 = [(0,1),(1,3),(3,2),(2,0)]
		edges2 = [(0,2),(2,3),(3,1),(1,0)]
		center = [(1,1),(1,2),(2,2),(2,1)]
		for i in range(rotation):
			self._transform(positions, edges1, False)
			self._transform(positions, edges2, False)
			self._transform(positions, center, False)
		return self.faceString(positions)
	
	def faceString(self, positions):
		result = ""
		for index in range(len(positions)):
			row = positions[index]
			if index in [0,3]:
				result += "   "
			for k in range(len(row)):
				item = row[k]
				if item != None:
					i,j = item
					if index in [0,3]:
						result += self._state[i][j] + ("\n" if k == 2 else "  ")
					else:
						result += self._state[i][j] + ("\n" if k == 3 else "  ")
		return result