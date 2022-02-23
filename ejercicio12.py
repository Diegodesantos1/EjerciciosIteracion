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