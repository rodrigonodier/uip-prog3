class Deportes(object):

	def __init__(self,nombre):
		self.nombre=nombre

	def list_add(self,lista,nombre):
		item=0
		i=0

		lista.append(nombre)
		
		tmp = str(input("\n Añadido correctamente "))
		
		return lista
		
	def statistics(self,ajedrez,atletismo,baloncesto,futbol,karate,natacion,volleyball,flag,pingpong,otros):
		tmp=0
		print("\n\t Ajedrez: "+ str(ajedrez))
		print("\n\t Atletismo: "+ str(atletismo))
		print("\n\t Baloncesto: "+ str(baloncesto))
		print("\n\t Futbol: "+ str(futbol))
		print("\n\t Karate: "+ str(karate))
		print("\n\t Natacion: "+ str(natacion))
		print("\n\t Volleyball: "+ str(volleyball))
		print("\n\t Flag: "+ str(flag))
		print("\n\t PingPong: "+ str(pingpong))
		print("\n\t Otros: "+ str(otros))
		tmp = str(input("\n Presione ENTER para volver al menu principal."))