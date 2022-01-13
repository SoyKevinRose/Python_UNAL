#ciclo for2 ejercicio
print("Algoritmo doble ciclo para Secciones Empresa ")
k = int (input("Digite la cantidad secciones empresa "))

rangoS = range(1, k+1)

totalF = 0

for s in rangoS:
  print(" Sección ", s)
  m = int (input ("Digite la cantidad de Empleados "))
  for emp in range(1, m+1):
    print("Empleado ", emp, " de la sección ", s)
    familiares = int (input("Digite cantidad familiares empleado "))
    totalF = totalF + familiares

print(" Total Familiares es  ", totalF)
print(" Total Subsidio mes ", totalF * 15000)
print("Total subsidio a medio año", totalF * 15000 * 6)