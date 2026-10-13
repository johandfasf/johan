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
# Problema 1: Temperature converter and range flag
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
# Problema 2:   Work hours and overtime payment
#
# Descripción:
# Este programa calcula el pago semanal de un
# trabajador según sus horas trabajadas y su
# pago por hora. Si trabaja más de 40 horas,
# las horas extra se pagan al 150%.
#
# Entradas:
# hours_worked: Horas trabajadas (float).
# hourly_rate: Pago por hora (float).
#
# Salidas:
# Regular pay: Pago de las horas normales.
# Overtime pay: Pago de las horas extra.
# Total pay: Pago total de la semana.
# Has overtime: True si trabajó más de 40 horas.
#
# Validaciones:
# Las horas trabajadas no pueden ser negativas.
# El pago por hora debe ser mayor que cero.
# Verificar que ambos datos sean numéricos.
#
# Casos de prueba:
# 1. Normal: hours_worked = 45, hourly_rate = 100
#    Regular pay: 4000.0
#    Overtime pay: 750.0
#    Total pay: 4750.0
#    Has overtime: true
#
# 2. Borde: hours_worked = 40, hourly_rate = 100
#    Regular pay: 4000.0
#    Overtime pay: 0.0
#    Total pay: 4000.0
#    Has overtime: false
#
# 3. Error: hours_worked = -5, hourly_rate = 100
#    Error: invalid input
#
# 
try:
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        has_overtime = hours_worked > 40

        print("Regular pay:", round(regular_pay, 2))
        print("Overtime pay:", round(overtime_pay, 2))
        print("Total pay:", round(total_pay, 2))
        print("Has overtime:", str(has_overtime).lower())

except ValueError:
    print("Error: invalid input")

#========================================================================
#
# Problema 3: Discount eligibility with booleans
# 
# Descripción:
# Este programa determina si un cliente puede
# recibir un descuento del 10% en su compra.
# El descuento se aplica si es estudiante,
# adulto mayor o compra $1000 o más.
#
# Entradas:
# purchase_total: Total de la compra (float).
# is_student_text: Indica si es estudiante (YES/NO).
# is_senior_text: Indica si es adulto mayor (YES/NO).
#
# Salidas:
# Discount eligible: True si obtiene descuento.
# Final total: Total a pagar después del descuento.
#
# Validaciones:
# El total de la compra no puede ser negativo.
# Las respuestas deben ser YES o NO.
# Verificar que el total sea un número válido.
#
# Casos de prueba:
# 1. Normal: purchase_total = 500
#    is_student_text = YES, is_senior_text = NO
#    Discount eligible: true
#    Final total: 450.0
#
# 2. Borde: purchase_total = 1000
#    is_student_text = NO, is_senior_text = NO
#    Discount eligible: true
#    Final total: 900.0
#
# 3. Error: purchase_total = 500
#    is_student_text = MAYBE, is_senior_text = NO
#    Error: invalid input
#


try:
    purchase_total = float(input("Enter purchase total: "))

    is_student_text = input("Are you a student? (YES/NO): ").strip().upper()
    is_senior_text = input("Are you a senior? (YES/NO): ").strip().upper()

    if (purchase_total < 0 or
        is_student_text not in ("YES", "NO") or
        is_senior_text not in ("YES", "NO")):
        print("Error: invalid input")
    else:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = (
            is_student or is_senior or purchase_total >= 1000.0
        )

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", round(final_total, 2))

except ValueError:
    print("Error: invalid input")


#===================================================================================
# 
# Problema 4: Basic statistics of three integers
#
# Descripción:
# Este programa recibe tres números enteros
# y calcula su suma, promedio, valor máximo
# y mínimo. También verifica si los tres
# números son pares.
#
# Entradas:
# n1: Primer número entero (int).
# n2: Segundo número entero (int).
# n3: Tercer número entero (int).
#
# Salidas:
# Sum: Suma de los tres números.
# Average: Promedio de los números.
# Max: Número mayor.
# Min: Número menor.
# All even: True si los tres números son pares.
#
# Validaciones:
# Verificar que los tres valores sean enteros.
# Se permiten números positivos, negativos y cero.
#
# Casos de prueba:
# 1. Normal: n1 = 4, n2 = 6, n3 = 8
#    Sum: 18
#    Average: 6.0
#    Max: 8
#    Min: 4
#    All even: true
#
# 2. Borde: n1 = 0, n2 = -2, n3 = 2
#    Sum: 0
#    Average: 0.0
#    Max: 2
#    Min: -2
#    All even: true
#
# 3. Error: n1 = 5, n2 = ABC, n3 = 10
#    Error: invalid input
#

try:
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))
    n3 = int(input("Enter third integer: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3

    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = (
        n1 % 2 == 0 and
        n2 % 2 == 0 and
        n3 % 2 == 0
    )

    print("Sum:", sum_value)
    print("Average:", round(average_value, 2))
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())

except ValueError:
    print("Error: invalid input")


#=============================================================================
# 
# Problema 5: Loean eligibility (income and debtratio)
#
# Descripción:
# Este programa determina si una persona puede
# obtener un préstamo según sus ingresos mensuales,
# sus deudas y su puntaje de crédito.
# Para ser elegible debe cumplir los tres requisitos.
#
# Entradas:
# monthly_income: Ingreso mensual (float).
# monthly_debt: Deuda mensual (float).
# credit_score: Puntaje de crédito (int).
#
# Salidas:
# Debt ratio: Proporción de deuda respecto al ingreso.
# Eligible: True si cumple todos los requisitos.
#
# Validaciones:
# El ingreso mensual debe ser mayor que cero.
# La deuda mensual no puede ser negativa.
# El puntaje de crédito no puede ser negativo.
# Verificar que los datos sean numéricos.
#
# Casos de prueba:
# 1. Normal: monthly_income = 10000
#    monthly_debt = 3000, credit_score = 700
#    Debt ratio: 0.3
#    Eligible: true
#
# 2. Borde: monthly_income = 8000
#    monthly_debt = 3200, credit_score = 650
#    Debt ratio: 0.4
#    Eligible: true
#
# 3. Error: monthly_income = 0
#    monthly_debt = 2000, credit_score = 700
#    Error: invalid input
#
try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000.0 and
            debt_ratio <= 0.4 and
            credit_score >= 650
        )

        print("Debt ratio:", round(debt_ratio, 2))
        print("Eligible:", str(eligible).lower())

except ValueError:
    print("Error: invalid input")


#============================================================
# 
# Porblema 6: Body Mass index (BMI) and category flag
#
# Descripción:
# Este programa calcula el índice de masa corporal
# utilizando el peso y la estatura de una persona.
# También determina mediante valores booleanos
# a cuál de los tres rangos pertenece el resultado.
#
# Entradas:
# weight_kg: Peso en kilogramos (float).
# height_m: Estatura en metros (float).
#
# Salidas:
# BMI: Índice de masa corporal con dos decimales.
# Underweight: True si el BMI es menor que 18.5.
# Normal: True si el BMI está entre 18.5 y 25.
# Overweight: True si el BMI es mayor o igual a 25.
#
# Validaciones:
# El peso debe ser mayor que cero.
# La estatura debe ser mayor que cero.
# Verificar que ambos datos sean numéricos.
# Evitar divisiones entre cero.
#
# Casos de prueba:
# 1. Normal: weight_kg = 70, height_m = 1.75
#    BMI: 22.86
#    Underweight: false
#    Normal: true
#    Overweight: false
#
# 2. Borde: weight_kg = 72, height_m = 1.80
#    BMI: 22.22
#    Underweight: false
#    Normal: true
#    Overweight: false
#
# 3. Error: weight_kg = 70, height_m = 0
#    Error: invalid input
#
# 

try:
    weight_kg = float(input("Enter weight in kg: "))
    height_m = float(input("Enter height in meters: "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)

        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", round(bmi, 2))
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())

except ValueError:
    print("Error: invalid input")


# ======================================================================
# 
# Conclusiones
#
# En esta práctica aprendí a utilizar los números
# enteros y decimales para realizar diferentes cálculos.
# También comprendí cómo las comparaciones generan
# valores booleanos para tomar decisiones con if.
# Aprendí que es importante validar los datos antes
# de utilizarlos para evitar errores en el programa.
# Además, practiqué el uso de and, or y not para
# comprender cómo se pueden combinar condiciones.
# Estos conocimientos pueden aplicarse en situaciones
# como calcular pagos, descuentos y préstamos.
#
# ===========================================================================
#
# Referencias 
#
# 1. Python Software Foundation. (2026).
#    Built-in Types.
#    https://docs.python.org/3/library/stdtypes.html
#
# 2. Python Software Foundation. (2026).
#    Floating-Point Arithmetic: Issues and Limitations.
#    https://docs.python.org/3/tutorial/floatingpoint.html
#
# 3. Python Software Foundation. (2026).
#    More Control Flow Tools.
#    https://docs.python.org/3/tutorial/controlflow.html
#
# 4. Python Software Foundation. (2026).
#    Errors and Exceptions.
#    https://docs.python.org/3/tutorial/errors.html
#
# 5. Python Software Foundation. (2026).
#    Built-in Functions.
#    https://docs.python.org/3/library/functions.html
#
# 6. Python Software Foundation. (2026).
#    An Informal Introduction to Python.
#    https://docs.python.org/3/tutorial/introduction.html
#
#