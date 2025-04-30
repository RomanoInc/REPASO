#lista frutas pide usuarioq ue elimine una
frutas = ["manzana", "banana", "naranja", "zapote", "mango"]
print(("lista de frutas", frutas))
eliminar = input("que fruta desea eliminar?: ")
if eliminar in frutas:
    frutas.remove(eliminar)
    print(f"{eliminar} fue eliminada") 
else:
    print(f"{eliminar} no esta lista")
    print("lista actualizada", frutas)
     
