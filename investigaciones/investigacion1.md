¿Qué es Main y como funciona?

Main "___main___" es una función en python, de hecho es la función con más alto nivel. 
Esto quiere decir que se creamos una variable fuera de una función, dicha variable va a pertenecer a la función __main__.
Esta función la utilizamos normalmente en conjunto con: *if ___name___ == '___main___':*, esta condición indica que el programa empezará a ejecutarse desde dicho segmento de código.

Ejemplo:

def main():
	print("Hola mundo")

if ___name___ == "___main___":
	main()
