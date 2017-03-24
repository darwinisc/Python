print ("Realiza un programa que permita generar un intervalo de los cuadrados de n numeros mayores a 100")

def pro7():

   n = int(input("Ingresa un intervalo: "))
   # x toma los numero genrados por n
   if n <= 10: 
   			print("ninguno de los numeros generados es mayor a 100 ingrese otro numero")
   			

   for x in range(n):
	# pow metodo para elvar un numero a su potencia (numero a elevar, potencia a elevar)
        res = pow(x+1,2)
        #condicion solo imprime los numero mayores a 100
        if res>100:
          
            print("lo numeros mayores a 100 son: ", res)

    

pro7()