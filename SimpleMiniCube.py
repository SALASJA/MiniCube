import copy

class SimpleMiniCube:

	CLOCKWISE = False
	COUNTER_CLOCKWISE = True
	
	def __init__(self):
		#                       0   1   2   3   4   5
		self._solved_state = [[' ',' ','R','R',' ',' '], #0
					          [' ',' ','R','R',' ',' '], #1
					          ['B','B','W','W','G','G'], #2
					          ['B','B','W','W','G','G'], #3
					          [' ',' ','O','O',' ',' '], #4
					          [' ',' ','O','O',' ',' '], #5
					          [' ',' ','Y','Y',' ',' '], #6
					          [' ',' ','Y','Y',' ',' ']] #7
		
		self._solution = self.fullCubeString(self._solved_state)
		self._state = copy.deepcopy(self._solved_state)
		
	def __str__(self):
		result = self.fullCubeString(self._state)
		return result
	
	def __repr__(self):
		return self.__str__()
	
	def fullCubeString(self, cube_data):
		result = ""
		for row in cube_data:
			result += "   ".join(row) + "\n\n"
		result += "\n"
		return result
		
	def is_solved(self):
		return self.fullCubeString(self._state) == self._solution
	
	def right(self, is_counter_clockwise = False):
		face_positions  = ((2,4),(2,5),(3,5),(3,4))
		self._transform(self._state, face_positions , is_counter_clockwise)
		edge_positions1 = ((2,3),(0,3),(6,3),(4,3))
		self._transform(self._state, edge_positions1, is_counter_clockwise)
		edge_positions2 = ((3,3),(1,3),(7,3),(5,3))
		self._transform(self._state, edge_positions2, is_counter_clockwise)
		
	
	def back(self, is_counter_clockwise = False):
		face_positions  = ((6,2),(6,3),(7,3),(7,2))
		self._transform(self._state, face_positions , is_counter_clockwise)
		edge_positions1 = ((5,2),(3,5),(0,3),(2,0))
		self._transform(self._state, edge_positions1, is_counter_clockwise)
		edge_positions2 = ((5,3),(2,5),(0,2),(3,0))
		self._transform(self._state, edge_positions2, is_counter_clockwise)
		
	
	def down(self, is_counter_clockwise = False):
		face_positions  = ((4,2),(4,3),(5,3),(5,2))
		self._transform(self._state, face_positions , is_counter_clockwise)
		edge_positions1 = ((3,2),(3,4),(6,3),(3,0))
		self._transform(self._state, edge_positions1, is_counter_clockwise)
		edge_positions2 = ((3,3),(3,5),(6,2),(3,1))
		self._transform(self._state, edge_positions2, is_counter_clockwise)
	
	
	def _transform(self, cube_data, face_positions, is_counter_clockwise):
		current_position = face_positions[0]
		prev_row = current_position[0]
		prev_col = current_position[1]
		temp = cube_data[prev_row][prev_col]
		n = len(face_positions)
		i = 1 if is_counter_clockwise else len(face_positions) - 1
		while i < n if is_counter_clockwise else 0 < i:
			current_position = face_positions[i]
			current_row = current_position[0]
			current_col = current_position[1]
			cube_data[prev_row][prev_col] = cube_data[current_row][current_col]
			prev_row = current_row
			prev_col = current_col
			i = i + 1 if is_counter_clockwise else i - 1
		cube_data[prev_row][prev_col] = temp
	
	def reset(self):
		self._state = copy.deepcopy(self._solved_state)



def main():
	cube = SimpleMiniCube()
	print("TESTING RIGHT CLOCKWISE")
	print(cube)
	for i in range(4):
		cube.right(SimpleMiniCube.CLOCKWISE)
		print(cube)
	
	print("TESTING DOWN CLOCKWISE")
	print(cube)
	for i in range(4):
		cube.down(SimpleMiniCube.CLOCKWISE)
		print(cube)
	
	
	print("TESTING BACK CLOCKWISE")
	print(cube)
	for i in range(4):
		cube.back(SimpleMiniCube.CLOCKWISE)
		print(cube)
	
	print("TESTING RIGHT COUNTER_CLOCKWISE")
	print(cube)
	for i in range(4):
		cube.right(SimpleMiniCube.COUNTER_CLOCKWISE)
		print(cube)
	
	print("TESTING DOWN COUNTER_CLOCKWISE")
	print(cube)
	for i in range(4):
		cube.down(SimpleMiniCube.COUNTER_CLOCKWISE)
		print(cube)
	
	
	print("TESTING BACK COUNTER_CLOCKWISE")
	print(cube)
	for i in range(4):
		cube.back(SimpleMiniCube.COUNTER_CLOCKWISE)
		print(cube)
	
	print("TESTING RESET")
	print(cube)
	cube.right(SimpleMiniCube.COUNTER_CLOCKWISE)
	cube.right(SimpleMiniCube.COUNTER_CLOCKWISE)
	print(cube)
	cube.reset()
	print(cube)

if __name__ == "__main__":
	main()

