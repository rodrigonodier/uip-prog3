# Clase 4
#
# Quiz 2
# 
# Autor: Rodrigo Vergara
#
# Programa que calcula el descuento sobre el total de la compra.


for i in range(1,6):

	print("")
	print("Monto de compra del cliente " + str(i))
	monto = int(input("$"))

	if monto >= 500:
		descuento = monto*0.30
		print("")
		print("\t Sub total: "+ str(monto))
		print("\t Descuento: "+  str(round(descuento,2)))
		print("\t Total: "+str((monto-descuento)))

	elif monto < 500 and monto >=200:
		descuento = monto*0.20
		print("")
		print("\t Sub total: "+ str(monto))
		print("\t Descuento: "+  str(round(descuento,2)))
		print("\t Total: "+str((monto-descuento)))

	elif monto < 200 and monto >= 100:
		descuento = monto*0.10
		print("")
		print("\t Sub total: "+ str(monto))
		print("\t Descuento: "+  str(round(descuento,2)))
		print("\t Total: "+str((monto-descuento)))
	else:
		print("")
		print("\t Sub total: "+ str(monto))
		print("\t Descuento: "+  "0")
		print("\t Total: "+str((monto)))