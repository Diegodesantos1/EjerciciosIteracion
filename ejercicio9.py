from tabulate import tabulate
def añadir_palabra():
  print("¿Qué palabra quieres introducir en el diccionario?")
  palabra=str(input())
def tabla():
    table = [['Diccionario'],[palabra]]
    print(tabulate(table, headers='firstrow', tablefmt='grid'))
tabla()
def eliminar_palabra():
  print("¿Qué palabra quieres eliminar?")
  palabra_borrar= str(input())
  table.remove(f"{palabra_borrar}")
eliminar_palabra()
def ordenar_palabras():

print("¿Qué quieres hacer? 1 añadir palabra 2 eliminar palabra 3 ordenar palabras")
eleccion= int(input())
if eleccion == 1:
  def añadir_palabra()

