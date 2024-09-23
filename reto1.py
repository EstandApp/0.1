#Diseñado por EstandApp y MisionTic
#Reto 1
salario, horas_extras, bonificaciones = input().split()

salario = float(salario)
horas_extra = int(horas_extras)
bonificacion = int(bonificaciones)

valor_hora = salario / 170

valor_horas_extra = valor_hora*45/100

total_horas_extra = valor_horas_extra * horas_extra

recargo_horas_extra = valor_hora * horas_extra

total_bonificacion = salario*2.8/100*bonificacion

salario_total = salario + total_horas_extra + total_bonificacion + recargo_horas_extra

descuentos = salario_total*4.9/100 + salario_total*5/100 + salario_total*3/100

salario_pagar = salario_total - descuentos

print(round(salario_pagar,1), round(salario_total,1))