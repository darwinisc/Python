print("Realiza una funcion que permita obtener el volumen de una esfera")

def pro2():
	
#importamos la libreria math para poder utiliza PI
import math
#radio solicita un numero con el valor del radio
#utilizamos float por si el radio tiene punto decimal
radio = float(input ("Ingrese el radio de la esfera: "))
#resultado almacena la operacion 
#math.pi se utiliza para la operacion PI
resultado = (4*math.pi * (radio**3)) / 3
print ("El volumen de la esfera es "+ str (resultado))

pro2()