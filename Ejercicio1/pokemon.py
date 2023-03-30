class Pokemon:
    def __init__(self, ID, nombre, arma, salud, ataque, defensa):
        self.ID = ID
        self.nombre = nombre
        self.arma = arma
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa

        while True:
            try:
                self.ID  = int(self.ID)
                break
            except ValueError:
                print("El ID debe ser un número")
                self.ID = input("Ingrese el ID: ")

        while True:
            try:
                self.salud = int(self.salud)
                break
            except ValueError:
                print("La salud debe ser un número")
                self.salud = input("Ingrese la salud: ")

    