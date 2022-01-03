import copy
import random
from FaceableMiniCube import FaceableMiniCube

class ExecutableMiniCube(FaceableMiniCube):
	def __init__(self):
		super().__init__()
		self._fundamental_operations = {"R" : self.right, "D" : self.down, "B" : self.back}
		self._operations = copy.deepcopy(self._fundamental_operations) #can contain derived instructions
		self._recent_operations = []
		self.saved_states = set()
	
	def reset(self):
		super().reset()
		self.clear_recent_operations()
		self.clear_save_states()
		return self #to show the state interactive in the python shell
	
	def right(self, num_quarter_turns = 1,  is_counter_clockwise = False):
		for i in range(num_quarter_turns):
			super().right(is_counter_clockwise)
		
	def down(self, num_quarter_turns = 1, is_counter_clockwise = False):
		for i in range(num_quarter_turns):
			super().down(is_counter_clockwise)
		
	def back(self, num_quarter_turns = 1, is_counter_clockwise = False):
		for i in range(num_quarter_turns):
			super().back(is_counter_clockwise)
	
	def get_recent_operations(self):
		return self._recent_operations.copy()
	
	def get_operation_names(self):
		return list(self._operations.keys())
		
	def valid(self, instructions):
		for instruction in instructions:
			instruction_name = self.__extract_name(instruction)
			if instruction_name not in self._operations:
				return False
		return True
		
	def new_operation(self, name, subinstructions):
		self._recent_operations.clear() #have to clear else undo no longer works anymore
		assert self.__firstNumericCharacter(name) == None
		assert "'" not in name
		assert self.valid(subinstructions)
		self._operations[name] = subinstructions
		self.reset()
	
	def delete_operation(self, name):
		if name in self._fundamental_operations:
			return
		
		if name not in self._operations:
			return
			
		del self._operations[name]		
		self._recent_operations.clear() #have to clear since operations in list may no longer be present
		self.reset()
	
	def load_operations(self, operations_list):
		self._operations = copy.deepcopy(self._fundamental_operations)
		for operation_name, subinstructions in operations_list:
			self.new_operation(operation_name, subinstructions)
	
	def load_file(self, filename):
		self.reset()
		try:
			file = open(filename,"r")
		except:
			print("loading file data failed! Operations reset to fundamentals: R, D, B")
			return False
			
		operations_list = []
		for line in file:
			if not line.isspace():
				line = line.lstrip()
				if line[0] != "#":
					line = line.rstrip()
					line = line.replace(" ","")
					line = line.split(":")
					line[1] = line[1].split(",")
					operations_list.append(line)
		
		self._operations = copy.deepcopy(self._fundamental_operations)
		try:
			self.load_operations(operations_list)
		except AssertionError as e:
			print("loading file data failed! Operations reset to fundamentals: R, D, B")
			file.close()
			return False #it failed
		file.close()
		return True #it was able to open
		
		
	
	def undo(self):
		if len(self._recent_operations) == 0:
			return
		recent_operation = self.invert(self._recent_operations.pop())
		return self.execute([recent_operation], False)
		
	
	def clear_recent_operations(self):
		self._recent_operations.clear()
		
	def __or__(self, values):
		return self.execute(values)
	
	def __invert__(self): #not to be confused with self.invert, __invert__ will undo the most recent operation
		return self.undo()
		
	def execute(self, instructions, saving_instructions = True):
		assert isinstance(instructions, str) or isinstance(instructions, list)
		if isinstance(instructions, str):
			instructions = instructions.replace(" ","")
			instructions = instructions.split(",") #turns into a list automatically if no commas found
			
		assert self.valid(instructions)
		if saving_instructions: #saving it in our history so we can undo, we se saving_instructions to False when undoing
			self._recent_operations.extend(instructions)
		expanded_instructions = []
		for instruction in instructions:
			instruction_name = self.__extract_name(instruction)
			if instruction_name in self._fundamental_operations:
				expanded_instructions.append(instruction)
			else: #it is a derived operation, and its a list in the self._operations dict, so we extend expanded_instructions
				expanded_instructions.extend(self.expand(instruction))
		self._execute_instructions(expanded_instructions)
		return self #this is so we can have clean interaction in the Python REPL shell
	
	
	#uses recursion and i dont expect a stack over flow with this
	def expand(self, instruction):
		instruction_name = self.__extract_name(instruction)
		if instruction_name in self._fundamental_operations:
			return [instruction]
					
		subinstructions = self._operations[instruction_name]
		expanded_subinstructions = []
		for subinstruction in subinstructions:
			expanded_subinstructions.extend(self.expand(subinstruction))
			
		multiplicity = int(self._extractNumber(instruction)) #if instruction was called A, then of course -1 is A, or if A', then -1 will contain ', therefore A'1 is what we are looking for, so if final character is numeric, then convert it
		if "'" in instruction: #if ' in instruction, then its an inverted derived instruction
			expanded_subinstructions = self.invert_instructions(expanded_subinstructions, True)
		return expanded_subinstructions * multiplicity
	
	
	def __extract_name(self, instruction):
		if "'" in instruction:
			return instruction[:instruction.index("'")]
		
		if instruction[-1].isnumeric():
			return instruction[:self.__firstNumericCharacter(instruction)]
		
		return instruction
	
	def __firstNumericCharacter(self, instruction):
		for i in range(len(instruction)):
			if instruction[i].isnumeric():
				return i
		return None
	
	def _extractNumber(self, instruction):
		index = self.__firstNumericCharacter(instruction)
		if index == None:
			return "1"
		return instruction[index:]
		
		
	def _execute_instructions(self, instructions):
		for instruction in instructions:
			self._execute_instruction(instruction)
			
	def invert_instructions(self, instructions, reversing_instructions = False):
		if reversing_instructions:
			instructions = list(reversed(instructions))
		for i in range(len(instructions)):
			instructions[i] = self.invert(instructions[i])
		return instructions
				
	def invert(self, instruction):
		instruction_name = self.__extract_name(instruction)
		is_counter_clockwise = "'" in instruction
		if is_counter_clockwise:
			return  instruction.replace("'","")
		return instruction_name + "'" + (self._extractNumber(instruction) if instruction[-1].isnumeric() else "")
		
	def _execute_instruction(self, instruction):
		is_counter_clockwise = "'" in instruction #R'5 for example is an instruction of length 3, and is counter clockwise while R2 is an instruction of length2
		instruction_name = self.__extract_name(instruction)
		num_quarter_turns = int(self._extractNumber(instruction))
		self._fundamental_operations[instruction_name](num_quarter_turns, is_counter_clockwise)
	
	def save_state(self):
		self.saved_states.add(self.fullCubeString())
	
	def clear_save_states(self):
		self.saved_states.clear()
	
	def randomize(self, n=10):
		operation_names = list(self._fundamental_operations.keys())
		for i in range(n):
			index = random.randint(0, len(operation_names) - 1)
			self.execute(operation_names[index])


def main():
	cube = ExecutableMiniCube()
	cube.load_file("algorithms.txt")
	print(cube.get_operation_names())

if __name__ == "__main__":
	main()
		
		
