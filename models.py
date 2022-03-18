import connection as db
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Reservation(db.Base):
    __tablename__ = 'reservations'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    reservationDate = Column(String(15), nullable=False, unique=True)
    create_at = Column(DateTime(), default=datetime.now, unique=True)
    
    def __init__(self, name, lastname, email, reservationDate):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.reservationDate = reservationDate
    
    def __str__(self):
        return self.name, self.lastname, self.email, self.reservationDate