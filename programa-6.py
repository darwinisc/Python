print ("programa 6 Realiza un programa que permita generar un intervalo de los cubos de los primeros n numeros") 

def pro6():
	
	n=int(input("Ingresa un numero: "))
	total=0
	for x in range(n):
        	res = pow(x+1,3)
        	print ("El cubo de ", x+1 ,"es ", res)

        	total += res
        	print("la suma del ", x+1 ,"numero generados es ", total)

pro6()