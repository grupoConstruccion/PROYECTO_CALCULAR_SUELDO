import unittest

def calcular_descuentos(sueldo_basico, bonificacion, dias_falta, minutos_tardanza):
    remuneracion_minima = sueldo_basico + bonificacion
    remuneracion_computable = remuneracion_minima
    
    descuento_faltas = remuneracion_computable / 30 * dias_falta
    
    descuento_tardanzas = remuneracion_computable / (30 * 8 * 60) * minutos_tardanza
    
    descuentos = descuento_faltas + descuento_tardanzas
    
    return descuentos

while True:
    try:
        sueldo_base = float(input("Ingrese el sueldo base: "))
        bonificacion = float(input("Ingrese la bonificación: "))
        dias_de_falta = int(input("Ingrese la cantidad de días de falta: "))
        minutos_de_tardanza = int(input("Ingrese la cantidad de minutos de tardanza: "))

        descuentos_totales = calcular_descuentos(sueldo_base, bonificacion, dias_de_falta, minutos_de_tardanza)
        print(f"El total de descuentos es: {descuentos_totales}")
        break
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido.")


casos_prueba = [
    (sueldo_base, bonificacion, dias_de_falta, minutos_de_tardanza),  
    (3000, 800, 5, 20),  
    (2500, 600, 4, 18),  
]

print("\nCasos de prueba:")
for idx, caso in enumerate(casos_prueba, 1):
    sueldo, bonif, faltas, tardanza = caso
    descuentos = calcular_descuentos(sueldo, bonif, faltas, tardanza)
    print(f"Caso {idx}: Descuentos = {descuentos}")
