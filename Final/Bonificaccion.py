def calcular_pago_horas_extras(sueldo_basico, horas_extras):
    return 1.50 * horas_extras * sueldo_basico / 30 / 8

def calcular_pago_hora_normal(sueldo_basico):
    return sueldo_basico / 30 / 8

def calcular_bonificaciones(sueldo_basico, horas_extras):
    movilidad = 1000
    bonificacion_suplementaria = 0.03 * sueldo_basico
    pago_horas_extras = calcular_pago_horas_extras(sueldo_basico, horas_extras)

    return movilidad + bonificacion_suplementaria + pago_horas_extras

def calcular_remuneracion_computable(sueldo_basico, horas_extras):
    movilidad = 1000
    bonificacion_suplementaria = 0.03 * sueldo_basico
    pago_horas_extras = calcular_pago_horas_extras(sueldo_basico, horas_extras)

    return sueldo_basico + movilidad + bonificacion_suplementaria + pago_horas_extras

if __name__ == "__main__":
    sueldo_basico = float(input("Ingrese el sueldo básico: "))
    horas_extras = float(input("Ingrese la cantidad de horas extras trabajadas: "))

    pago_horas_extras = calcular_pago_horas_extras(sueldo_basico, horas_extras)
    pago_hora_normal = calcular_pago_hora_normal(sueldo_basico)
    bonificaciones = calcular_bonificaciones(sueldo_basico, horas_extras)
    remuneracion_computable = calcular_remuneracion_computable(sueldo_basico, horas_extras)

    print(f"Pago por horas extras: {pago_horas_extras}")
    print(f"Pago por una hora normal: {pago_hora_normal}")
    print(f"Bonificaciones totales: {bonificaciones}")
    print(f"Remuneración Computable: {remuneracion_computable}")

# Caso de prueba 1: Obtener bonificaciones con datos simulados
sueldo_test_1 = 3000  # Sueldo básico
horasExtras_test_1 = 10  # Horas extras trabajadas
bonificaciones_obtenidas_1 = calcular_bonificaciones(sueldo_test_1, horasExtras_test_1)
bonificaciones_esperadas_1 = 1000 + 0.03 * sueldo_test_1 + 1.50 * horasExtras_test_1 * sueldo_test_1 / 30 / 8

# Caso de prueba 2: Obtener remuneración computable con datos simulados
sueldo_test_2 = 4000  # Sueldo básico
horasExtras_test_2 = 5  # Horas extras trabajadas
remuneracion_obtenida_2 = calcular_remuneracion_computable(sueldo_test_2, horasExtras_test_2)
remuneracion_esperada_2 = sueldo_test_2 + 1000 + 0.03 * sueldo_test_2 + 1.50 * horasExtras_test_2 * sueldo_test_2 / 30 / 8

# Mostrar resultados de casos de prueba
print("\nCasos de prueba:")
print("Caso 1 - Bonificaciones:")
print(f"Bonificaciones esperadas: {bonificaciones_esperadas_1}")
print(f"Bonificaciones obtenidas: {bonificaciones_obtenidas_1}")
print("\nCaso 2 - Remuneración Computable:")
print(f"Remuneración Computable esperada: {remuneracion_esperada_2}")
print(f"Remuneración Computable obtenida: {remuneracion_obtenida_2}")
