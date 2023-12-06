from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base

class BoletaDePago(Base):
    __tablename__ = 'boleta_de_pago'

    id = Column(Integer, primary_key=True)
    nombreTrabajador = Column(String)
    sueldoBasico = Column(Float)
    boletade_pago = Column(String, default='boleta_de_pago')

    def __init__(self, nombreTrabajador, sueldoBasico):
        self.nombreTrabajador = nombreTrabajador
        self.sueldoBasico = sueldoBasico
