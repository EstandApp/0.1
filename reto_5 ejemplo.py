
def agregar(base_datos,productos):
    llave = productos[0]
    productos.pop(0)
    base_datos[llave] = productos
    return

def borrar(base_datos,productos):
    base_datos.pop(productos[0])
    return

def actualizar(base_datos,productos):
    llave = productos[0]
    productos.pop(0)
    base_datos[llave] = productos
    return


def leer_datos():
    operacion = input()
    productos = input().split()
    productos[0] = int(productos[0])
    productos[2] = float(productos[2])
    productos[3] = int(productos[3])
    return operacion, productos


def principal(): 
    base_datos = {
            1: ['Manzanas', 5000.0, 25],
            2: ['Limones', 2300.0, 15],
            3: ['Peras', 2700.0, 33],
            4: ['Arandanos', 9300.0, 5],
            5: ['Tomates', 2100.0, 42],
            6: ['Fresas', 4100.0, 3],
            7: ['Helado', 4500.0, 41],
            8: ['Galletas', 500.0, 8],
            9: ['Chocolates', 3500.0, 80],
            10: ['Jamon', 15000.0, 10] 
        }
        
    operacion, productos = leer_datos()
    if operacion == 'AGREGAR':
        agregar(base_datos,productos)
    elif operacion == 'BORRAR':
        borrar(base_datos,productos)
    elif operacion == 'ACTUALIZAR':
        actualizar(base_datos,productos)


principal()

