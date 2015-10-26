
import os
import tarea_5_add as A
import tarea_5_del as R
import tarea_5_display as D

lista_items={}

def main():
	op=1
	catch=0
	tmp=0
	while op !=4:
	
		os.system('cls')
		print("\n\t Gestión de lista de supermercado.\n")
		print("\t\t 1. Agregar elemento a la lista de supermercado.")
		print("\t\t 2. Eliminar elemento a la lista de supermercado.")
		print("\t\t 3. Ver elemento a la lista de supermercado.")
		print("\t\t 4. Salir.")

		op = int(input("\n Opción: "))

		if op==1:
			tmp = A.list_add(lista_items)
		
		if op==2:
			if tmp ==0:
				print("\nPrimero debe introducir un elemento en la lista.")
				catch = input ("\n\nPresione ENTER para volver al Menu principal")
				main()
			elif tmp!=0:
				obj = R.list_del(tmp)
		
		if op==3:
			obj = D.list_display(tmp)
			catch = input ("\n\nPresione ENTER para volver al Menu principal")
	else:
		return

if __name__ == "__main__":
	main()