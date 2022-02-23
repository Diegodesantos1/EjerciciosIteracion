def separacion(texto, separador):
  lista = texto.split(separador)
  return lista

texto = "Hola,Carlos"
print(separacion(texto, ","))
