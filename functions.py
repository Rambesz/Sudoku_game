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
		
	def printDefaultField(self):
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
		if len(self.firstLeftColumn) == 2:
			for j in range(1,2):
				if self.firstLeftColumn[1] == self.firstUpperRow[j]:
					self.firstLeftColumn.pop()
					return 0
		if len(self.firstLeftColumn) == 3:
			for j in range(1,2):
				if self.firstLeftColumn[2] == self.firstUpperRow[j]:
					self.firstLeftColumn.pop()
					return 0
		if len(self.firstLeftColumn)>1:
			for i in range(0, len(self.firstLeftColumn)-1):
				if self.firstLeftColumn[i] == self.firstLeftColumn[len(self.firstLeftColumn)-1]:
					self.firstLeftColumn.pop()
					return 0
		return 1
