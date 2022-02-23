<h1 align="center">Ejercicios de Iteración</h1>

*Hemos usado la herramienta de Replit para poder programar online y de forma colaborativa y así resolver los ejercicios propuestos.*

***

<h2>Repositorio</h2>

Este es el link del [Repositorio](https://github.com/Diegodesantos1/EjerciciosIteracion)

***

<h2>Integrantes</h2>

1. [Juan](https://github.com/jmedina28)
2. [Diego](https://github.com/Diegodesantos1)

***

<h2>Milestones</h2>

## Ejercicio 6: Historial de una cuenta corriente

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/1?closed=1)

## Ejercicio Ejercicio 7: Edición de un número entero

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/2?closed=1)
 
 EL código empleado para resolverlo es el siguiente:
 ```python
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
```

## Ejercicio 8: Análisis de una cadena de caracteres

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/3)

## Ejercicio 9: Búsqueda de palabras en un diccionario

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/4)

## Ejercicio 10: Representar los miembros de una familia

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/5)

## Ejercicio 11: mcd de dos números enteros

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/6)

## Ejercicio 12: Cuadrados perfectos y raíz cuadrada entera

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/7)

