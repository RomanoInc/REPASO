#Pide un color favorito. Si no es "rojo",muestra "Ese no es el color que esperaba".

continuar = True
while continuar:
    color = input("ingresa color: ")
    
    if color == "rojo":
        print("color acertado")
        break
    else:
        print("ese no es el color que esperaba")
        pregunta = input("desea continuar?: ")
        if pregunta != "Si":
            continuar = False


        