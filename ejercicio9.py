import sys
lista = []
def añadir_palabra():
  print("¿Qué palabra quieres introducir en el diccionario?")
  palabra = str(input())
  lista.append(palabra)
  print(lista)
  print("¿Quieres introducir más palabras? si o no")
  eleccion1=str(input())
  if eleccion1 == "si":
    añadir_palabra()
  if eleccion1 == "no":
    eleccion_actual()
def eliminar_palabra():
  print("¿Qué palabra quieres eliminar?")
  palabra_borrar= str(input())
  lista.remove(f"{palabra_borrar}")
  print(lista)
  eleccion_actual()
def ordenar_palabra():
    lista.sort()
    print(lista)
def eleccion_actual():
  print("¿Qué quieres hacer? añadir, eliminar, ordenar o terminar")
  eleccion= str(input())
  if eleccion == "añadir":
    añadir_palabra()
  if eleccion == "eliminar":
    eliminar_palabra()
  if eleccion == "ordenar":
    ordenar_palabra()
  if eleccion == "terminar":
    print(lista)
    sys.exit
añadir_palabra()