#TAREA3
# Autor: Rodrigo Vergara
#
# Escriba un programa en Python donde el usuario introduce un número n y el programa imprime los primeros n números triangulares, junto con su índice. 
# Los números triangulares se originan de la suma de los números naturales desde 1 hasta n.

num = int(input("\n Introduzca un número para calcular los primeros n números triangulares junto con su índice: "))
temp = 1

for i in range(num):
	num_t = int(temp*(temp+1)/2)
	print("\n\t " + str(temp) + "  -  " + str(num_t))
	temp = temp+1