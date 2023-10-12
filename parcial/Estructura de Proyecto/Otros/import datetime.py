import datetime

SUELDO_MINIMO = 1000

def calcular_pago_horas_extras(horas_extras, sueldo_basico):
    return 1.5 * horas_extras * sueldo_basico / 30 / 8

def calcular_bonificaciones(horas_extras, sueldo_basico):
    bonificacion_movilidad = 1000
    bonificacion_suplementaria = 0.03 * sueldo_basico
    pago_horas_extras = calcular_pago_horas_extras(horas_extras, sueldo_basico)
    return bonificacion_movilidad + bonificacion_suplementaria + pago_horas_extras

def calcular_descuentos(remuneracion_computable, dias_falta, minutos_tardanza):
    descuento_faltas = remuneracion_computable / 30 * dias_falta
    descuento_tardanzas = remuneracion_computable / 30 / 8 / 60 * minutos_tardanza
    return descuento_faltas + descuento_tardanzas

def calcular_sueldo_neto(sueldo_basico, bonificaciones, descuentos):
    return sueldo_basico + bonificaciones - descuentos

def imprimir_boleta_pago(nombre_trabajador, sueldo_basico, bonificaciones, descuentos, sueldo_neto):
    print("Boleta de pago")
    print("Nombre del trabajador:", nombre_trabajador)
    print("Sueldo básico:", sueldo_basico)
    print("Bonificaciones:", bonificaciones)
    print("Descuentos:", descuentos)
    print("Sueldo neto:", sueldo_neto)

def preguntar_si_ingresar_nuevamente():
    respuesta = input("¿Desea ingresar datos nuevamente? (si/no): ").lower()
    return respuesta == "si"

while True:
    nombre_trabajador = input("Ingrese el nombre del trabajador: ")
    sueldo_basico = float(input("Ingrese el sueldo básico: "))
    dias_falta = int(input("Ingrese los días de faltas: "))
    minutos_tardanza = int(input("Ingrese los minutos de tardanzas: "))
    horas_extras = int(input("Ingrese las horas extras: "))

    bonificaciones = calcular_bonificaciones(horas_extras, sueldo_basico)
    descuentos = calcular_descuentos(sueldo_basico + bonificaciones - SUELDO_MINIMO, dias_falta, minutos_tardanza)
    sueldo_neto = calcular_sueldo_neto(sueldo_basico, bonificaciones, descuentos)

    imprimir_boleta_pago(nombre_trabajador, sueldo_basico, bonificaciones, descuentos, sueldo_neto)

    respuesta = preguntar_si_ingresar_nuevamente()
    if not respuesta:
        break