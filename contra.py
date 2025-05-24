import re

regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]+')

print("Ingresa palabras para validar (escribe 'salir' para terminar):")

while True:
    palabra = input("Ingresa tú contraseña").strip()
    
    if palabra.lower() == "salir":
        break
    
    if regex.fullmatch(palabra):
        print("Válida: cumple con los requisitos.")
    else:
        print("Inválida: debe contener al menos una minúscula, una mayúscula y un número.")
