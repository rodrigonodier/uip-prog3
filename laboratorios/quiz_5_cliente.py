# mostrar_contador() <- imprime en pantalla el valor del contador privado
# comparar_mensaje() <-  compara el mensaje introducido por el usuario contra el contenido de la variable Msg
# guardar_mensaje() <- guarda mensaje en un archivo txt.

class Mundo(object): 
	
	""" Declaración de atributos"""
	Msg ="hola mundo"
	
	__counter=0
	
	def __init__(self,strMsg):
		self.strMsg = strMsg
		Mundo.__counter+=1
		
	def mostrar_contador(self):
		return "\n\nCondador actual: " + str(self.__counter)

	def comparar_mensaje(self, strMsg):
		if self.Msg ==  strMsg:
			res = " \nLos mensajes son iguales"
			return res
		else:
			res = "\nLos mensajes son diferentes"
			return res

	def guardar_mensaje(self, strMsg):
		try:
			fh = open("mensajes.txt","a+")
			fh.write("Contador: " + str(self.__counter) + " Mensaje: " + strMsg + "\n")

		except IOError:
			print("\nNo se ha podido crear el fichero: " + "mensajes.txt")
		else:
			print("\nEl archivo mensajes.txt se ha creado correctamente.")
		fh.close()