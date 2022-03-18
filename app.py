import connection as db
import methods as mt
from sqlalchemy_utils import create_database, database_exists
        
if __name__ == '__main__':
    if not database_exists(db.engine.url):
        create_database(db.engine.url)
    db.Base.metadata.create_all(db.engine)

    while True:
        mt.menu()
        option = int(input("Escoge una opcion: "))
        if option == 1:
            name = input("Ingrese el nombre: ")
            lastname = input("Ingrese el Apellido: ")
            email = input("Ingrese el Correo: ")
            dateReservation = input("Ingrese una fecha de reservacion dd/mm/aaaa: ")
            mt.insertRow(name, lastname, email, dateReservation)
        elif option == 2:
            mt.showRows()
        elif option == 3:
            mt.showRows()
            print("")
            id = int(input("Ingrese el ID identificador de la reservacion: "))
            mt.updateRow(id)
        elif option == 4:
            mt.showRows()
            print("")
            id = int(input("Ingrese el ID identifiacor de la reservacion: "))
            mt.deleteRow(id)