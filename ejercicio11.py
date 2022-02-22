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

  
  
