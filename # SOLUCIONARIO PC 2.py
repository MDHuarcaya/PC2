# SOLUCIONARIO PC 2

## Ejercicio 1

listado_num = []

for i in range(1500,2701):
    if i%7==0 and i%5==0:
        listado_num.append(i)
print(f"Los numeros divisibles por 7 y multiplos de 5 son: {listado_num}")


## Ejercicio 2

filas = 9 
for i in range(filas):
    if i <= filas/2:
        print("* "* (i+1))
    else:
        print("* "* (filas-i))


## Ejercicio 3

print("Bienvenido al menú interactivo")
num_ingresados =[] 
pares = 0
impares = 0

while True:
    print("""¿Desea ingresar un numero?
    1) SI
    2) NO""")
   
    opcion = input() # me devuelve un string ''
    if opcion == '1':
        numero = int(input("Introduce un número: "))
        num_ingresados.append(numero)
        
    elif opcion == '2':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    
for i in num_ingresados:
    if i%2 == 0:
        pares +=1
    else:
        impares +=1

print(f"Numeros ingresados; {num_ingresados}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")


## Ejercicio 4

list_alumnos = [] 
# Solicitar número de alumnos
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

def ingresar_alumnos(n):
    for alumno in range(n):
        nombre = input(f"Ingrese el nombre del alumno {alumno+1}: ")
        notas = []
        for calificacion in range(3):
            nota = float(input(f"Ingrese la nota {calificacion+1} de {nombre}: "))
            notas.append(nota)
        
        datos_alumno = {'Alumno': nombre, 'Notas': notas}
        list_alumnos.append(datos_alumno)
    
    return list_alumnos

# Ingresar datos de los alumnos
alumnos = ingresar_alumnos(cantidad_alumnos)

def list(alumnos):
    print("Listado de los alumnos:")
    for nombre in alumnos:
        print(f"Alumno: {nombre['Alumno']}, Notas: {nombre['Notas']}")

# Mostrar el listado completo de los alumnos
list(alumnos)


## Ejercicio 5

numero = int(input("Ingresar numero: "))
digito = int(input("Ingresar digito: "))

def contar_digitos(numero, digito):
    # Convertir el número a una cadena de texto para poder contar los dígitos
    numero_str = str(numero)
    # Usar el método count() para contar cuántas veces aparece el dígito en el número
    cantidad = numero_str.count(str(digito))
    return cantidad
# Llamar a la función para contar el dígito en el número ingresado
cantidad_digitos = contar_digitos(numero, digito)

# Mostrar el resultado
print(f"numero ingresado: {numero} y digito: {digito}")
print(f"Cantidad de veces {digito} en el número: {cantidad_digitos}")


## Ejercicio 6

def fibonacci(n, a=0, b=1):
    if a > n:
        return []
    else:
        return [a] + fibonacci(n, b, a + b)

print(f"La serie de Finobacci entre 0 y 50 es:", fibonacci(50))


## Ejercicio 7

def evaluar_primo(n):
    es_primo=True
    for i in range(2,n):
        if n % i==0:
            es_primo=False

    return es_primo


# solicitar al usuario numero 
numero = int(input("Ingresar un numero: "))

es_primo = evaluar_primo(n=numero)

if es_primo and numero>1:
    print("el numero es primo")
else:
    print("El numero no es primo")


## Ejercicio 8
    
def calcular_fact(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact
numero = int(input("Ingresar un numero: "))
print(f"El factorial del numero", numero, "es:", calcular_fact(numero))


## Ejercicio 9

import re
cadena = input("por favor, Ingrese una cadena de texto: ")
def eliminar_vocales(texto):
    return re.sub(r'[aeiouAEIOU]', '', texto)

print("Texto sin vocales:", eliminar_vocales(cadena))


## Ejercicio 10


