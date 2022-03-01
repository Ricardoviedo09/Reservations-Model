from datetime import datetime
import connection as db
from models import Reservation

def menu():
        print('''
        ***The Wow Box***
        
        1- Hacer una Reservacion
        2- Ver Reservaciones
        3- Modificar una Reservacion
        4- Eliminar Reservacion
        ''')

def insertRow(name, lastname, email, reservationDate):
    date = datetime.strptime(reservationDate, '%d/%m/%Y')
    reservation = Reservation(name=f'{name}', lastname=f'{lastname}', email=f'{email}', reservationDate=date)
    if str(date) in reservationDate:
        print("Esta fecha ya se encuentra registrada por otra persona.")
    else:
        db.session.add(reservation)
        db.session.commit()
    
def showRows():
    reservation = db.session.query(Reservation.id, Reservation.name, Reservation.lastname, Reservation.email).all()
    
    for i in reservation:
        print("ID: {}, Nombre: {}, Apellido: {}, Correo: {}".format(i.id, i.name, i.lastname, i.email))

def updateRow(id):
    print('''
          1- Actualizar el nombre
          2- Actualizar el apellido
          3- Actualizar el correo
          ''')
    option = int(input("Que desea realizar: "))
    if option == 1:
        name = input("Ingresa el nuevo nombre: ")
        db.session.query(Reservation).filter(Reservation.id == id).update(
            {
                Reservation.name: name
            }
        )
        db.session.commit()
    elif option == 2:
        lastname = input("Ingresa el nuevo apellido: ")
        db.session.query(Reservation).filter(Reservation.id == id).update(
            {
                Reservation.lastname: lastname
            }
        )
        db.session.commit()
    elif option == 3:
        email = input("Ingresa el nuevo correo: ")
        db.session.query(Reservation).filter(Reservation.id == id).update(
            {
                Reservation.email: email
            }
        )
        db.session.commit()
    
def deleteRow(id):
    db.session.query(Reservation).filter(
        Reservation.id == id
    ).delete()
    
    db.session.commit()