def separacion(texto, separador):
  lista = texto.split(separador)
  return lista

texto = input("Introduzca el texto que desea separar: ")
print(separacion(texto, input("Introduzca el separador que desea usar: ")))