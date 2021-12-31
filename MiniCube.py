from ExecutableMiniCube import ExecutableMiniCube

class MiniCube(ExecutableMiniCube):
	def __init__(self, state = None):
		super().__init__()
		if state != None:
			self._state = copy.deepcopy(state)
			

if __name__ == "__main__":
	cube = MiniCube()
	cube.load_file("algorithms.txt")
	print(cube.get_operation_names())
		