import random
import math

a = float(input("Ingrese a (elipse): "))
b = float(input("Ingrese b (elipse): "))
c = float(input("Ingrese c (hiperbola): "))
d = float(input("Ingrese d (hiperbola): "))
n = int(input("Ingrese cantidad de puntos: "))

ptosE = 0
ptosI = 0

for i in range(n):
  
    x = -a + (2 * a) * random.random()
    y = -b + (2 * b) * random.random()
    
    if (x**2 / a**2) + (y**2 / b**2) <= 1:
        ptosE += 1
        
        if (x**2 / c**2) - (y**2 / d**2) >= 1:
            ptosI += 1

areaE = math.pi * a * b

if ptosE > 0:
    areaI = (ptosI / ptosE) * areaE
else:
    areaI = 0

print()
print("Puntos aleatorios que cayeron dentro de la elipse:", ptosE)
print("Puntos aleatorios que cayeron dentro de la interseccion:", ptosI)
print("Area calculada elipse:", areaE)
print("Area aproximada interseccion:", areaI)