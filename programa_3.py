print("Realiza una funcion que permita obtener la intercalacion de 10 numeros impares, iniciando con el 13")

def pro3():
	# se genera los numeros del 13 a 32
	for intercalacion in range(13, 32):
		#se determina que los numeros etaran en incremento de 2 en 2
		if intercalacion % 2 != 0:
			print (intercalacion)
pro3()