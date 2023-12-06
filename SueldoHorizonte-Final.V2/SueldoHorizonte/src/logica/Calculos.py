def ingreso_datos():
    while True:
        try:
            nombreTrabajador = input("Ingrese el nombre del trabajador: ")
            sueldoBasico = float(input("Ingrese el sueldo básico: "))
            diasFalta = int(input("Ingrese el número de días de faltas: "))
            minutosTardanza = int(input("Ingrese el número de minutos de tardanza: "))
            horasExtras = float(input("Ingrese el número de horas extras: "))
            break  # Si todos los datos son válidos, salimos del bucle

        except ValueError:
            print("Error: Ingresa un valor válido. Intenta nuevamente.")

    return nombreTrabajador, sueldoBasico, diasFalta, minutosTardanza, horasExtras

def calcular_bonificaciones(sueldoBasico, horasExtras):
    pagoHorasExtras = 1.50 * horasExtras
    movilidad = 1000
    bonificacionSuplementaria = 0.03 * sueldoBasico
    bonificaciones = movilidad + bonificacionSuplementaria + pagoHorasExtras

    return bonificaciones

def calcular_descuentos(remuneracionComputable, diasFalta, minutosTardanza):
    descuentoFaltas = remuneracionComputable / 30 * diasFalta
    descuentoTardanzas = remuneracionComputable / 30 / 8 / 60 * minutosTardanza
    descuentos = descuentoFaltas + descuentoTardanzas

    return descuentos

def calcular_sueldo_a_pagar(sueldoBasico, bonificaciones, descuentos):
    sueldoNeto = sueldoBasico + bonificaciones - descuentos

    return sueldoNeto

def imprimir_boleta_pago(nombreTrabajador, sueldoNeto):
    # Nombre del archivo
    nombre_archivo = f"boleta_pago_{nombreTrabajador.replace(' ', '_')}.txt"

    # Abrir el archivo en modo escritura
    with open(nombre_archivo, 'w') as archivo:
        # Escribir los datos en el archivo
        archivo.write("Sueldo Horizonte""\n")
        archivo.write("Nombre del trabajador: " + nombreTrabajador + "\n")
        archivo.write("Sueldo a pagar: " + str(sueldoNeto) + "\n")

    print(f"Se ha generado la boleta de pago en el archivo: {nombre_archivo}")

# Código principal
nombreTrabajador, sueldoBasico, diasFalta, minutosTardanza, horasExtras = ingreso_datos()
bonificaciones = calcular_bonificaciones(sueldoBasico, horasExtras)
descuentos = calcular_descuentos(sueldoBasico, diasFalta, minutosTardanza)
sueldoNeto = calcular_sueldo_a_pagar(sueldoBasico, bonificaciones, descuentos)
imprimir_boleta_pago(nombreTrabajador, sueldoNeto)

