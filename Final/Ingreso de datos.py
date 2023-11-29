nombre_trabajador = input("Ingrese el nombre del trabajador: ")
sueldo_basico = float(input("Ingrese el sueldo básico del trabajador: "))

dias_falta = int(input("Ingrese los días de falta del trabajador: "))
minutos_tardanza = int(input("Ingrese los minutos de tardanza del trabajador: "))

horas_extras = float(input("Ingrese las horas extras trabajadas: "))

sueldo_total = sueldo_basico

penalizacion_faltas = 100 * dias_falta
penalizacion_tardanza = 0.5 * minutos_tardanza

sueldo_total -= penalizacion_faltas
sueldo_total -= penalizacion_tardanza

pago_horas_extras = 1.5 * sueldo_basico * horas_extras

sueldo_total += pago_horas_extras

print("\nResumen del trabajador", nombre_trabajador)
print("Sueldo básico: $", sueldo_basico)
print("Días de falta: ", dias_falta)
print("Minutos de tardanza: ", minutos_tardanza)
print("Horas extras trabajadas: ", horas_extras)
print("\n---Resumen de pago---")
print("Sueldo total a pagar: $", sueldo_total)
