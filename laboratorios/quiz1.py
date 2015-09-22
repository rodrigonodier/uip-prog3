#CLASE 3
# Autor: Rodrigo Vergara
#
# Calcular el area y perimetro de un rectangulo dada la base y altura de 5cm y 7cm respectivamente ademas debe convertir los resltados del area y perimetro
# a otras unidades de medida, metros y pulgadas.

base = 5
altura = 7

area = base * altura
perimetro = 2*(base+altura)

print("")
print("AREA Y PERIMETRO EN CENTIMETROS")
print("")
print("\tEl area es: " + str(area) + "cm")
print("\tEl perimetro es: "+ str(perimetro) + "cm")
print("")

print("AREA Y PERIMETRO DE CM A METROS")
print("")
print("\tEl area es: " + str(area/100) + "m")
print("\tEl perimetro es: "+ str(perimetro/100) + "m")
print("")

print("AREA Y PERIMETRO DE CM A PULGADAS")
print("")
print("\tEl area es: " + str(area*0.39) + " pulgadas")
print("\tEl perimetro es: "+ str(perimetro*0.39) + " pulgadas")
print("")