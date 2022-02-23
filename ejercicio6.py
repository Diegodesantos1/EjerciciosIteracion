import random
from tabulate import tabulate
from tabulate import TableFormat

print("""
Bienvenido a la plataforma de acceso de su cuenta bancaria,
  Introduzca los datos que se le van a pedir a continuación
  """)
nombre = str(input("Por favor, introduzca su nombre completo: "))
min = 5000
max = 100000
saldo = random.uniform(min, max)
gastomax = saldo / 4
gastos = random.uniform(min, gastomax)
tabla = [[" Nombre", "Saldo total ", "Gastos "], [ nombre, saldo, gastos]]
print(tabulate(tabla, headers="firstrow", tablefmt="grid"))
familia = int(input("Si desea acceder a los datos de la cuenta familiar pulse 1, en caso contrario pulse 0: "))
