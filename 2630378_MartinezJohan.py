# Manejo de Strings en Python


    #portada
    #nombre: Johan Martinez Estrella()
    #matricula: 2630378
    #grupo: IM-3

#Resumen Ejecutivo


    #un string en python es una secuencia de caracter, es de texto presentada
    #por el tipo de dato str. los strings son inmutables, por lo que su contenido
    #no puede modificarse directamente, las operaciones crean nuevos strings.
    #Entre las operacion basicas estan la concatenacion, conocer la longitud,
    #indexar, hacer slicing, buscar, remplazar, dividir, y unir texto.
    #validar las entradas es importante porque evita datos vacios o
    #con formatos incorrectos que puedan provocar resultados inesperados.
    #la normalicacion con strip(), lower(), upper() o title() hace que
    #el texto sea mas facil de comparar y mostrar de forma constante.

#Principios y buenas practicas


    #Los strings son inmutables: cualquier modificacion
    #crea un nuevo string
    #usa strip() y lower() para normalizar texto antes 
    #de compararlo
    #evita numeros magicos en indices y documenta
    #que obtiene cada slice
    #usa metodos integrados de strings en lugar de 
    #repetir logica basica
    #primero valida que la entrada no este vacia
    #y desupues su formato
    #usa nombres de variables claros y mensajes
    #de error faciles de entender

"==============================================================================0"
#problema 1 Formtaeador de nombre ccompleto
#descripcion: normalizar el nombre completo
#de una persona, eliminar espacios extra
#convertirlo a Title case y genera sus iniciales

#entradas:
#-full_name:(string)

#salidas:
#-nombre formateado
#-iniciales

#valicaciones:
#-la entrada no debe estar vacia despues del strip()
#-la entrada debe contener al menos dos palabras

#caso de prueba:
#1-Normal: "johan martinez estrella" -> "Johan Martinez Estrella", "JME"
#2-borde: "Ana Lopez" -> "Ana Lopez", "AL"
#3-error: " " -> entrada vacia/ invalida

full_name = "johan martinez"
full_name = full_name.strip()

if not full_name:
    print("error: invalid input - name cannot be empty")
else:
    name_parts = full_name.split()

    if len(name_parts) < 2:
        print("error: invalid input - enter at least two words")
    else:
        formatted_name = " ".join(name_parts).title()
        initials = "".join(part[0].upper() for part in name_parts)

        print(f"formatted name: {formatted_name}")
        print(f"initials: {initials}")


"----------------------------------------------------------------------------------------"
#problema 2 validador simple de correo electronico
#Descripción:
#Valida si una dirección de correo tiene un formato básico correcto:
#- Contiene exactamente un '@'.
#- Después del '@' debe haber al menos un '.'.
#- No contiene espacios en blanco.
#Si el correo es válido, también muestra el dominio (la parte después de '@').

#Entradas:
#- email_text (string).

#Salidas:
#- "Valid email: true" o "Valid email: false"
#- Si es válido: "Domain: <domain_part>"

#Validaciones:
#- email_text no vacío tras strip().
#- Contar cuántas veces aparece '@'.
#- Verificar que no haya espacios (no debe haber " " en email_text).

#Operaciones clave sugeridas: strip(), count(), find(), slicing, in, not in

email_text = "2630378@gmail.com"
email_text = email_text.strip()

if not email_text:
    print("error: invalid input - email cannot be empty")
elif " " in email_text:
    print("valid email:false")
elif email_text.count("@") != 1:
    print("valid email:false")
else:
    local_part, domain_part = email_text.split("@", 1)
    if "." not in domain_part:
        print("valid email:false")
    else:
        print("valid email:true")
        print(f"domain: {domain_part}")


"----------------------------------------------------------------------------------------"


#problema 3
#Descripción:
#Determina si una frase es un palíndromo, es decir, se lee igual de 
# izquierda a derecha y de derecha a izquierda, 
# ignorando espacios y mayúsculas/minúsculas.

#Ejemplos:
#- "Anita lava la tina" -> palíndromo.
#- "Hola mundo" -> no palíndromo.

#Entradas:
#- phrase (string).

#Salidas:
#- "Is palindrome: true" o "Is palindrome: false"
#- (Opcional) Mostrar también la versión normalizada de la frase.

#Validaciones:
#- phrase no vacía tras strip().
#- Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).

#Operaciones clave sugeridas: lower(), replace(" ", ""), slicing inverso text[::-1], comparación ==.

# Casos de prueba:
# 1) Normal: "Anita lava la tina" -> true
# 2) Borde: "aba" -> true
# 3) Error: "  " -> entrada inválida

phrase = "johan estudia en clase de charly"
phrase = phrase.strip()

if not phrase:
    print("error: invalid input - phrase cannot be empty")
else:
    normalized_phrase = phrase.lower().replace(" ", "")

    if len(normalized_phrase) < 3:
        print("error: invalid input - phrase must have at least 3 characters")
    else:
        reversed_phrase = normalized_phrase[::-1]
        is_palindrome = normalized_phrase == reversed_phrase

        result = "true" if is_palindrome else "false"
        print(f"normalized phrase:{normalized_phrase}")
        print(f"is palindrome:{result}")


"----------------------------------------------------------------------------------------"

#problema 4
#Descripción:
#Dada una oración, el programa debe:
#1) Normalizar espacios (quitar espacios al principio y al final).
#2) Separar las palabras por espacios.
#3) Mostrar:
#   - Número total de palabras.
#   - Primera palabra.
#   - Última palabra.
#   - Palabra más corta y más larga (por longitud).

#Entradas:
#- sentence (string).

#Salidas:
#- "Word count: <n>"
#- "First word: <...>"
#- "Last word: <...>"
#- "Shortest word: <...>"
#- "Longest word: <...>"

#Validaciones:
#- Oración no vacía tras strip().
#- Debe contener al menos una palabra válida después de split().

#Operaciones clave sugeridas: strip(), split(), len(), 
# recorrer la lista de palabras para encontrar mínima y máxima longitud.
# Casos de prueba:
# 1) Normal: "Python is easy to learn"
# 2) Borde: "Hello"
# 3) Error: "   " -> entrada inválida

sentence = "python es un lenguaje de programacion"
sentence = sentence.strip()

if not sentence:
    print("error: invalid input - sentence cannot be empty")
else:
    words = sentence.split()
    if not words:
        print("error: invalid input - no valid words found")
    else:
        shortest_word = min(words, key=len)
        longest_word = max(words, key=len)

        print(f"word count: {len(words)}")
        print(f"first word: {words[0]}")
        print(f"last word: {words[-1]}")
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")


"---------------------------------------------------------------------------------------"

#problema 5: clasificador de seguridad de contraseñas
#Descripción:
#Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

#Ejemplo de reglas:
#- Weak: longitud < 8 o todo en minúsculas o muy simple.
#- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
#- Strong: longitud >= 8 y contiene al menos:
#- una letra mayúscula,
#- una letra minúscula,
#- un dígito,
#- un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

#Entradas:
#- password_input (string).

#Salidas:
#- "Password strength: weak"
#- "Password strength: medium"
#- "Password strength: strong"

#Validaciones:
#- No aceptar contraseña vacía.
#- Verificar longitud con len().

#Operaciones clave sugeridas:
#- Recorrer carácter por carácter.
#- Métodos: isupper(), islower(), isdigit(), isalnum().
#- Uso de banderas booleanas (has_upper, has_lower, etc.).
# Casos de prueba:
# 1) Normal: "Hello123" -> medium
# 2) Borde: "Aa1!aaaa" -> strong
# 3) Error: "" -> entrada inválida

password_input = "MARTINEZ689"

if password_input == "":
    print("Error: invalid input - password cannot be empty")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    password_length = len(password_input)

    if (
        password_length >= 8
        and has_upper
        and has_lower
        and has_digit
        and has_symbol
    ):
        strength = "strong"
    elif (
        password_length >= 8
        and ((has_upper and has_lower) or has_digit)
    ):
        strength = "medium"
    else:
        strength = "weak"

    print(f"Password strength: {strength}")

"-----------------------------------------------------------"

# Problema 6: Formateador de etiqueta de producto
# Descripción:
# Crear una etiqueta de producto en una sola línea usando el formato indicado.
# La etiqueta final debe tener exactamente 30 caracteres. Si es más corta,
# se agregan espacios al final. Si es más larga, se recorta a 30 caracteres.
#
# Entradas:
# - product_name (string)
# - price_value (string o número)
#
# Salidas:
# - Etiqueta con exactamente 30 caracteres
#
# Validaciones:
# - El nombre del producto no debe estar vacío después de strip().
# - El precio debe poder convertirse a un número positivo.
#
# Casos de prueba:
# 1) Normal: "Notebook", "25.50"
# 2) Borde: "A", "0.01"
# 3) Error: "Pen", "-5" -> precio inválido

product_name = "Keyboard"
price_value = "25.99"

product_name = product_name.strip()

if not product_name:
    print("Error: invalid input - product name cannot be empty")
else:
    try:
        numeric_price = float(str(price_value).strip())

        if numeric_price <= 0:
            print("Error: invalid input - price must be positive")
        else:
            price_text = str(price_value).strip()
            label = f"Product: {product_name} | Price: ${price_text}"

            if len(label) < 30:
                label = label + (" " * (30 - len(label)))
            else:
                label = label[:30]

            print(f'Label: "{label}"')
            print(f"Label length: {len(label)}")
    except (ValueError, TypeError):
        print("Error: invalid input - price must be a number")


#El manejos de strings es esencial porque los programas reciben,
#procesan, validad y muestran datos de texto constantemente.
#Metodos como strip(), lower(), split() y join() ayudan a normalizar
#y organizar el texto antes de compararlo o proscesarlo.
#Normalizar el texto reduce problemas causados por espacios extra o diferencias
#entre mayusculas y minusculas, haciendo las validaciones mas confiables
#las validaciones claras ayudan a evitar datos vacios, incompletos o incorrectos.
#aprendi que los strings son inmutables, por lo que sus metodos devuelven
#nuevos strings en lugar de modificar directamente el original.
#El sclicing es util para extraer partes especificas  de un string y para
#operaciones como invertir texto mediante [::-1]

#Referencias


#1-Documentacion de Python - bluit-in Types; text sequence Type-- str
#2-Documentacion de Python - common String Oprations
#3-Documentacion de Python - built-in Functions: len()
#4-Documentacion de Python - Strings Methods
#5-Documentacion de Python - input and Output
#6-Documentacion de python - errors and exceptions

