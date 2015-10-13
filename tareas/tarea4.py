# Clase 5
#
# Tarea 4
# 
# Autor: Rodrigo Vergara
#
# Dado un intervalo de tiempo en minutos, calcular los días, horas y minutos correspondientes.


tiempo = int(input("\nIntroduzca el tiempo en minutos: "))

dias = tiempo // 1440

horas = tiempo // 60

minutos = tiempo

segundos = tiempo * 60

print("\n")
print("\tDias:          \t" + str(dias))
print("\tHoras:        \t" + str(horas))
print("\tMinutos:   \t" + str(minutos))
print("\tSegundos:  \t" + str(segundos))