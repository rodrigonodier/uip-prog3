import inspect,os,win32ui
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

Window.size=(850,130)

class Boxes(FloatLayout):
	lista={}
	title="Sistema de Inventario SuperMercados Emperador S.A"
	def add(self,a,b,c):
		if a=="" and b=="" and c=="":
			print("Rellene todos los campos.")
			win32ui.MessageBox("Rellene todos los campos.", str(self.title))
		else:
			self.lista[a]=b+"#"+c
			win32ui.MessageBox("El articulo se añadio correctamente a la base de datos.", str(self.title))
			print(str(self.lista))
	pass

	def delete_item(self,a,cant):
		if a in self.lista:
			tmp1=self.lista[a]
			tmp2=tmp1.find("#")+1
			qty=int(tmp1[tmp2:])-int(cant)
			self.lista[a]=tmp1[:tmp2]+str(qty)
		else:
			try:
				del (self.lista[item])
				print("Articulo borrado correctamente")
			except Exception:
				print("El articulo no existe en la base de datos.")

	def delete(self,a):
		try:
			del (self.lista[a])
			print("Articulo borrado correctamente")
		except Exception:
			print("El articulo no existe en la base de datos.")

	def search(self,a):
		if a in self.lista:
			print(str(self.lista[a]))
		else:
			print("El articulo no existe en la base de datos.")

	def export(self):
		print(self.lista)
		f_path=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		try:
			zz = open(f_path+ "/articulos.txt","w")
			for key in self.lista.keys():
				strItem=str(self.lista[key])
				qty=strItem.find("#",1)+1
				zz.write("IDArticulo: \t"+ str(key) + "\t cantidad: \t" + str(strItem[qty:]) + "\n" )

		except IOError:
			print("\nNo se ha podido crear el fichero articulos.txt")
		else:
			print("\nEl archivo articulos.txt se ha creado correctamente.")
		zz.close()


class Parcial1App(App):
	def build(self):
		self.title="Sistema de Inventario SuperMercados Emperador S.A | Parcial 1 | Programación 3"
		return Boxes()

if __name__ == '__main__':
	Parcial1App().run()