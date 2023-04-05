#!/usr/bin/env python
# -- coding: utf-8 --


"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.

import csv
import random
from pokemon import Pokemon
from weapon_type import WeaponType




def get_data_from_user(name_file):
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      list_pokemons List of Pokemons obtained from CSV .

    Example
    -------
      >>> list_pokemons = get_data_from_user("file.csv")
    """

    list_pokemons = []
    with open (name_file, "r") as file:
      reader = csv.reader(file)
      for line in reader:
        if line[2] == "headbutt":
           list = Pokemon(int(line[0])), str(line[1]), WeaponType.HEADBUTT, int(line[3]), int(line[4]), int(line[5])
        elif line[2] == "elbow":
            list = Pokemon(int(line[0])), str(line[1]), WeaponType.ELBOW, int(line[3]), int(line[4]), int(line[5])
        elif line[2] == "kick":
            list = Pokemon(int(line[0])), str(line[1]), WeaponType.KICK, int(line[3]), int(line[4]), int(line[5])
        elif line[2] == "punch":
            list = Pokemon(int(line[0])), str(line[1]), WeaponType.PUNCH, int(line[3]), int(line[4]), int(line[5])

        list_pokemons.append(list)
        return list_pokemons
      
    



def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       List List of the Pokemons associaated to the coach that are undefeated.

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """

    if len(list_of_pokemons) == 3:
        print("1:", list_of_pokemons[0].pokemon_name, "2:", list_of_pokemons[1].pokemon_name, "3:", list_of_pokemons[2].pokemon_name)
    elif len(list_of_pokemons) == 2:
        print("1:", list_of_pokemons[0].pokemon_name, "2:", list_of_pokemons[1].pokemon_name)
    else:
        print("Careful, you only have 1 left:", list_of_pokemons[0].pokemon_name)
    
    pokemon_to_choose = int(input("Coach " + str(coach_to_ask) + " choose your Pokemon: "))
    if pokemon_to_choose == 1:
        return list_of_pokemons[0]
    elif pokemon_to_choose == 2:
        return list_of_pokemons[1]
    elif pokemon_to_choose == 3:
        return list_of_pokemons[2]
    return pokemon_to_choose





def coach_is_undefeated(list_of_pokemons):
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Boolean True if the coach has all her/his Pokemons defeated.
               False if the coach has any Pokemon that is undefeated.

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """

    if len(list_of_pokemons) == 0:
        return False
    else:
        return True


def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.

    coach1 = get_data_from_user("coach1_pokemons.csv")
    for i in coach1:
      print(i)

  
    # Get configuration for Game User 2.

    coach2 = get_data_from_user("coach2_pokemons.csv")
    for i in coach2:
        print(i)
      
    dañoRecibido1 = 0
    dañoRecibido2 = 0
    dañoInflingido1 = 0
    dañoInflingido2 = 0





    


    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:

    pokemons = [coach1, coach2]


    # Choose first pokemons

    pokemons1 = get_pokemon_in_a_list_of_pokemons("coach1", coach1)
    pokemons2 = get_pokemon_in_a_list_of_pokemons("coach2", coach2)
 

    # Main loop.

    while coach_is_undefeated(coach1) and coach_is_undefeated(coach2):
        random_number = random.randint(1, 2)
        print(random_number)
        if random_number == 1:
            print("Coach 1 attacks")
            dañoInflingido1 = pokemons1.attack(pokemons2)
            dañoRecibido2 = pokemons2.receive_damage(dañoInflingido1)
            print("The damage received by Coach 2 is: ", dañoRecibido2)
            if dañoRecibido2 >= pokemons2.pokemon_life:
                print("Coach 2 has lost the battle")
                coach2.remove(pokemons2)
                if coach_is_undefeated(coach2):
                    pokemons2 = get_pokemon_in_a_list_of_pokemons("coach2", coach2)
                else:
                    break
            else:
                print("Coach 2 has not lost the battle")
        else:
            print("Coach 2 attacks")
            dañoInflingido2 = pokemons2.attack(pokemons1)
            dañoRecibido1 = pokemons1.receive_damage(dañoInflingido2)
            print("The damage received by Coach 1 is: ", dañoRecibido1)
            if dañoRecibido1 >= pokemons1.pokemon_life:
                print("Coach 1 has lost the battle")
                coach1.remove(pokemons1)
                if coach_is_undefeated(coach1):
                    pokemons1 = get_pokemon_in_a_list_of_pokemons("coach1", coach1)
                else:
                    break
            else:
                print("Coach 1 has not lost the battle")

            if pokemons1.pokemon_life <= 0:
                coach1.remove(pokemons1)
                if coach_is_undefeated(coach1):
                    pokemons1 = get_pokemon_in_a_list_of_pokemons("coach1", coach1)
                else:
                    break
            elif pokemons2.pokemon_life <= 0:
                coach2.remove(pokemons2)
                if coach_is_undefeated(coach2):
                    pokemons2 = get_pokemon_in_a_list_of_pokemons("coach2", coach2)
                else:
                    break
                





        
        





    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")


    print("Game User 2:")



# Checking whether this module is executed just itself alone.
if __name__ == "_main_":
    main()


# EOF



