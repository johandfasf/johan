# PRÁCTICA DE PYTHON: LISTAS, TUPLAS Y DICCIONARIOS
#
#
# Estudiante: Martinez Estrella
# Matrícula: 2630378
# Grupo: I-M3
# Materia: Programación
#
# Tema: Listas, Tuplas y Diccionarios
# 
# 
# ======================================================================
#
# Resmen Ejecutivo
#
# En Python existen diferentes estructuras que permiten
# almacenar y organizar información.
# Las listas son colecciones ordenadas que se pueden modificar.
# Las tuplas también almacenan datos ordenados, pero no permiten
# cambiar sus elementos después de crearlas.
# Los diccionarios guardan información mediante claves y valores.
# Esto permite encontrar datos utilizando una clave específica.
# En esta práctica se resolverán seis problemas utilizando
# estas estructuras, sus operaciones y sus validaciones.
# También se aplicarán en catálogos, registros y estadísticas.
#
#=======================================================================
#
# Principios y Buenas Practicas
#
# 1. Utilizar listas cuando sea necesario agregar, eliminar
#    o modificar elementos de una colección.
#
# 2. Utilizar tuplas para guardar información que no debe
#    cambiar, como coordenadas o fechas.
#
# 3. Utilizar diccionarios cuando se necesite encontrar
#    información mediante una clave, como nombres o códigos.
#
# 4. Evitar modificar una lista mientras se recorre con
#    un ciclo for para prevenir errores.
#
# 5. Utilizar claves descriptivas en los diccionarios
#    para identificar fácilmente los datos almacenados.
#
# 6. Escribir código ordenado, con variables descriptivas
#    y mensajes fáciles de comprender.
#
#=========================================================================
#
# Problema 1: Lista básica de compras
#
# Descripción:
# Este programa permite crear una lista de compras
# a partir de productos ingresados por el usuario.
# También permite agregar un producto nuevo,
# contar los elementos y buscar un producto.
#
# Entradas:
# initial_items_text: Productos separados por comas.
# new_item: Producto que se agregará a la lista.
# search_item: Producto que se desea buscar.
#
# Salidas:
# Items list: Lista completa de productos.
# Total items: Cantidad de productos en la lista.
# Found item: True o False según la búsqueda.
#
# Validaciones:
# Verificar que la lista inicial no esté vacía.
# Eliminar espacios adicionales en los productos.
# Verificar que el nuevo producto no esté vacío.
# Verificar que el producto buscado no esté vacío.
#
# Casos de prueba:
# 1. Normal: "apple,banana", "orange", "banana"
#    Resultado esperado: 3 productos, Found item: true.
# 2. Límite: "apple", "banana", "orange"
#    Resultado esperado: 2 productos, Found item: false.
# 3. Error: "", "banana", "apple"
#    Resultado esperado: Error: invalid input.
#
initial_items_text = input("Enter shopping items: ").strip()

if initial_items_text == "":
    print("Error: invalid input")
else:
    items_list = initial_items_text.split(",")
    clean_items = []

    for item in items_list:
        item = item.strip()

        if item != "":
            clean_items.append(item)

    items_list = clean_items

    if len(items_list) == 0:
        print("Error: invalid input")
    else:
        new_item = input("Enter new item: ").strip()

        if new_item == "":
            print("Error: invalid input")
        else:
            items_list.append(new_item)

            search_item = input("Enter item to search: ").strip()

            if search_item == "":
                print("Error: invalid input")
            else:
                is_in_list = search_item in items_list
                total_items = len(items_list)

                print("Items list:", items_list)
                print("Total items:", total_items)
                print("Found item:", str(is_in_list).lower())

#===========================================================================================
#  Problema 2: Tuplas y cálculos de coordenadas
# 
# Descripción:
# Este programa almacena las coordenadas de dos puntos
# utilizando tuplas. Calcula la distancia entre ellos
# y encuentra las coordenadas de su punto medio.
#
# Entradas:
# x1, y1: Coordenadas del primer punto.
# x2, y2: Coordenadas del segundo punto.
#
# Salidas:
# Distance: Distancia entre los dos puntos.
# Midpoint: Coordenadas del punto medio.
#
# Validaciones:
# Verificar que las coordenadas sean números válidos.
#
# Casos de prueba:
# 1. Normal: Punto A (0, 0), punto B (3, 4).
#    Resultado esperado: Distance = 5, Midpoint = (1.5, 2.0).
# 2. Límite: Punto A (2, 2), punto B (2, 2).
#    Resultado esperado: Distance = 0, Midpoint = (2.0, 2.0).
# 3. Error: Ingresar texto en lugar de una coordenada.
#    Resultado esperado: Error: invalid input.
#

import math

try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = math.sqrt(
        (point_b[0] - point_a[0]) ** 2
        + (point_b[1] - point_a[1]) ** 2
    )

    midpoint = (
        (point_a[0] + point_b[0]) / 2,
        (point_a[1] + point_b[1]) / 2
    )

    print("Distance:", distance)
    print("Midpoint:", midpoint)

except ValueError:
    print("Error: invalid input")

#========================================================================
#
# 
# Problema 3: Catálogo de productos
# 
#
# Descripción:
# Este programa almacena productos en un diccionario,
# incluyendo su precio y cantidad disponible.
# Permite buscar un producto y calcular el valor
# total de su inventario.
#
# Entradas:
# product_name: Nombre del producto.
# price: Precio unitario del producto.
# quantity: Cantidad disponible.
# search_product: Producto que se desea consultar.
#
# Salidas:
# Product information: Información del producto.
# Inventory value: Valor total del inventario.
#
# Validaciones:
# Verificar que el nombre del producto no esté vacío.
# Verificar que el precio sea un número válido y positivo.
# Verificar que la cantidad sea un entero no negativo.
# Verificar que el producto buscado exista.
#
# Casos de prueba:
# 1. Normal: Producto "apple", precio 10, cantidad 5.
#    Resultado esperado: Inventory value = 50.
# 2. Límite: Precio 0, cantidad 0.
#    Resultado esperado: Inventory value = 0.
# 3. Error: Introducir texto en lugar del precio.
#    Resultado esperado: Error: invalid input.
#

try:
    product_name = input("Enter product name: ").strip()

    if product_name == "":
        print("Error: invalid input")
    else:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        if price < 0 or quantity < 0:
            print("Error: invalid input")
        else:
            products = {
                product_name: {
                    "price": price,
                    "quantity": quantity
                }
            }

            search_product = input(
                "Enter product to search: "
            ).strip()

            if search_product in products:
                product_info = products[search_product]

                inventory_value = (
                    product_info["price"]
                    * product_info["quantity"]
                )

                print("Product information:", product_info)
                print("Inventory value:", inventory_value)
            else:
                print("Error: product not found")

except ValueError:
    print("Error: invalid input")

#
#=================================================================================
#
#
# Problema 4: Registro de calificaciones
#
# Descripción:
# Este programa almacena estudiantes y sus calificaciones
# utilizando un diccionario con listas.
# Calcula el promedio de cada estudiante y muestra
# sus calificaciones.
#
# Entradas:
# student_name: Nombre del estudiante.
# grades: Lista de calificaciones.
#
# Salidas:
# Student grades: Calificaciones del estudiante.
# Average grade: Promedio de sus calificaciones.
#
# Validaciones:
# Verificar que el nombre no esté vacío.
# Verificar que las calificaciones sean números válidos.
# Verificar que las calificaciones estén entre 0 y 100.
# Verificar que se ingrese al menos una calificación.
#
# Casos de prueba:
# 1. Normal: Calificaciones 80, 90, 100.
#    Resultado esperado: Average grade = 90.
# 2. Límite: Calificación 0.
#    Resultado esperado: Average grade = 0.
# 3. Error: Introducir texto en lugar de una calificación.
#    Resultado esperado: Error: invalid input.
#

try:
    student_name = input("Enter student name: ").strip()

    if student_name == "":
        print("Error: invalid input")
    else:
        grades_text = input(
            "Enter grades separated by commas: "
        ).strip()

        if grades_text == "":
            print("Error: invalid input")
        else:
            grades = [
                float(grade.strip())
                for grade in grades_text.split(",")
            ]

            if (
                len(grades) == 0
                or any(grade < 0 or grade > 100 for grade in grades)
            ):
                print("Error: invalid input")
            else:
                students = {
                    student_name: grades
                }

                average_grade = sum(grades) / len(grades)

                print("Student grades:", students[student_name])
                print("Average grade:", average_grade)

except ValueError:
    print("Error: invalid input")

#
#================================================================================
#
#
# Problema 5: Conteo de palabras
# 
#
# Descripción:
# Este programa recibe una oración y separa sus
# palabras utilizando una lista.
# Después, utiliza un diccionario para contar cuántas
# veces aparece cada palabra.
#
# Entradas:
# sentence: Oración ingresada por el usuario.
#
# Salidas:
# Words list: Lista de palabras de la oración.
# Word frequencies: Cantidad de apariciones por palabra.
# Total words: Número total de palabras.
#
# Validaciones:
# Verificar que la oración no esté vacía.
# Ignorar diferencias entre mayúsculas y minúsculas.
# Eliminar signos de puntuación básicos.
#
# Casos de prueba:
# 1. Normal: "hello world hello"
#    Resultado esperado: hello = 2, world = 1.
# 2. Límite: "python"
#    Resultado esperado: python = 1.
# 3. Error: Introducir una oración vacía.
#    Resultado esperado: Error: invalid input.
#

import string

sentence = input("Enter a sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    cleaned_sentence = sentence.lower()

    for punctuation in string.punctuation:
        cleaned_sentence = cleaned_sentence.replace(
            punctuation, ""
        )

    words_list = cleaned_sentence.split()
    word_frequencies = {}

    for word in words_list:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

    total_words = len(words_list)

    print("Words list:", words_list)
    print("Word frequencies:", word_frequencies)
    print("Total words:", total_words)

#================================================================================
# Problema 6: Agenda de contactos
# 
#
# Descripción:
# Este programa administra una agenda de contactos
# utilizando un diccionario.
# Permite agregar, buscar y eliminar contactos.
#
# Entradas:
# action: Acción que desea realizar el usuario.
# contact_name: Nombre del contacto.
# phone_number: Número telefónico del contacto.
#
# Salidas:
# Contact added: Confirmación de contacto agregado.
# Phone number: Número telefónico encontrado.
# Contact deleted: Confirmación de contacto eliminado.
#
# Validaciones:
# Verificar que el nombre no esté vacío.
# Verificar que el número telefónico no esté vacío.
# Comprobar que el contacto exista antes de buscarlo
# o eliminarlo.
# Verificar que la acción sea válida.
#
# Casos de prueba:
# 1. Normal: Agregar, buscar y eliminar un contacto.
#    Resultado esperado: Las tres operaciones funcionan.
# 2. Límite: Buscar un contacto inexistente.
#    Resultado esperado: Error: contact not found.
# 3. Error: Ingresar una acción no válida.
#    Resultado esperado: Error: invalid action.
#

contacts = {}

action = input(
    "Choose an action (ADD, SEARCH, DELETE): "
).strip().upper()

if action == "ADD":
    contact_name = input("Enter contact name: ").strip()
    phone_number = input("Enter phone number: ").strip()

    if contact_name == "" or phone_number == "":
        print("Error: invalid input")
    else:
        contacts[contact_name] = phone_number
        print("Contact added")

elif action == "SEARCH":
    contact_name = input("Enter contact name: ").strip()

    if contact_name == "":
        print("Error: invalid input")
    elif contact_name in contacts:
        print("Phone number:", contacts[contact_name])
    else:
        print("Error: contact not found")

elif action == "DELETE":
    contact_name = input("Enter contact name: ").strip()

    if contact_name == "":
        print("Error: invalid input")
    elif contact_name in contacts:
        del contacts[contact_name]
        print("Contact deleted")
    else:
        print("Error: contact not found")

else:
    print("Error: invalid action")

print("Contacts:", contacts)

#Conclusiones

#3En esta práctica aprendí un poco más sobre cómo utilizar las listas, tuplas y diccionarios en Python. Al realizar los ejercicios pude entender mejor para qué sirve cada uno y cómo se pueden utilizar para guardar y organizar diferentes tipos de información.

#También pude practicar algunas cosas que ya había visto anteriormente, como los ciclos, las condiciones y las operaciones. Algunos ejercicios fueron un poco más complicados que otros, pero me ayudaron a comprender mejor cómo funcionan estas estructuras y cómo aplicarlas en diferentes situaciones.

#En general, esta actividad me sirvió para seguir practicando Python y conocer otras formas de trabajar con los datos dentro de un programa.

#Referencias

#- Python Software Foundation. (s. f.). Tutorial de Python. https://docs.python.org/es/3/tutorial/
#- Python Software Foundation. (s. f.). Estructuras de datos. https://docs.python.org/es/3/tutorial/datastructures.html
#- W3Schools. (s. f.). Python Lists. https://www.w3schools.com/python/python_lists.asp
#- W3Schools. (s. f.). Python Tuples. https://www.w3schools.com/python/python_tuples.asp
#- W3Schools. (s. f.). Python Dictionaries. https://www.w3schools.com/python/python_dictionaries.asp
