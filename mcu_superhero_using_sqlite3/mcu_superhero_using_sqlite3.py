# import the sqlite3 database module
import sqlite3

def initialize_database(conn, cursor):
    # check if the mcu_superheroes table already exists, if so, drop it so we can start with a new table
    cursor.execute("DROP TABLE IF EXISTS mcu_superheroes;")

    # create the table if it doesn't already exist
    # primary keys are automatically created in sqlit3 and referenced as rowid 
    cursor.execute("CREATE TABLE mcu_superheroes (first_name TEXT, last_name TEXT, alias TEXT, species TEXT, citizenship TEXT, birth_year TEXT, status TEXT, portrayed_by TEXT)")

    # create some initial records of data
    cursor.execute("INSERT INTO mcu_superheroes VALUES ('Tony', 'Stark', 'Iron Man', 'Human', 'American', '1970', 'Deceased', 'Robert Downey, Jr.')")

    cursor.execute("INSERT INTO mcu_superheroes VALUES ('Carol', 'Danvers', 'Captain Marvel', 'Human/Kree Hybrid', 'American / Kree Imperial (formerly)', '1964', 'Alive', 'Brie Larson')")

    cursor.execute("INSERT INTO mcu_superheroes VALUES ('Stephen', 'Strange', 'Doctor Strange', 'Human', 'American', '1982', 'Alive', 'Benedict Cumberbatch')")

    cursor.execute("INSERT INTO mcu_superheroes VALUES ('Shang-Chi', 'Xu', 'N/A', 'Human', 'Chinese (formerly) / American', '1999', 'Alive', 'Simu Liu')")

    cursor.execute("INSERT INTO mcu_superheroes VALUES ('Natasha', 'Romanoff', 'Black Widow', 'Human', 'Russian (formerly) / American', '1984', 'Deceased', 'Scarlett Johansson')")

    return cursor

def list_name_and_alias(conn, cursor):
    print("Superheroes and their aliases")
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, alias FROM mcu_superheroes")

    # store the results of a the query to a list called superheroess
    superheroes = cursor.fetchall()

    # loop through the results of the query
    for this_superhero in superheroes:
      print(this_superhero[0], this_superhero[1], this_superhero[2], this_superhero[3])

def list_species_and_citizenship(conn, cursor):
    print("Superheroes, their species and citizenship")
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, species, citizenship FROM mcu_superheroes")

    # store the results of a the query to a list called superheroes
    superheroes = cursor.fetchall()

    # loop through the results of the query
    for this_superhero in superheroes:
      print(this_superhero[0], this_superhero[1], this_superhero[2], this_superhero[3], this_superhero[4])

def list_birth_year_and_status(conn, cursor):
    print("Superheroes, their birth year and status")
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, birth_year, status FROM mcu_superheroes")

    # store the results of a the query to a list called superheroess
    superheroes = cursor.fetchall()

    # loop through the results of the query
    for this_superhero in superheroes:
      print(this_superhero[0], this_superhero[1], this_superhero[2], this_superhero[3], this_superhero[4])

def list_portrayed_by(conn, cursor):
    print("Superheroes and the actors/actresses who portray them")
    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, portrayed_by FROM mcu_superheroes")

    # store the results of a the query to a list called superheroess
    superheroes = cursor.fetchall()

    # loop through the results of the query
    for this_superhero in superheroes:
      print(this_superhero[0], this_superhero[1], this_superhero[2], this_superhero[3])

def add_new_superhero(conn, cursor):
    print("Let's add new MCU superhero to the database following instructions below:\n")
    print("If you know that the superhero doesn't possess any attributes, \nplease input \"N/A\"!")
    print()
    print("If you're not sure about any attributes, \nplease input \"Not sure\"!")
    print()

    input_first_name = input("First name: ")
    input_last_name = input("Last name: ")
    input_alias = input("Alias: ")
    input_species = input("Species: ")
    input_citizenship = input("Citizenship: ")
    input_birth_year = input("Birth year: ")
    input_status = input("Status: ")
    input_portrayed_by = input("Portrayed by: ")

    # prepare your insert statement using ? for each item that you will insert
    sql = """
        INSERT INTO mcu_superheroes (first_name, last_name, alias, species, citizenship, birth_year, status, portrayed_by)
        VALUES (?,?,?,?,?,?,?,?)
        """

    cursor.execute(sql, (input_first_name, input_last_name, input_alias, input_species, input_citizenship, input_birth_year, input_status, input_portrayed_by))

    print(f"{input_first_name} {input_last_name} added. Thank you!")
    return cursor


def display_menu():
    print()
    print("* * * * * * * COMMAND MENU * * * * * * *")
    print("0 - Initialize/reset database. (Careful this will wipe all data of new added superheroes)")
    print("1 - List superheroes and their alias")
    print("2 - List superheroes, their species and citizenship")
    print("3 - List superheroes, their birth year and status")
    print("4 - List superheroes and actors/actresses who portray them")
    print("5 - Add new superhero to the database")
    print("6 - Exit the program")

def main():
    print("Welcome to MCU Superheroes Database")
    # create a connection to the database file
    conn = sqlite3.connect("myDatabase.db")
    # create a cursor that we will use to move through the database 
    cursor = conn.cursor()
    while True:
        display_menu()
        print()
        command = input("Command: ")
        print()
        if command == "0":
            cursor = initialize_database(conn, cursor)
            print("Database reset successfully!")
        elif command == "1":
            list_name_and_alias(conn, cursor)
        elif command == "2":
            list_species_and_citizenship(conn, cursor)
        elif command == "3":
            list_birth_year_and_status(conn, cursor)
        elif command == "4":
            list_portrayed_by(conn, cursor)
        elif command == "5":
            cursor = add_new_superhero(conn, cursor)
        elif command == "6":
            break
        else:
            print("Unknown command. Please try again.")

    # save the updates/inserts to the database
    conn.commit()
    # close the connection
    conn.close()
    # farewell message
    print("Thank you for using MCU superhero database. See you later for more interesting about Marvel Cinematic Universe!")

if __name__ == "__main__":
    main()