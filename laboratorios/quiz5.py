# CLASE 7
# Autor: Abdel G. Martinez L.
#
# Instrucciones: Simular un cliente de un banco

import os
import msvcrt
import quiz_5_cliente as M

def main():

	opc = 0
	c=0
	while opc !=5:
		os.system('cls')
		print("\n\t Menu")
		print("\n\t 1. Ingresar mensaje.")
		print("\n\t 2. Comparar mensaje.")
		print("\n\t 3. Guardar mensaje.")
		print("\n\t 4. Mostrar contador.")
		print("\n\t 5  Salir.")
		
		opc= int(input("\n\t Opción: "))

		if opc==1:
			txt = input("\nMensaje: ")
			msg = M.Mundo(txt)
			tmp = input ("\n\nPresione ENTER para volver al Menu principal...")
			c= 1

		if opc==2 and c==0:
			print("\nPrimero debe ingresar un mensaje")
			tmp = input ("\n\nPresione ENTER para volver al Menu principal...")
		elif opc==2 and c!=0:
			print(msg.comparar_mensaje(txt.lower()))
			tmp = input ("\n\nPresione ENTER para volver al Menu principal...")

		if opc==3 and c==0:
			print("\nPrimero debe ingresar un mensaje")
			tmp = input ("\n\nPresione ENTER para volver al Menu principal...")
		elif opc==3 and c!=0:
			msg.guardar_mensaje(txt)
			tmp = input ("\n\nPresione ENTER para volver al Menu principal...")

		if opc==4 and c==0:
			print("\nEl contador esta en 0")
			tmp = input ("\n\nPresione ENTER para volver al Menu principal...")
		elif opc==4 and c!=0:
			print(msg.mostrar_contador())
			tmp = input ("\n\nPresione ENTER para volver al Menu principal...")

if __name__ == "__main__":
	main()