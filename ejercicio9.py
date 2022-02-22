from tabulate import tabulate
def añadir_palabra():
  print("¿Qué palabra quieres introducir en el diccionario?")
  palabra=str(input())
def tabla():
    table = [['Diccionario'],[palabra]]
    print(tabulate(table, headers='firstrow', tablefmt='grid'))
tabla()
def eliminar_palabra():
  print("¿Qué palabra quieres eliminar? Describe la posición")
  posicion_borrar= int(input())
  

  
print("¿Qué quieres hacer? 1 añadir palabra 2 eliminar palabra 3 ordenar palabras")
eleccion= int(input())

if eleccion == 1:
  def añadir_palabra()
if eleccion == 2:
  def eliminar_palabra()
if eleccion == 3:
  def ordenar_palabra()
else:
  print("Fin del programa")