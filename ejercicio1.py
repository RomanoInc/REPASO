#Un usuario ingresa una contraseña. Verifica si la contraseña es igual a "1234".
password = 0
clave = input("Ingresa contraseña: ")

while True:
 if clave == "1234":
    print("contraseña correcta")
    break
 else:
    print("Contraseña erronea, Ingrese de nuevo: ")
    clave = input("ingresa contraseña: ")
    
 

