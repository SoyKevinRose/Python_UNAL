#ciclo for
n = int (input(" Digite cuántos valores ingresa el usuario"))
sumaN = 0
mayores10=0

rango4 = range(1,n+1)
for m in rango4:
  print("Digite el número ", m)
  numero = int (input())
  sumaN = sumaN + numero
  if (numero >= 10):
    mayores10 = mayores10 + 1


print("La suma de los números es ", sumaN)
print ("Total mayores o iguales que 10 son ", mayores10)



