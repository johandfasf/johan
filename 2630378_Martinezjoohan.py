# Practica de Python: numeros y boleanos
# 
# Alumno: Martinez Estrella
# Matrícula: 2630378
# Grupo: I-M3
# Materia: Programación
#
# Tema: Tipos numéricos y booleanos
# 
#====================================================================
# 
# Resumen Ejecutivo
#
# En Python, los tipos int y float se utilizan para
# trabajar con números enteros y decimales.
# Los booleanos representan dos valores: True y False,
# que podemos obtener al realizar comparaciones.
# Es importante validar los datos antes de utilizarlos
# para evitar errores como dividir entre cero.
# En esta práctica resolveremos seis problemas usando
# números enteros, decimales y valores booleanos.
# También identificaremos las entradas, salidas y
# validaciones necesarias para cada problema.
#
#=====================================================================
#
# Principios y Buenas Practicas 
#
# Es importante utilizar el tipo de dato adecuado
# dependiendo de la información que necesitamos.
# Por ejemplo, int para cantidades enteras y float
# para valores que pueden contener decimales.
#
# También es recomendable guardar los resultados
# de las operaciones en variables para evitar
# repetir cálculos innecesarios.
#
# Antes de realizar operaciones debemos validar
# que los datos sean correctos, evitando valores
# negativos cuando no estén permitidos.
#
# Las variables deben tener nombres descriptivos
# y los mensajes deben ser claros para el usuario.
#
# Los valores booleanos permiten representar
# condiciones: True cuando se cumple una condición
# y False cuando no se cumple.
#
# ====================================================================
#
# Problema 1:
#
# Descripción:
# Este programa convierte una temperatura en grados
# Celsius a Fahrenheit y Kelvin. También determina
# si la temperatura es alta cuando alcanza los 30 °C.
#
# Entradas:
# temp_c: Temperatura en grados Celsius (float).
#
# Salidas:
# Fahrenheit: Temperatura convertida a Fahrenheit.
# Kelvin: Temperatura convertida a Kelvin.
# High temperature: True si temp_c >= 30, False si no.
#
# Validaciones:
# Verificar que la temperatura sea un número decimal.
# No permitir temperaturas menores al cero absoluto.
#
# Casos de prueba:
# 1. Normal: temp_c = 35
#    Fahrenheit: 95.0
#    Kelvin: 308.15
#    High temperature: true
#
# 2. Borde: temp_c = 30
#    Fahrenheit: 86.0
#    Kelvin: 303.15
#    High temperature: true
#
# 3. Error: temp_c = -300
#    Error: invalid input
#
#

try:
    temp_c = float(input("Enter temperature in Celsius: "))

    temp_k = temp_c + 273.15

    if temp_k < 0:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("High temperature:", str(is_high_temperature).lower())

except ValueError:
    print("Error: invalid input")

#================================================================================
# 