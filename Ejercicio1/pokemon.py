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

        while True:
            try:
                self.ataque = int(self.ataque)
                break
            except ValueError:
                print("El ataque debe ser un número")
                self.ataque = input("Ingrese el ataque: ")

        while True:
            try:
                self.defensa = int(self.defensa)
                break
            except ValueError:
                print("La defensa debe ser un número")
                self.defensa = input("Ingrese la defensa: ")

        while True:
            if self.salud < 0 or self.salud > 100:
                self.salud = input("La salud debe estar entre 0 y 100: ")
            else:
                break
        
        while True:
            if self.ataque < 0 or self.ataque > 10:
                self.ataque = input("El ataque debe estar entre 0 y 10:")
            else:
                break

        while True:
            if self.defensa < 0 or self.defensa > 10:
                self.defensa = input("La defensa debe estar entre 0 y 10:")
            else:
                break

        while True:
            if self.arma == "Puñetazo" or self.arma == "Patada" or self.arma == "Codazo" or self.arma == "Cabezazo":
                break
            else:
                self.arma = input("El arma debe ser Puñetazo, Patada, Codazo o Cabezazo: ")

    def esta_vivo(self):
            if self.salud > 0:
                return True
            else:
                return False
    
    def defender(self, puntos_de_daño):
        if self.defensa > puntos_de_daño:
            return False
        else:
            self.salud -= puntos_de_daño - self.defensa
            print(self.salud)
            return True
    
    def atacar(self, pokemon_al_que_atacar):
        return pokemon_al_que_atacar.defender(self.ataque)
        


    def __str__(self):
        return "El pokemon con ID: " + str(self.ID) + " de nombre: " + self.nombre + " tiene un arma: " + self.arma + " y una salud de: " + str(self.salud)
    
pokemon1 = Pokemon(1, "Pikachu", "Puñetazo", 100, 10, 10)
pokemon2 = Pokemon(2, "Charmander", "Patada", 100, 10, 10)
print(pokemon1)
print(pokemon1.atacar(pokemon2))
    

                
                

            



    