distancia, vel_permitida, tiempo=input().split()

distancia=float(distancia)  # separa las dos camaras  ---->  metros
vel_permitida=float(vel_permitida) # en el trayecto (distancia) ----> km/h
tiempo=float(tiempo) # que tarda el conducto en recorrer Distancia ----> segundos 

vel_conductor=(distancia/1000)/(tiempo/3600)  #  ---> km/h
nueva_velocidad= vel_permitida*1.2 # nueva velocidad aumentada en un 20 %

if distancia<0 or vel_permitida<0 or tiempo<0:
  print('ERROR')
elif vel_conductor<=vel_permitida:
  print(round(vel_conductor,1),'OK')
elif vel_conductor>vel_permitida and vel_conductor<nueva_velocidad:
  print(round(vel_conductor,1),'MULTA')
elif vel_conductor>=nueva_velocidad:
  print(round(vel_conductor,1),'CURSO')

