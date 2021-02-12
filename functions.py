import math
import random

class BoardDecimal:
	firstUpperRow = []
	firstLeftColumn = []

	# Public methods
	def __init__(self):
		self.setFirstUpperRow(self)
		self.setFirstLeftColumn(self)
		
	def getFirstUpperRow(self):
		return self.firstUpperRow
	
	def getFirstLeftColumn(self):
		return self.firstLeftColumn
		
	def printEmptyField(self):
		for i in range(0,9):
			print('|', 9* 'x|')

	# Private methods
	@staticmethod
	def setFirstUpperRow(self):
		filled = False # Has the first row been filled
		i = 0 # Array index
		while filled != True: # Fill the array as long, as condition is not fulfilled
			self.firstUpperRow.append(random.randint(1,9)) # Add new element to the array
			if i > 0: # Called only if the array has at least 2 items aready
				i += self.CRowLast(self)
				if i == 9:
					filled = True
			else:
				i += 1 # First increase
			
	@staticmethod
	def setFirstLeftColumn(self):
		filled = False
		i = 1
		self.firstLeftColumn.append(self.firstUpperRow[0])
		while filled != True:
			self.firstLeftColumn.append(random.randint(1,9))
			i += self.CColumnLast(self)
			if(i == 9):
				filled = True
		
	
	@staticmethod
	def CRowLast(self):
		for i in range(0, len(self.firstUpperRow)-1):
			if self.firstUpperRow[i] == self.firstUpperRow[len(self.firstUpperRow)-1]:
				self.firstUpperRow.pop()
				return 0
		return 1
	
	@staticmethod
	def CColumnLast(self):
		can_return = False
		if len(self.firstLeftColumn) == 2:
			for j in range(1,3):
				if self.firstLeftColumn[1] == self.firstUpperRow[j]:
					self.firstLeftColumn.pop()
					can_return = True
					break
		if (can_return != True):
			if len(self.firstLeftColumn) == 3:
				for j in range(1,3):
					if self.firstLeftColumn[2] == self.firstUpperRow[j]:
						self.firstLeftColumn.pop()
						can_return = True
						break
			if (can_return != True):
				if len(self.firstLeftColumn)>1:
					for i in range(0, len(self.firstLeftColumn)-1):
						if self.firstLeftColumn[i] == self.firstLeftColumn[len(self.firstLeftColumn)-1]:
							self.firstLeftColumn.pop()
							can_return = True
							break
					if (can_return != True):
						return 1
					else:
						return 0
			else:
				return 0
		else:
			return 0
	
	def printField(self):
		for i in range(0,8):
			if i == 0:
				for j in range(0,8):
					print(str(self.firstUpperRow[j]) + ' | ', end = "")
				print()
			if i > 0:
				print(str(self.firstLeftColumn[i]) + ' | x |' + 6 * ' x |')
