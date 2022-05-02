# Name: Hoang Do
# Date: December 13, 2021
# Class: ISIT 333
# Final Programming Project: Employee Database

# import the sqlite3 database module and random module
import sqlite3
import random

def initialize_or_reset_database(conn, cursor):
    # check if the employees table already exists, if so, drop it so we can start with a new table
    cursor.execute("DROP TABLE IF EXISTS Employees;")

    # create the table
    cursor.execute("CREATE TABLE Employees (employee_id_number INTEGER, first_name TEXT, last_name TEXT, street_address TEXT, city TEXT, state TEXT, zipcode TEXT, email_address TEXT, phone_number TEXT, hourly_rate REAL, department_name TEXT)")

    # build an INSERT statement with ? for values
    sqlite_initialize_param = """
        INSERT INTO Employees (employee_id_number, first_name, last_name, street_address, city, state, zipcode, email_address, phone_number, hourly_rate, department_name)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
        """

    # create some initial records of data, employee_id_numbers are randomly generated between 1000 and 9999
    employee_1 = (random.randint(1000, 9999), "Mary", "Johnson", "2254 Dane Street", "Renton", "WA", "98059", "mary.johnson@dimdom.com", "425-247-1747", 41.50, "Production")

    employee_2 = (random.randint(1000, 9999), "Daniel", "Jackson", "1475 Oakridge Farm Lane", "Seattle", "WA", "53213", "daniel.jackson@dimdom.com", "206-303-4931", 25.50, "Human Resource Management")

    employee_3 = (random.randint(1000, 9999), "Patricia", "Davis", "7855 East Lane", "Portland", "OR", "48348", "patricia.davis@dimdom.com", "257-527-8428", 19.80, "Purchasing")

    employee_4 = (random.randint(1000, 9999), "Robert", "Johnson", "6364 Riverside St.", "Westminster", "CA", "36067", "robert.johnson@dimdom.com", "542-224-8771", 30.50, "Accounting and Finance")

    employee_5 = (random.randint(1000, 9999), "Jennifer", "Garcia", "145 Wagon Ave.", "Burien", "WA", "98188", "jennifer.garcia@dimdom.com", "206-753-5387", 24.00, "Purchasing")

    employee_6 = (random.randint(1000, 9999), "Linda", "Lee", "9911 53rd Dr.", "Portland", "OR", "60089", "linda.lee@dimdom.com", "579-287-7747", 35.00, "Marketing")

    employee_7 = (random.randint(1000, 9999), "William", "Johnson", "487 Golden Star Lane", "Seattle", "WA", "98168", "william.johnson@dimdom.com", "206-870-5114", 48.50, "Marketing")

    employee_8 = (random.randint(1000, 9999), "Elizabeth", "Davis", "7124 Hillside Ave.", "Tukwila", "WA", "98170", "elizabeth.davis@dimdom.com", "206-578-8874", 28.00, "Production")

    employee_9 = (random.randint(1000, 9999), "David", "Wilson", "461 Baker Dr.", "Tacoma", "WA", "01844", "david.wilson@dimdom.com", "272-387-8388", 29.50, "R&D")

    employee_10 = (random.randint(1000, 9999), "Richard", "Lee", "9642 Parker Ave.", "Lynwood", "WA", "12601", "richard.lee@dimdom.com", "209-778-9947", 27.00, "Production")

    cursor.execute(sqlite_initialize_param, employee_1)
    cursor.execute(sqlite_initialize_param, employee_2)
    cursor.execute(sqlite_initialize_param, employee_3)
    cursor.execute(sqlite_initialize_param, employee_4)
    cursor.execute(sqlite_initialize_param, employee_5)
    cursor.execute(sqlite_initialize_param, employee_6)
    cursor.execute(sqlite_initialize_param, employee_7)
    cursor.execute(sqlite_initialize_param, employee_8)
    cursor.execute(sqlite_initialize_param, employee_9)
    cursor.execute(sqlite_initialize_param, employee_10)

    print("Database initialize/reset successfully!")

def add_an_employee(conn, cursor):
    # if input_hourly_rate is NOT NUMERIC, the code can throw an exception
    try:
        # employee_id_number is randomly generated between 1000 and 9999
        generated_employee_id_number = random.randint(1000, 9999)

        print("Please input the information below:\n")
        input_employee_first_name = input("First name: ").title()
        input_employee_last_name = input("Last name: ").title()
        input_street_address = input("Street address: ").title()
        input_city = input("City: ").title()
        input_state = input("State: ").upper()
        input_zipcode = input("Zipcode: ")
        input_phone_number = input("Phone number: ")
        # if input_hourly_rate is NOT NUMERIC, the code can throw an exception
        input_hourly_rate = float(input("Hourly rate: "))
        input_department_name = input("Department name: ")

        # the email address is automatically created using a format based on the inputted first name and last name
        input_email_address = f"{input_employee_first_name.lower()}.{input_employee_last_name.lower()}@dimdom.com"

        # build an INSERT statement with ? for values
        sqlite_add_param = """
            INSERT INTO Employees (employee_id_number, first_name, last_name, street_address, city, state, zipcode, email_address, phone_number, hourly_rate, department_name)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)
            """

        # store the added data of the new employee in a tuple
        added_data = (generated_employee_id_number, input_employee_first_name, input_employee_last_name, input_street_address, input_city, input_state, input_zipcode, input_email_address, input_phone_number, input_hourly_rate, input_department_name)

        cursor.execute(sqlite_add_param, added_data)

        print(f"\nThe employee, {input_employee_first_name} {input_employee_last_name}, has been added. Thank you!")
    except:
        print("\nSomething went wrong. Please try again!")

def list_all_employee_id_numbers_employee_names_email_addresses_and_department_names(conn, cursor):
    print("Here is the list of all employees with their\nemployee ID numbers, names, email and department names\n")
    # query the table
    cursor.execute("SELECT employee_id_number, first_name, last_name, email_address, department_name FROM Employees")

    # store the results of the query to a list called employeess
    employees = cursor.fetchall()

    # loop through the results of the query
    for this_employee in employees:
        print(this_employee[0], this_employee[1], this_employee[2], this_employee[3], this_employee[4])
    print()

def list_all_employee_names_full_addresses_and_phone_numbers(conn, cursor):
    print("Here is the list of all employees with their\nnames, full addresses, and phone numbers\n")
    # query the table
    cursor.execute("SELECT first_name, last_name, street_address, city, state, zipcode, phone_number FROM Employees")

    # store the results of a the query to a list called employees
    employees = cursor.fetchall()

    # loop through the results of the query
    for this_employee in employees:
        print(f"{this_employee[0]} {this_employee[1]}. {this_employee[2]}, {this_employee[3]}, {this_employee[4]} {this_employee[5]}. {this_employee[6]}")
    print()

def search_employees_by_last_name(conn, cursor):
    try:
        searching_input = input("Please enter the last name\nof the employees you would like to search: ").title()
        print()

        # build SELECT statement with ? for values
        sqlite_search_param = """
        SELECT last_name, first_name, email_address, department_name
        FROM Employees
        WHERE last_name = ?
        """
        cursor.execute(sqlite_search_param, (searching_input,))

        # store the results of a the query to a list called employees
        employees = cursor.fetchall()

        if employees[0][0] == "":
            raise Exception("Sorry, record not found. Please try again!")
        else:
            print(f"Bravo! Here is the record of\nall employees who have the last name {searching_input}:\n")
            # loop through the results of the query
            for this_employee in employees:
                print(this_employee[0], this_employee[1], this_employee[2], this_employee[3])
        print()
    except:
        print("Sorry, record not found. Please try again!")

def update_hourly_rate(conn, cursor):
    try:
        # if id_to_edit is NOT INTEGER, the code can throw an exception
        id_to_edit = int(input("Please enter the employee ID number\nof the employee you would like to update: "))
        # if input_hourly_rate is NOT NUMERIC, the code can throw an exception
        input_hourly_rate = float(input("\nNew hourly rate: "))

        # build an UPDATE statement with ? for values
        sqlite_update_param = """
            UPDATE Employees
            SET hourly_rate = ?
            WHERE employee_id_number = ? """
        cursor.execute(sqlite_update_param, (input_hourly_rate, id_to_edit))
        print("\nThe hourly rate has been updated successfully.")
    except:
        print("\nSomething went wrong. Please try again!")

def update_contact_information(conn, cursor):
    # if id_to_edit is NOT INTEGER, the code can throw an exception
    try:
        id_to_edit = int(input("Please enter the employee ID number\nof the employee you would like to update: "))
        print()
        input_street_address = input("New street address: ").title()
        input_city = input("New city: ").title()
        input_state = input("New state: ").upper()
        input_zipcode = input("New zipcode: ")
        input_phone_number = input("New phone number: ")

        # build an UPDATE statement with ? for values
        sqlite_update_param = """
            UPDATE Employees
            SET street_address = ?
              ,city = ?
              ,state = ?
              ,zipcode = ?
              ,phone_number = ?
            WHERE employee_id_number = ? """
        # store the data needed for UPDATE in a tuple
        update_data = (input_street_address, input_city, input_state, input_zipcode, input_phone_number, id_to_edit) 
        cursor.execute(sqlite_update_param, update_data)
        
        print("\nThe contact information has been updated successfully.")
    except:
        print("\nSomething went wrong. Please try again!")

def delete_a_given_employee(conn, cursor):
    try:
        # if id_to_delete is NOT INTEGER, the code can throw an exception
        id_to_delete = int(input("Please enter the employee ID number\nof the employee you would like to delete: "))

        # build DELETE statement with ? for values
        sqlite_delete_param = """
            DELETE FROM Employees
            WHERE employee_id_number = ? """
        cursor.execute(sqlite_delete_param, (id_to_delete,))
        
        print(f"\nThe data of the given employee\nwho has employee ID number {id_to_delete} has been deleted.")
    except:
        print("\nSomething went wrong. Please try again!")

def list_all_employee_id_numbers_and_hourly_rates(conn, cursor):
    print("Here is the list of all employees with their\nemployee ID numbers, names, and hourly rates\n")
    # query the table including the employee_id_number primary key value
    cursor.execute("SELECT employee_id_number, first_name, last_name, hourly_rate FROM Employees")

    # store the results of a the query to a list called employeess
    employees = cursor.fetchall()

    # loop through the results of the query
    for this_employee in employees:
        print(this_employee[0], this_employee[1], this_employee[2], this_employee[3])
    print()

def list_all_employee_id_numbers_and_contact_information(conn, cursor):
    print("Here is the list of all employees with their\nnames and contact information\n")
    # query the table including the employee_id_number primary key value
    cursor.execute("SELECT employee_id_number, first_name, last_name, street_address, city, state, zipcode, phone_number FROM Employees")

    # store the results of a the query to a list called employees
    employees = cursor.fetchall()

    # loop through the results of the query
    for this_employee in employees:
        print(f"{this_employee[0]} {this_employee[1]} {this_employee[2]}. {this_employee[3]}, {this_employee[4]}, {this_employee[5]} {this_employee[6]}. {this_employee[7]}")
    print()

def display_menu():
    print()
    print("* * * * * * * MENU SYSTEM * * * * * * *")
    print("0 - Initialize/reset database. (Careful this will wipe all data of newly added employees)")
    print("1 - Add an employee to the database")
    print("2 - List all employees with their employee ID numbers, names, email and department names")
    print("3 - List all employees with their names, full addresses, and phone numbers")
    print("4 - Search for employees by last name")
    print("5 - Update the hourly rate for a given employee")
    print("6 - Update the contact information for a given employee")
    print("7 - Delete data of a given employee")
    print("8 - Exit the program")

def main():
    print("Welcome to the Employee Database System of DimDom Inc.")
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
            initialize_or_reset_database(conn, cursor)
            conn.commit()
        elif command == "1":
            add_an_employee(conn, cursor)
            conn.commit()
        elif command == "2":
            list_all_employee_id_numbers_employee_names_email_addresses_and_department_names(conn, cursor)
        elif command == "3":
            list_all_employee_names_full_addresses_and_phone_numbers(conn, cursor)
        elif command == "4":
            search_employees_by_last_name(conn, cursor)
        elif command == "5":
            list_all_employee_id_numbers_and_hourly_rates(conn, cursor)
            update_hourly_rate(conn, cursor)
            conn.commit()
        elif command == "6":
            list_all_employee_id_numbers_and_contact_information(conn, cursor)
            update_contact_information(conn, cursor)
            conn.commit()
        elif command == "7":
            list_all_employee_id_numbers_employee_names_email_addresses_and_department_names(conn, cursor)
            delete_a_given_employee(conn, cursor)
            conn.commit()
        elif command == "8":
            break
        else:
            print("Unknown command. Please try again.")
    # close the connection to the database file
    conn.close()
    # farewell message
    print("Thank you for using the Employee Database System of DimDom Inc.\n\nHave a good rest of your day!")

if __name__ == "__main__":
    main()