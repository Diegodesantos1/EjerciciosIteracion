# Ejercicio 7: Edición de un número entero
def edicion(n):
  print("¿Qué número quieres editar?")
  numero = int(input())
  print("¿Qué base quieres usar?")
  base = int(input())
  if base > 36:
    base = 10
  else:
    