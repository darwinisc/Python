print("Realiza un programa que permita generar un intervalo de n numeros entre 20 y 60") 

def inter():
   numero = int(input ("Ingrese un numero entre 20 y 60: "))
   
   #condicion si el numero es menor a 20 es error y si el numero es mayor a 60 es error
   if numero>=20 and numero<=60:
   	#los numeros generados son guardados en la variable
      resultado=numero
      #condicion los numeros generados deben ser mernores o igual a 60
      while resultado<=60:
         print(resultado)
         resultado +=1
     
   else:
      print ("Error no ingreso un intervalo entre 20 y 60")
inter()