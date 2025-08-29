#nombre: elaborar un algoritmo que muestre si la temperatura es adecuada 

#entrada: tiempo

#proceso: ingresa un numero y muestra si la temperatura es mayor o menor 

#salida: imprime en pantalla la temperatura 

temp = int (input("ingrese la temperatura:"))
if temp <= 0 :
    print("la temperatura es adecuada:")
else:
    print("la temperatura no es adecuada")