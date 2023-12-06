from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base
from src.modelo.boletade_pago import BoletaDePago  # Asegúrate de tener la importación correcta

class CalculoSueldo(Base):
    __tablename__ = 'tabla_calculo_sueldo'

    id = Column(Integer, primary_key=True)
    bonificaciones = Column(Float)
    descuento = Column(Float)
    sueldoBasico = Column(Float)
    boleta_de_pago_id = Column(Integer, ForeignKey("tabla_boleta_de_pago.id"), nullable=False)
    boleta_de_pago = relationship(BoletaDePago, backref="calculo_sueldo")

    def __init__(self, bonificaciones, descuento, sueldoBasico):
        self.bonificaciones = bonificaciones
        self.descuento = descuento
        self.sueldoBasico = sueldoBasico

