# Ejercicio 7: Edición de un número entero
import math
def edicion(numero):
  print("¿Qué número quieres editar?")
  numero = int(input())
  n =numero/base
  if n == 0:
    print(f"El {numero} es igual a elevado a 1")
  else:
    edicion(n)
edicion(numero)