# Clase 5
#
# Quiz 3
# 
# Autor: Rodrigo Vergara
#
# Dado un intervalo de tiempo en segundos, calcular los segundos restantes que corresponden para convertirse exactamente en minutos. Este programa debe funcionar para 5 oportunidades.


for i in range(5):
	fijo = 60
	num = 0
	temp = 0
	num = int(input("\nIntroduzca un intervalo de tiempo en segundos: "))
	
	while num > fijo:
		fijo = fijo + 60

	tmp = fijo -num

	print("\n\tFaltan " + str(tmp) + " segundos")