# ISIT 333 - Lab 9
# November 28, 2021
# Hoang Do

# import pandas
import pandas as pd

def display_menu():
    print()
    print("* * * * * * * MAIN MENU * * * * * * *")
    print("1 - Display all of the Pokemon by Name, Type, Generation")
    print("2 - Display all of the Pokemon by Name, HP, Attack, Defense, Speed")
    print("3 - Display all of the GRASS type Pokemon")
    print("4 - Display all of the Pokemon in order of HP (highest to lowest)")
    print("5 - Display all of the Pokemon in order of NAME A-Z")
    print("6 - Display all of the LEGENDARY Pokemon")
    print("7 - Search the Pokemon by Name")
    print("8 - Exit the program")

def display_by_name_type_and_generation(pokemon):
    print(pokemon[["Name", "Type 1", "Type 2", "Generation"]])

def display_by_name_hp_attack_defense_and_speed(pokemon):
    print(pokemon[["Name", "HP", "Attack", "Defense", "Speed"]])

# this function displays all of the GRASS type Pokemon, could be Type 1 GRASS or Type 2 GRASS
def display_grass_type(pokemon):
    # create a dataFrame displaying all of the GRASS type Pokemon
    frame_grass_type_pokemon = pd.DataFrame(pokemon[(pokemon["Type 1"] == "Grass")|(pokemon["Type 2"] == "Grass")])
    # print the dataFrame
    print(frame_grass_type_pokemon[["Name", "Type 1", "Type 2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"]])

def display_hp_highest_to_lowest_order(pokemon):
    # create a dataFrame displaying all of the Pokemon in order of HP (highest to lowest)
    frame_hp_highest_to_lowest_order_pokemon = pd.DataFrame(pokemon.sort_values("HP", ascending=False))
    # print the dataFrame
    print(frame_hp_highest_to_lowest_order_pokemon[["Name", "HP", "Type 1", "Type 2", "Total", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"]])

def display_name_in_a_to_z_order(pokemon):
    # create a dataFrame displaying all of the Pokemon in order of NAME A-Z
    frame_name_in_a_to_z_order_pokemon = pd.DataFrame(pokemon.sort_values("Name"))
    # print the dataFrame
    print(frame_name_in_a_to_z_order_pokemon[["Name", "Type 1", "Type 2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"]])

def display_legendary(pokemon):
    # create a dataFrame of all the LEGENDARY Pokemon
    frame_legendary_pokemon = pd.DataFrame(pokemon[pokemon["Legendary"] == True])
    # print the dataFrame
    print(frame_legendary_pokemon[["Name", "Legendary", "Type 1", "Type 2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation"]])

def search_by_name(pokemon):
    try:
        while True:
            continuance = input("Please press any key to continue or press e to exit. ")
            print()

            if continuance.lower() != "e":
                search_input = input("Input a Pokemon name: ")
                print()
                frame_associated_data_result = pd.DataFrame(pokemon[pokemon["Name"] == search_input])

                
                # .shape[0] returns the number of rows of the DataFrame
                # if there are 0 rows result
                if frame_associated_data_result.shape[0] == 0:
                    print("Sorry, record not found. Please try again!\n")
                else:
                    print(f"Bravo! Here is the record for {search_input}:\n")
                    print(frame_associated_data_result)
                    print()
            else:
                print("Thank you!")
                break
    except:
        print("Something went wrong. Please try again!")

def main():
    print("Welcome to The Amazing Pokemon Data Program.")
    # save data to a variable "pokemon"
    pokemon = pd.read_csv("pokemon.csv")

    while True:
        display_menu()
        print()
        command = input("Command: ")
        print()
        if command == "1":
            display_by_name_type_and_generation(pokemon)
        elif command == "2":
            display_by_name_hp_attack_defense_and_speed(pokemon)
        elif command == "3":
            # GRASS type Pokemon could be Type 1 GRASS or Type 2 GRASS
            display_grass_type(pokemon)
        elif command == "4":
            display_hp_highest_to_lowest_order(pokemon)
        elif command == "5":
            display_name_in_a_to_z_order(pokemon)
        elif command == "6":
            display_legendary(pokemon)
        elif command == "7":
            search_by_name(pokemon)
        elif command == "8":
            break
        else:
            print("Unknown command. Please try again.")

    # farewell message
    print("Thank you for using The Amazing Pokemon Data Program. See you later!")

if __name__ == "__main__":
    main()