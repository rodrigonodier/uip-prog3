def list_del(tmp):
	item=0
	catch =0
	print(str(tmp))
	
	while catch != "n":
		item = str(input("\n\t Nombre del articulo: "))
		try:
			del(tmp[item])
		except Exception:
			print("\n\n El elemento no existe")
		else:
			catch = str(input("\n Articulo borrado correctamente. Desea borrar otro ? S/N: ")).lower()

	else:
		return tmp