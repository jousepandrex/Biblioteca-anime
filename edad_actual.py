#Práctica 1
palabra = input("Por favor ingrese una palabra: ")
contador = 0
while contador < 10:
    contador += 1
    print(palabra)

#Práctica 2
edad = int(input("Por favor ingrese su edad: "))
contador = 0
while contador <= edad:
    contador += 1
    print(contador)

#Práctica 3
num = int(input("Por favor ingrese un número entero: "))
contador = 0
for i in range(1, num+1, 2):
    print(i, end=", ")