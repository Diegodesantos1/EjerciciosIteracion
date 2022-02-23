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
  print("¿Quieres ordenar la lista? si o no")
  si_no=str(input())
  if si_no == "si" or "Si" or "Sí" or "sí":
    lista.sort()
  else:
    sys.exit
def eleccion_actual():
  print("¿Qué quieres hacer? añadir, eliminar, ordenar o terminar")
  eleccion= str(input())
  if eleccion == "añadir" or "Añadir":
    añadir_palabra()
  if eleccion == "eliminar" or "Eliminar":
    eliminar_palabra()
  if eleccion == "ordenar" or "Ordenar":
    ordenar_palabra()
  if eleccion == "terminar" or "Terminar":
    sys.exit
añadir_palabra()