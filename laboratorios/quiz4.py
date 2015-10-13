# Clase 6
#
# Quiz 4
# 
# Autor: Rodrigo Vergara
#
# Desarrolle una aplicación que guarde, en un archivo de texto, las calificaciones de los 5 quizzes realizados por 3 estudiantes. Cada estudiante tendrá su propio archivo de texto, cuyo nombre de archivo será igual al nombre del estudiante. Además debe mostrar en pantalla, el valor promedio de las calificaciones de cada estudiante. Utilice todos los conceptos aprendidos hasta el momento.

def main():
	for i in range(3):
		estudiante = input("\n Nombre del estudiante: ")
		lista = []
		tmp_prom = 0
		
		print("\nIntroduzca una nota entre 1 y 100.\n")
		for x in range(1,6):
			nota =int(input("\n Nota quiz " + str(x) + ": "))
			while(nota<0 or nota>100):
				print("\n \t Introduzca una nota valida. Rango 1 a 100")
				nota =int(input("\n Nota quiz " + str(x) + ": "))
			else:
				tmp_prom = tmp_prom + nota
				lista.append(nota)

		promedio = tmp_prom/5 
		print("\nEl promedio de notas del estudiante " + estudiante + " es: " + str(promedio))

		try:
			fh = open(estudiante + ".txt","w")
			fh.write("Estudiante: "+ estudiante + "\nNotas:      " + str(lista) + "\nPromedio:   " + str(promedio))

		except IOError:
			print("\nNo se ha podido crear el fichero: " + estudiante + ".txt")
		else:
			print("\nEl archivo " + estudiante + ".txt se ha creado correctamente.")
		fh.close()

if __name__ == "__main__":
	main()