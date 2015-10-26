lista_items = {}

def main():
	print("\n\t Bienvenido al modulo de inventario.\n")
	print("\t\t 1. Agregar elemento a la lista de supermercado.")
	print("\t\t 2. Eliminar elemento a la lista de supermercado.")
	print("\t\t 3. Ver elemento a la lista de supermercado.")
	op = int(input("\n Opción: "))
	if op==1:
		list_add()
	
	if op==2:
		list_del()
	
	if op==3:
		list_display()
	else:
		print("Opción invalida.")
		main()


def list_add():

	global lista_items
	item=0
	i=1
	tmp=0
	
	while tmp != "N":
	
		item = str(input("\n\t Nombre del articulo: "))
		#item_qty = str(input("\n\t Cantidad: "))
		
		#lista_items[item]=item_qty
		lista_items[item]=i
		
		
		print("\n Articulo: " + str(lista_items))
		
		tmp = str(input("\n Desea añadir un nuevo articulo? S/N: "))
		i=i+1
		
	else:
		main()

def list_del():
	item=0
	
	item = str(input("\n\t Nombre del articulo: "))
	
	del(lista_items[item])
	
	print(lista_items)
	
	main()
	
	'''
	try:
		fh = open(estudiante + ".txt","w")
		fh.write("Estudiante: "+ estudiante + "\nNotas:      " + str(lista) + "\nPromedio:   " + str(promedio))

	except IOError:
		print("\nNo se ha podido crear el fichero: " + estudiante + ".txt")
	else:
		print("\nEl archivo " + estudiante + ".txt se ha creado correctamente.")
	fh.close()
'''

def list_display():
	print("Añadir elemento.")
if __name__ == "__main__":
	main()