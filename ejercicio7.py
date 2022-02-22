# Ejercicio 7: Edición de un número entero
resultado=[]
print("¿Qué número quieres editar?")
numero = int(input())
print("¿Qué base quieres usar?")
base = int(input())
def edicion(numero,base):
  if base > 36:
    print(f"{numero}\u2081\u2080") #Para ponerlo más claro
  elif base < 2:
    print("La base no es válida")
  else:
    resultado.append(numero%base)
    if numero//base == 0:
      print(f"La solución es {resultado}")
    else:
      numero=numero//base
      edicion(numero, base)
edicion(numero, base)