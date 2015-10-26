def list_add(lista_items):

	item=0
	i=0
	tmp=0
	
	while tmp != "n":
	
		item = str(input("\n\t Nombre del articulo: "))

		lista_items[item]=i
		
		tmp = str(input("\n Articulo agregado correctamente. Desea añadir uno nuevo? S/N: ")).lower()
		
	else:
		return lista_items