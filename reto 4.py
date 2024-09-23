def verificar_copias(billetes,K):
    billetes_repetidos = 0
    billetes_detectados = 0
    menoria = {}

    for posicion, nombre in enumerate(billetes):
        if (nombre in menoria and posicion - menoria.get(nombre) <= K):
            billetes_detectados += 1
        if (nombre in menoria):
            billetes_repetidos += 1
        menoria[nombre] = posicion
    return billetes_repetidos, billetes_detectados


N,K = input().split()
N = int(N)
K = int(K)

billetes = input().split()

billetes_repetidos, billetes_detectados = (verificar_copias(billetes,K))
print(billetes_detectados,billetes_repetidos)
