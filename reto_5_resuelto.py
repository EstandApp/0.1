
def precio_mayor(base_datos):
    mayor = list(base_datos.keys())[0]
    for i in base_datos:
        if base_datos[i][1] > base_datos[mayor][1]:
            mayor = i
    return base_datos[mayor][0]
def precio_menor(base_datos):
    menor = list(base_datos.keys())[0]
    for i in base_datos:
        if base_datos[i][1] < base_datos[menor][1]:
            menor = i
    return base_datos[menor][0]
def promedio(base_datos):
    promedio_total = 0
    for i in base_datos:
        promedio_total += base_datos[i][1]
    promedio_total /= len(base_datos)
    return promedio_total
def total_inventario(base_datos):
    total = 0.0
    for i in base_datos:
        total += base_datos[i][1] * base_datos[i][2]
    return total
def agregar(base_datos,productos):
    if productos[0] in base_datos:
        return False
    llave = productos[0]
    productos.pop(0)
    base_datos[llave] = productos
    return True
def borrar(base_datos,productos):
    if productos[0] in base_datos:
        base_datos.pop(productos[0])
        return True
    return False
def actualizar(base_datos,productos):
    if productos[0] in base_datos:
        llave = productos[0]
        productos.pop(0)
        base_datos[llave] = productos
        return True
    return False
def leer_datos():
    operacion = input()
    productos = input().split()
    productos[0] = int(productos[0])
    productos[2] = float(productos[2])
    productos[3] = int(productos[3])
    return operacion, productos
def inventario(): 
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
        error = agregar(base_datos,productos)
    elif operacion == 'BORRAR':
        error = borrar(base_datos,productos)
    elif operacion == 'ACTUALIZAR':
        error = actualizar(base_datos,productos)
    
    if error:
        print(precio_mayor(base_datos), precio_menor(base_datos),round(promedio(base_datos),1),round(total_inventario(base_datos),1))
    else:
        print("ERROR")
inventario()

