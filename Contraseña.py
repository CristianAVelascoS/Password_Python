def verificar_contraseña(password:str, password_confirmar: str) ->str:
    if len(password) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    if ' ' in password:
        raise ValueError("La contraseña no debe tener espacios.")

    if not any(char.islower() for char in password):
        raise ValueError("La contraseña debe tener al menos una letra minúscula.")
    if not any(char.isupper() for char in password):
        raise ValueError("La contraseña debe tener al menos una letra mayúscula.")
    if not any(char.isdigit()for char in  password):
        raise ValueError("La contraseña debe tener al menos un número.")
    if not any(char.isalnum() for char in password):
        raise ValueError("La contraseña debe tener al menos un caracter espacial.")
    
    if password !=password_confirmar:
        raise ValueError("las contraseñas no coinciden.")
    return "La contraseña es validad y coincide con la confirmación."
    
def ingresar_contraseña():
    password =input("Ingresa una contraseña: ")     
    password_confirmar=input("Confirma la contraseña:")
                             

    try:
        resultado = verificar_contraseña(password, password_confirmar)
        print(resultado)
    except ValueError as e:
        print(e)
ingresar_contraseña()


    
    
