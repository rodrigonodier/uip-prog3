import os
import tarea_6_cliente as C

ajedrez=[]
atletismo=[]
baloncesto=[]
futbol=[]
karate=[]
natacion=[]
volleyball=[]
flag=[]
pingpong=[]
otros=[]

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
			nombre = input("\n\t Introduzca su nombre: ")
			tmp = C.Deportes(nombre)
			menu(tmp)
			c=1
			count=count+1
		if opc==2 and c==0:
			x = str(input("\n\t Primero debe crear una encuesta.."))
		elif opc==2 and c!=0:
			os.system('cls')
			tmp.statistics(ajedrez,atletismo,baloncesto,futbol,karate,natacion,volleyball,flag,pingpong,otros)
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
		tmp.list_add(ajedrez,tmp.nombre)
	if op==2:
		tmp.list_add(atletismo,tmp.nombre)
	if op==3:
		tmp.list_add(baloncesto,tmp.nombre)
	if op==4:
		tmp.list_add(futbol,tmp.nombre)
	if op==5:
		tmp.list_add(karate,tmp.nombre)
	if op==6:
		tmp.list_add(natacion,tmp.nombre)
	if op==7:
		tmp.list_add(volleyball,tmp.nombre)
	if op==8:
		tmp.list_add(flag,tmp.nombre)
	if op==9:
		tmp.list_add(pingpong,tmp.nombre)
	if op==10:
		tmp.list_add(otros,tmp.nombre)

if __name__ == "__main__":
	main()
	
	