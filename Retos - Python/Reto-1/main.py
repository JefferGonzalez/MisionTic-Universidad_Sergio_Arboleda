salario , horas_extra , bonificacion = input().split()

if int(horas_extra) > 0 :
    horas_extra = (int(horas_extra) * ((float(salario) / 192) * 1.25))
if int(bonificacion) > 0:
    bonificacion = float(salario) * 0.05

salario_total = float(salario) + horas_extra + bonificacion
print(round((salario_total) - (salario_total * 0.085),1))