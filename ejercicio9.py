
print("¿Qué palabra quieres introducir en el diccionario?")
palabra=str(input())
lista = []
lista.append(palabra)
def añadir_palabra():
  print("¿Qué palabra quieres introducir en el diccionario?")
  palabra = str(input())
  lista.append(palabra)
  print(lista)
def eliminar_palabra():
  print("¿Qué palabra quieres eliminar?")
  palabra_borrar= str(input())
  lista.remove(f"{palabra_borrar}")
  print(lista)
def ordenar_palabra():
  lista.sort()
  print(lista)
def eleccion_actual():
  print("¿Qué quieres hacer? añadir,eliminar u ordenar ")
  eleccion= str(input())
  if eleccion == "añadir":
    añadir_palabra()
  if eleccion == "eliminar":
    eliminar_palabra()
  if eleccion == "ordenar":
    ordenar_palabra()
