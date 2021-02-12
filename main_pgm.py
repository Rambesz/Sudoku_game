from functions import*

def Main():
	tabla = BoardDecimal()
	print(tabla.getFirstUpperRow())
	print(tabla.getFirstLeftColumn())
	#tabla.printDefaultField()
	

if __name__ == '__main__':
	Main()