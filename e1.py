'''
## Problema 1 (6pts):
Crea un módulo para validación de contraseñas. Dicho módulo deberá cumplir con los siguientes criterios de aceptación:
- La contraseña debe contener un mínimo de 8 caracteres.
- Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
- La contraseña no puede contener espacios en blanco.
- Contraseña válida: retorna “Contraseña ingresada correctamente”.
- Contraseña no válida: retorna el mensaje "La contraseña elegida no es válida".
'''

number = False
lower = False
upper = False
special = False
valid = False

# se solicita la constraseña
p = input("Ingrese su nueva contraseña: ")

# se valida longitud de la contraseña
if len(p) >= 8:
    # se valida que no contenga espacios
    if not " " in p:
        for c in p:
            # validar si el caracter es un número
            if c.isnumeric() and not number:
                number = True
            # validar si el caracter es una letra minúscula
            elif c.islower() and not lower:
                lower = True
            # validar si el caracter es una letra mayúscula
            elif c.isupper() and not upper:
                upper = True
            # validar si el caracter es un caracter especial
            elif (not c.isalnum()) and (not special):
                special = True
            
            # en caso de que ya todas las condiciones se cumplan, se sale del loop
            if number and lower and upper and special:
                valid = True
                break

# imprimir resultado
if valid:    
    print("Contraseña ingresada correctamente.")
else:
    print("La contraseña elegida no es válida.")