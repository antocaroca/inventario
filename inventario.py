from tabulate import tabulate

class Producto:
    def __init__(self, nombre, cantidad, precio, id_producto, categoria, peso):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.id_producto = id_producto
        self.categoria = categoria
        self.peso = peso

    def registrar(self):
        with open("inventario.txt", "a") as inv:
            inv.write("\n" + f"{self.nombre}")
            inv.write(";" + f"{self.cantidad}")
            inv.write(";" + f"{self.precio}")
            inv.write(";" + f"{self.id_producto}")
            inv.write(";" + f"{self.categoria}")
            inv.write(";" + f"{self.peso}")
        inv.close()
        
class Inventario(Producto):
    nombre = input("Ingrese nombre del producto:")
    cantidad = input("Ingrese cantidad del producto:")
    precio = input("Ingrese precio del producto:")
    id_producto = input("Ingrese id numérico del producto:")
    categoria = input("Ingrese categoría del producto:")
    peso = input("Ingrese peso del producto:")

    producto1 = Producto(nombre, cantidad, precio, id_producto, categoria, peso)
    producto1.registrar()
    print()
    print("****producto:", producto1.nombre, "se ha registrado correctamente****\n")

    def buscar_nombre_id_precio():
        archivo = open("inventario.txt", "r")
        nombres = {}
        headers=["Nombre", "Cantidad", "Precio", "ID", "Categoría", "Peso"]
        nombre_id_precio = input("\n ingrese nombre, id o precio del producto: \n")

        for linea in archivo:
            nombre, cantidad, precio, id_numerico, categoria, peso = linea.strip().split(";")
                        
            if  nombre  not in nombres:
                nombres[nombre] = []
            nombres[nombre].append((nombre, cantidad, precio, id_numerico, categoria, peso))
            if id_numerico  not in nombres:
                nombres[id_numerico] = []
            nombres[id_numerico].append((nombre, cantidad, precio, id_numerico, categoria, peso))
            if precio  not in nombres:
                nombres[precio] = []
            nombres[precio].append((nombre, cantidad, precio, id_numerico, categoria, peso))

        print()
        print(tabulate(nombres[nombre_id_precio], headers=headers)) 
    

    def buscar_categoria():
        archivo = open("inventario.txt", "r")
        categorias = {}
        headers2=["Categoría", "Cantidad", "Precio", "ID", "Nombre", "Peso"] 
        categoria_a_buscar = input("\nIngrese la categoria del producto: \n")

        for linea in archivo:
            nombre, cantidad, precio, id_numerico, categoria, peso = linea.strip().split(";")

            if  categoria  not in categorias:
                categorias[categoria] = []
            categorias[categoria].append((categoria, cantidad, precio, id_numerico, nombre, peso))

        print(tabulate(categorias[categoria_a_buscar], headers=headers2))  
        archivo.close()

    def buscar_top_9():
        archivo = open("inventario.txt", "r")
        cantidades = {}
        cant = {}
        headers3=["Cantidad", "Categoría", "Precio", "ID", "Nombre", "Peso"] 
       
        for linea in archivo:
            nombre, cantidad, precio, id_numerico, categoria, peso = linea.strip().split(";")
        
            if  cantidad not in cantidades:
                cantidades[cantidad] = []
            cantidades[cantidad].append((cantidad, categoria, precio, id_numerico, nombre, peso))

        #print(tabulate(cantidades[cantidad], headers=headers3))
        for  value in cantidades.values():
            for i in value: = []
                if int(i[0]) < 10:
                    cant[i] = []
                cant[]
                    print(i[0], i[1], i[2], i[3], i[4], i[5])
                    #print(tabulate((i[0], i[1], i[2], i[3], i[4], i[5]), headers=headers3))
        
        archivo.close()
        
Inventario.buscar_nombre_id_precio()
print()
Inventario.buscar_categoria()
print()
Inventario.buscar_top_9()