from datetime import date
from SueldoHorizonte.src.modelo.Boleta_pago import BoletaDePago
from SueldoHorizonte.src.modelo.Calculo_sueldo import CalculoSueldo
from SueldoHorizonte.src.modelo.Trabajador import Trabajador
from SueldoHorizonte.src.modelo.Bonificacion import Bonificacion
from SueldoHorizonte.src.modelo.Descuento import Descuento
from SueldoHorizonte.src.modelo.declarative_base import Base, engine, Session

def ingreso_datos(trabajador):
    diasFalta = int(input(f"Ingrese el número de días de faltas para {trabajador.nombre}: "))
    minutosTardanza = int(input(f"Ingrese el número de minutos de tardanza para {trabajador.nombre}: "))
    horasExtras = float(input(f"Ingrese el número de horas extras para {trabajador.nombre}: "))

    return diasFalta, minutosTardanza, horasExtras

# Generate database schema
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# create a new session
session = Session()

# create trabajador
trabajador1 = Trabajador("ene2023", "Juan Matos Solis", 3500)
trabajador2 = Trabajador("ene2023", "Fernando Salva Ortega", 3000)
trabajador3 = Trabajador("ene2023", "Manuel Taza Castro", 5000)
trabajador4 = Trabajador("ene2023", "José Perales Romero", 2500)
session.add_all([trabajador1, trabajador2, trabajador3, trabajador4])
session.commit()

# Crea descuentos
for trabajador in [trabajador1, trabajador2, trabajador3]:
    diasFalta, minutosTardanza, horasExtras = ingreso_datos(trabajador)
    descuento = Descuento(date(2023, 1, 2), diasFalta, minutosTardanza, trabajador)
    session.add(descuento)

# Crea bonificaciones
for trabajador in [trabajador1, trabajador2, trabajador3, trabajador4]:
    diasFalta, minutosTardanza, horasExtras = ingreso_datos(trabajador)
    bonificacion = Bonificacion(date(2023, 1, 1), horasExtras, 1000, trabajador)
    session.add(bonificacion)

# Crea instancias de BoletaDePago y CalculoSueldo
boleta1 = BoletaDePago("Juan Matos Solis", 3500)
calculo_sueldo1 = CalculoSueldo(1000, 200, 3500)

# Establece la relación
calculo_sueldo1.boleta_de_pago = boleta1

# Agrega a la sesión y commit
session.add_all([boleta1, calculo_sueldo1])
session.commit()
session.close()

