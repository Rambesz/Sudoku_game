from functions import*

def Main():
	tabla = BoardDecimal()
	tablaa = [0,1,2,3,4]
	print(tabla.getFirstUpperRow())
	
	print(tabla.getFirstLeftColumn())
	#tabla.printDefaultField()

if __name__ == '__main__':
	Main()