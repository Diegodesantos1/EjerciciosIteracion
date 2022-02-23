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
  