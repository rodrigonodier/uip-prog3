import os
import tarea_6_cliente as C

lista={"ajedrez":0,"atletismo":0,"baloncesto":0,"futbol":0,"karate":0,"natacion":0,"volleyball":0,"flag":0,"pingpong":0,"otros":0}

def main():
	
	opc=0
	nombre=1
	c=0
	count=0
	while opc!=3:
		os.system('cls')
		print("\n\t\t\t ENCUESTAS DE DEPORTES\n\n")
		print("\n\t 1. Rellenar nueva encuesta.")
		print("\n\t 2. Mostrar estadisticas.")
		print("\n\t 3. Salir del programa.")
		opc = int(input("\n Opción: "))
		
		if opc==1 and count==10:
			x = str(input("\n\t Ha alcanzado el maximo de 10 encuestas.."))
		elif opc==1 and count<=9:
			nombre = input("\n\t Introduzca el nombre: ")
			while nombre =="":
				print("\n\t Introduzca un nombre valido.")
				nombre = input("\n\t Introduzca el nombre: ")
			else:
				tmp = C.Deportes(nombre)
				menu(tmp)
				c=1
				count=count+1
		if opc==2 and c==0:
			x = str(input("\n\t Primero debe crear una encuesta.."))
		elif opc==2 and c!=0:
			os.system('cls')
			tmp.statistics(lista)
	else:
		return

def menu(tmp):
	op=1
	catch=0
	os.system('cls')
	print("\n\t\t\t Categorias de deportes.\n\n")
	print("\n¿Que deporte le gusta a " + tmp.nombre + " ? \n")
	print("\t\t 1. Ajedrez.")
	print("\t\t 2. Atletismo.")
	print("\t\t 3. Baloncesto.")
	print("\t\t 4. Futbol.")
	print("\t\t 5. Karate.")
	print("\t\t 6. Natación.")
	print("\t\t 7. Volleyball.")
	print("\t\t 8. Flag.")
	print("\t\t 9. Ping Pong.")
	print("\t\t 10. Otros.")

	op = int(input("\n Introduzca el numero asociado a la categoria: "))
	
	if op==1:
		zzz="ajedrez"
		tmp.list_add(lista,tmp.nombre,zzz)
	if op==2:
		zzz="atletismo"
		tmp.list_add(lista,tmp.nombre,zzz)
	if op==3:
		zzz="baloncesto"
		tmp.list_add(lista,tmp.nombre,zzz)
	if op==4:
		zzz="futbol"
		tmp.list_add(lista,tmp.nombre,zzz)
	if op==5:
		zzz="karate"
		tmp.list_add(lista,tmp.nombre,zzz)
	if op==6:
		zzz="natacion"
		tmp.list_add(lista,tmp.nombre,zzz)
	if op==7:
		zzz="volleyball"
		tmp.list_add(lista,tmp.nombre,zzz)
	if op==8:
		zzz="flag"
		tmp.list_add(lista,tmp.nombre,zzz)
	if op==9:
		zzz="pingpong"
		tmp.list_add(lista,tmp.nombre,zzz)
	if op==10:
		zzz="otros"
		tmp.list_add(lista,tmp.nombre,zzz)

if __name__ == "__main__":
	main()
	
	