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
