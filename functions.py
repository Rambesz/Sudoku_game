import math
import random

class BoardDecimal:
	centralRow = []
	centralColumn = []
	
	def setCentralRow(self):
		filled = False # Has the first row been filled
		i = 0 # Array index
		while filled != True: # Fill the array as long, as condition is not fulfilled
			self.centralRow.append(random.randint(1,9)) # Add new element to the array
			if i > 0: # Called only if the array has at least 2 items aready
				i += self.CheckLastItem(self)
				if i == 9:
					filled = True
			else:
				i += 1 # First increase
			
		print(20*'-', '\n',self.centralRow)

	@staticmethod
	def CheckLastItem(self):
		for i in range(0, len(self.centralRow)-1):
			if self.centralRow[i] == self.centralRow[len(self.centralRow)-1]:
				print(self.centralRow, '  ', len(self.centralRow) - 1)
				self.centralRow.remove(self.centralRow[len(self.centralRow) - 1])
				print(self.centralRow)
				return 0
		return 1
