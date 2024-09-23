class SistemadeMultas:
    def __init__(self,Distancia,VelMax,Tiempo):  
        self.Distancia = Distancia #distancia entre las dos camaras (mtr)
        self.VelMax = VelMax #velocidad permirtida en el trayecto (k/h)
        self.Tiempo = Tiempo #tiempo en el que tardo el condutor en recorrer distancia (segundos)
        
    def datosconductor(self):
        self.velocidadconductor = (self.Distancia / 1000) / (self.Tiempo /3600)
        self.nuevavel = VelMax * 1.2
    def multas(self):
        if self.Distancia < 0 or self.VelMax < 0 or self.Tiempo < 0:
            print("ERROR")
        elif self.velocidadconductor <= self.VelMax:
            print ("OK" ) 
        elif self.velocidadconductor > self.VelMax and self.velocidadconductor < self.nuevavel:
            print("MULTA")
        elif self.velocidadconductor >= self.nuevavel:
            print("CURSO SENSIBILIZACION")             


Distancia,VelMax,Tiempo = input().split()
Distancia = float(Distancia)
VelMax = float(VelMax)
Tiempo = float(Tiempo)