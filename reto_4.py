
def verificar_copias(monedas,K):
    monedas_repetidos = 0
    monedas_detectados = 0
    menoria = {}

    for posicion, nombre in enumerate(monedas) :
        if (nombre in menoria and posicion - menoria.get(nombre) <= K):
            monedas_detectados += 1
        if (nombre in menoria):
            monedas_repetidos += 1
        menoria[nombre] = posicion
    return monedas_repetidos, monedas_detectados


N, K = input().split()
N = int(N)
K = int(K)

lista = []

monedas = input().split()

monedas_repetidos, monedas_detectados = (verificar_copias(monedas,K))
print(monedas_repetidos, monedas_detectados)

