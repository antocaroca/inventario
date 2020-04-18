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
    def ingresar_datos():
        nombre = input("Ingrese nombre del producto:")
        cantidad = input("Ingrese cantidad del producto:")
        precio = input("Ingrese precio del producto:")
        id_producto = input("Ingrese id numérico del producto:")
        categoria = input("Ingrese categoría del producto:")
        peso = input("Ingrese peso del producto:")

        producto1 = Producto(nombre, cantidad, precio, id_producto, categoria, peso)
        producto1.registrar()
        print("\n****producto:", producto1.nombre, "se ha registrado correctamente****")

    def buscar_nombre_id_precio():
        archivo = open("inventario.txt", "r")
        nombres = {}
        headers=["Nombre", "Cantidad", "Precio", "ID", "Categoría", "Peso"]
        nombre_id_precio = input("\n ingrese nombre, id o precio del producto: ")
        print()

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
        print(tabulate(nombres[nombre_id_precio], headers=headers)) 
    
    def buscar_categoria():
        archivo = open("inventario.txt", "r")
        categorias = {}
        headers2=["Categoría", "Cantidad", "Precio", "ID", "Nombre", "Peso"] 
        categoria_a_buscar = input("\nIngrese la categoria del producto: ")
        print()

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
        cant_9 = {}
        headers3=["Cantidad", "Categoría", "Precio", "ID", "Nombre", "Peso"] 
    
        for linea in archivo:
            nombre, cantidad, precio, id_numerico, categoria, peso = linea.strip().split(";")
        
            if  cantidad not in cantidades:
                cantidades[cantidad] = []
            cantidades[cantidad].append((cantidad, categoria, precio, id_numerico, nombre, peso))
        
        lista_de_productos = []
        for key, value in cantidades.items():
            lista_de_productos.append((list(value)))
        
        lista_prod_final = []
        for i in lista_de_productos:
            for j in i:
                if (int(j[0])) < 10:
                    lista_prod_final.append(j)
        print("***** Lista de productos bajo 10 unidades *****\n")
        print(tabulate(lista_prod_final, headers=headers3))
        archivo.close()


Inventario.ingresar_datos()              
Inventario.buscar_nombre_id_precio()
Inventario.buscar_categoria()
print()
Inventario.buscar_top_9()