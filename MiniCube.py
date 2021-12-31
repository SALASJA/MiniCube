from ExecutableMiniCube import ExecutableMiniCube

class MiniCube(ExecutableMiniCube):
	def __init__(self, state = None):
		super().__init__()
		if state != None:
			self._state = copy.deepcopy(state)
			

def main():
	cube = MiniCube()

if __name__ == "__main__":
	main()
		