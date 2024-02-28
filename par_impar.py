# Ejercicio #4 poder diferenciar si un numero es par o impar

# imput

print("-------------------")
X = int(imput("Digame el valor de x: "))


# Processing 

r = X % 2
if r == 0:
    rta = "PAR"
    print("el numero es par")
    
else:
    rta = "IMPAR"
    print("el numero es impar")
print("-------------------")
# output

print("-------------------")
print("El numero " + str(X) + " es " + rta)
print("---------------------------")
