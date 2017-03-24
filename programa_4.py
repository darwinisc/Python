#Maximo de 3 numeros 
n1=int(input("Ingrese el primer numero \n"))
n2=int(input("Ingrese el segundo numero \n"))
n3=int(input("Ingrese el tercer numero \n"))

if(n1 > n2 and n1 > n3):
  print("El Numero Maximo es: " + str(n1))
else:
 if(n2 > n1 and n2 > n3):
  print("El Numero Maximo es: " + str(n2))
 else:
  print("El Numero Maximo es: " + str(n3))
