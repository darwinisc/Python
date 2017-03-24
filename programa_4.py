print("Realiza una funcion que permita obtener el maximo de 3 numeros")

def pro4():
	#n1,n2,n3 solicitan 3 numeros para realizar la comparacion 
	n1 = int( input("Ingrese el primer numero \n"))
	n2 = int( input("Ingrese el segundo numero \n"))
	n3 = int( input("Ingrese el tercer numero \n"))

	#en esta seccion se compara el primer numero ingresado 
	if(n1 > n2 and n1 > n3):
  		print("El Numero Maximo es: " + str(n1))
	else:
		#en esta seccion se compara el segundo numero ingresado 
 	if(n2 > n1 and n2 > n3):
  		print("El Numero Maximo es: " + str(n2))
  		#si ninguna de las condiciones se cumple se imprime el tercer numero ingresado
 	else:
  		print("El Numero Maximo es: " + str(n3))

pro4()