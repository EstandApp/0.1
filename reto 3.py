registro = int(input())

resultado = []

for x in range(registro):
    caracteristicas = input().split() 
    if int(caracteristicas[0]) > 100 and \
       int (caracteristicas[1]) <= 9  and \
       int (caracteristicas[2]) <= 6  and \
       int (caracteristicas[3]) == 0 :
        resultado.append(int(caracteristicas[4]))  
    if len(resultado) == 0 :
        resultado.append("NO DISPONIBLE")
        resultado.pop(0)

if len(resultado) == 0:
        resultado.append("NO DISPONIBLE") 
        print("NO DISPONIBLE")      
else:
    print(*resultado, sep="\n") 