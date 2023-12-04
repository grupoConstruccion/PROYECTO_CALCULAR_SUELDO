def calcular_pago_horas_extras(sueldo_basico, horas_extras):
    return 1.50 * horas_extras * sueldo_basico / 30 / 8

def calcular_pago_hora_normal(sueldo_basico):
    return sueldo_basico / 30 / 8

def calcular_bonificaciones(sueldo_basico, horas_extras):
    movilidad = 1000
    bonificacion_suplementaria = 0.03 * sueldo_basico
    pago_horas_extras = calcular_pago_horas_extras(sueldo_basico, horas_extras)

    return movilidad + bonificacion_suplementaria + pago_horas_extras

def calcular_remuneracion_computable(sueldo_basico):
    movilidad = 1000
    bonificacion_suplementaria = 0.03 * sueldo_basico

    return sueldo_basico + movilidad + bonificacion_suplementaria

if __name__ == "__main__":
    sueldo_basico = float(input("Ingrese el sueldo básico: "))
    horas_extras = float(input("Ingrese la cantidad de horas extras trabajadas: "))

    pago_horas_extras = calcular_pago_horas_extras(sueldo_basico, horas_extras)
    pago_hora_normal = calcular_pago_hora_normal(sueldo_basico)
    bonificaciones = calcular_bonificaciones(sueldo_basico)
    remuneracion_computable = calcular_remuneracion_computable(sueldo_basico)

    print(f"Pago por horas extras: {pago_horas_extras}")
    print(f"Pago por una hora normal: {pago_hora_normal}")
    print(f"Bonificaciones totales: {bonificaciones}")
    print(f"Remuneración Computable: {remuneracion_computable}")
