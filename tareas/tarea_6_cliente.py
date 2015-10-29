from collections import Counter

class Deportes(object):

	def __init__(self,nombre):
		self.nombre=nombre

	def list_add(self,lista,nombre,zzz):
		item=0
		i=0
		lista[zzz]+=1

		#lista.append(zzz)
		
		tmp = str(input("\n Añadido correctamente "))
		
		return lista
		
	def statistics(self,lista):
		tmp=0
		
		print("\n\t Ajedrez: "+ str(lista["ajedrez"]))
		print("\n\t Atletismo: "+ str(lista["atletismo"]))
		print("\n\t Baloncesto: "+ str(lista["baloncesto"]))
		print("\n\t Futbol: "+ str(lista["futbol"]))
		print("\n\t Karate: "+ str(lista["karate"]))
		print("\n\t Natacion: "+ str(lista["natacion"]))
		print("\n\t Volleyball: "+ str(lista["volleyball"]))
		print("\n\t Flag: "+ str(lista["flag"]))
		print("\n\t PingPong: "+ str(lista["pingpong"]))
		print("\n\t Otros: "+ str(lista["otros"]))
		
		high_txt = max(lista, key=lista.get) 
		high_num = lista[high_txt]
		
		print("\n\t El deporte mas popular es: " +  str(high_txt)  + " con " + str(high_num) + " persona(as) encuestada(as).")
		
		tmp = str(input("\n Presione ENTER para volver al menu principal."))
		