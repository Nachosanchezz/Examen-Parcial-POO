import csv
from pokemon import Pokemon


def get_data_from_coach(coach_1_pokemons, csv):
    pokemons_coach_1 = []
    with open("coach_1_pokemons.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            id = row [0]
            name = row [1]
            weapon = row [2]
            health = row [3]
            attack = row [4]
            defense = row [5]
            p = Pokemon(id, name, weapon, health, attack, defense)
            pokemons_coach_1.append(p)
            
    
    pokemons_coach_2 = []
    with open("coach_2_pokemons.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            id = row [0]
            name = row [1]
            weapon = row [2]
            health = row [3]
            attack = row [4]
            defense = row [5]
            p = Pokemon(id, name, weapon, health, attack, defense)
            pokemons_coach_2.append(p)

    return pokemons_coach_1, pokemons_coach_2

def get_pokemon_in_a_list_of_pokemons(pokemon):
    print("Choose a Pokemon from the list: ")
    for i, p in enumerate(pokemon):
        print(i, p.name)

    while True:
        try:
            opcion = int(input("Choose a Pokemon: "))
            if opcion < 0 or opcion > len(pokemon):
                print("The option is not valid. Try again.")
            else:
                return pokemon[opcion - 1]
        except ValueError:
            print("The option is not valid. Try again.")

def coach_is_undefeated(list_of_pokemons):
    for p in list_of_pokemons:
        if p.health > 0:
            return False
    return True

def main():
    coach1 = get_data_from_coach("coach_1_pokemons.csv")
    coach2 = get_data_from_coach("coach_2_pokemons.csv")

    coach_playing1 = coach1[0]
    coach_playing2 = coach2[0]

    print("The coach 1 has chosen " + coach_playing1.name)
    print("The coach 2 has chosen " + coach_playing2.name)

    while True:
        if not coach_is_undefeated(coach1):
            print("The coach 2 has won")
            break
        if not coach_is_undefeated(coach2):
            print("The coach 1 has won")
            break
    
    
    if __name__ == "__main__":
      main()



