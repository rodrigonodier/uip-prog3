#TAREA2
# Autor: Rodrigo Vergara
#
# Crear un programa en Python que resuelva el siguiente problema de física: Una ambulancia se mueve con una velocidad de 120 km/h y necesita recorrer un tramo recto de 60km. 
# Calcular el tiempo necesario, en segundos, para que la ambulancia llegue a su destino. La fórmula a utilizar es: velocidad = distancia / tiempo.

# velocidad = distancia / tiempo

velocidad_kmh = 120
distancia_km = 60

velocidad_ms = (velocidad_kmh * 1000)/3600
distancia_m = distancia_km *1000
tiempo_s = distancia_m / velocidad_ms

print("")
print("""Una ambulancia se mueve con una velocidad de 120 km/h y necesita recorrer un tramo recto de 60km.  Calcular el tiempo necesario, en segundos, para que la ambulancia llegue a su destino. 

La fórmula a utilizar es: velocidad = distancia / tiempo.""")

print("")
print(" DATOS ORIGINALES")
print("")
print("\t Velocidad = " + str(velocidad_kmh) + "km/h")
print("\t Distancia = " + str(distancia_km) + "km")
print("")
print(" VALORES TRANSFORMADOS")
print("")
print("\t Velocidad = " + str(round(velocidad_ms, 2)) + "m/s")
print("\t Distancia = " + str(distancia_m) + "m")
print("")
print("\t Tiempo = "  + str(round(tiempo_s, 2)) + "s") 
print("")

