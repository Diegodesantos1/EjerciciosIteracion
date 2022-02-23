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

## Ejercicio 6: Historial de una cuenta corriente

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/1?closed=1)

El código empleado para resolverlo es el siguiente:

```python
import random
from tabulate import tabulate
from tabulate import TableFormat

print("""
Bienvenido a la plataforma de acceso de su cuenta bancaria,
  Introduzca los datos que se le van a pedir a continuación:
  """)
nombre = str(input("Por favor, introduzca su nombre completo: "))
min = 5000
max = 100000
saldo = random.uniform(min, max)
gastomax = saldo / 4
gastos = random.uniform(0, gastomax)
tabla = [[" Nombre", "Saldo total ", "Gastos "], [ nombre, saldo, gastos]]
print(tabulate(tabla, headers="firstrow", tablefmt="grid"))
familia = int(input("Si desea acceder a los datos de la cuenta familiar pulse 1, en caso contrario pulse 0: "))
if familia == 1:
  print("Usted ha accedido a los datos bancarios de su entorno familiar, aquí se muestra un resumen: ")
  tabla2 = [[" Nombre", "Saldo total ", "Gastos "], [ nombre, saldo, gastos],[ "Susana", random.uniform(3000, 80000), random.uniform(0, 2999)],[ "Elver (menor de edad)", random.uniform(300,1000), random.uniform(0, 200)],[ "Rosa (menor de edad)", random.uniform(300,1000), random.uniform(0, 200)],[ "Devora (menor de edad)", random.uniform(300,1000), random.uniform(0, 200)]]
  print(tabulate(tabla2, headers="firstrow", tablefmt="grid"))
else:
  print("Usted ha decidido abandonar la plataforma.")
 ```


## Ejercicio Ejercicio 7: Edición de un número entero

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/2?closed=1)
 
El código empleado para resolverlo es el siguiente:
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

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/3?closed=1)

El código empleado para resolverlo es el siguiente:
```python
def separacion(texto, separador):
  lista = texto.split(separador)
  return lista

texto = input("Introduzca el texto que desea separar: ")
print(separacion(texto, input("Introduzca el separador que desea usar: ")))
```

## Ejercicio 9: Búsqueda de palabras en un diccionario

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/4?closed=1)

El código empleado para resolverlo es el siguiente:
```python
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
```

## Ejercicio 10: Representar los miembros de una familia

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/5?closed=1)

El código empleado para resolverlo es el siguiente:

```python
import random
from tabulate import tabulate
from tabulate import TableFormat

print('"Usted ha decidido ejecutar el programa de "Miembros de una familia".')
edad1 = random.randint(5,99)
edad2 = random.randint(5,99)
edad3 = random.randint(5,99)
edad4 = random.randint(5,99)
edad5 = random.randint(5,99)
edad6 = random.randint(5,99)
edad7 = random.randint(5,99)
tabla = [[" Nombre", "Edad ", "Atributo "], [ "Juan", edad1, "Huérfan@"],[ "María", edad2, "Huérfan@"],[ "Isabel", edad3, "Vacío"],[ "Carlos", edad4, "Borrado"],[ "Leonardo", edad5, "Vacío"],[ "Manuel", edad6, "Vacío"],[ "Carla", edad7, "Huérfan@"]]
print(tabulate(tabla, headers="firstrow", tablefmt="grid"))

variable = int(input("Si desea sumarle un año a todos los miembros de la familia pulse 1, en caso contrario pulse cualquier otro número: "))
if variable == 1:
  edad1 += 1
  edad2 += 1
  edad3 += 1
  edad4 += 1
  edad5 += 1
  edad6 += 1
  edad7 += 1
  tabla = [[" Nombre", "Edad ", "Atributo "], [ "Juan", edad1, "Huérfan@"],[ "María", edad2, "Huérfan@"],[ "Isabel", edad3, "Vacío"],[ "Carlos", edad4, "Borrado"],[ "Leonardo", edad5, "Vacío"],[           "Manuel", edad6, "Vacío"],[ "Carla", edad7, "Huérfan@"]]
  print(tabulate(tabla, headers="firstrow", tablefmt="grid"))
 ```

## Ejercicio 11: mcd de dos números enteros

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/6?closed=1)

El código empleado para resolverlo es el siguiente:

```python
print("¿Qué forma quieres ejecutar? 1(Euclides) o 2 (sumas y restas)")
eleccion=int(input())
print("Introduzca el primer número")
n_1=int(input())
print("Introduzca el segundo número")
n_2 = int(input())
if eleccion == 1:
  def mcd(n_1, n_2):
      if n_2 == 0:
          return n_1
      return mcd (n_2, n_1 % n_2)
  resultado =mcd(n_1,n_2)
  print(f"El mcd de {n_1} y {n_2} es {resultado}")
elif eleccion == 2:
  def mcd(n_1, n_2): 
    if (n_1 == 0): 
        return n_2 
    if (n_2 == 0): 
        return n_1 
    if (n_1 == n_2): 
        return n_1 
    if (n_1 > n_2): 
        return mcd(n_1-n_2, n_2) 
    return mcd(n_1, n_2-n_1)
  if(mcd(n_1, n_2)):
    resultado = mcd(n_1, n_2)
    print(f"El máximo común divisor de {n_1} y {n_2} es {resultado}") 
else: 
    print('No existe mcd') 
```
## Ejercicio 12: Cuadrados perfectos y raíz cuadrada entera

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosIteracion/milestone/7?closed=1)

El código empleado para resolverlo es el siguiente:
 ```python
# Importo las librerías necesarias para la realización del ejercicio.
import math

# Fragmento el ejercicio en los dos apartados que se plantean.
pregunta = int(input("""Si desea obtener todos los cuadrados perfectos de un intervalo entre 0 y un parámetro introducido por usted pulse 1,
en cambio si desea realizar la raíz cuadrada de un número entero pulse 2: """))
# Procedemos con la realización del ejercicio.
if pregunta == 1:
    def cuadradosperfectos(a, b):

        if (a**2 <= b):
            print(a**2)
            cuadradosperfectos(a+1, b)
    cuadradosperfectos(
        0, int(input("Introduzca hasta que valor quiere que llegue su lista de cuadrados perfectos: ")))
elif pregunta == 2:
    a = int(input(
        "Introduzca un número entero para el cual desee obtener su raíz cuadrada: "))
    print("La raíz cuadrada de " + str(a) + " es igual a " + str(math.sqrt(a)))

else:
  print("Por favor, introduzca valores correctos (1 ó 2)")
```

