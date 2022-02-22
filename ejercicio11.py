print("¿Qué forma quieres ejecutar? 1(Euclides) o 2 (sumas y restas)")
eleccion=int(input())
if eleccion == 1:
  print("Introduzca el primer número")
  n1=int(input())
  print("Introduzca el segundo número")
  n2 = int(input())
  def mcd(n1, n2):
      if n2 == 0:
          return n1
      return mcd (n2, n1 % n2)
  resultado =mcd(n1,n2)
  print(f"El mcd de {n1} y {n2} es {resultado}")
elif eleccion == 2: