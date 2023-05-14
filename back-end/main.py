import sqlite3


def show_menu():
    print("1_ show list")
    print("2_ add new")
    print("3_ edit")
    print("4_ remove")
    print("5_ exit")


def load_database():
    global connection, my_cursor
    connection = sqlite3.connect("database\shop.db")
    my_cursor = connection.cursor()


def show_list():
    table_name = input("Enter table's name: ")
    for data in my_cursor.execute(f"SELECT * FROM '{table_name}'"):
        print(data)
        print()


def add_new():
    table_name = input("Enter table's name: ")
    new_name = input("Enter new name: ")
    new_price = float(input("Enter new price: "))
    new_count = int(input("Enter count: "))
    my_cursor.execute(
        f"INSERT INTO {table_name}(Name) VALUES('name = {new_name}', price = '{new_price}', count = '{new_count}')")
    connection.commit()
    print("add successful")
    print()


def edit():
    name = input("Enter product's name: ")
    new_price = float(input("Enter price: "))
    new_count = int(input("Enter count: "))
    my_cursor.execute(
        f"UPDATE product SET price = '{new_price}', count = '{new_count}' WHERE name = '{name}'")
    connection.commit()


def remove():
    name = input("Enter name: ")
    my_cursor.execute(f"DELETE FROM products WHERE Name = '{name}'")
    connection.commit()


if __name__ == "__main__":
    load_database()

    while True:
        show_menu()
        choice = int(input())

        if choice == 1:
            show_list()

        elif choice == 2:
            add_new()

        elif choice == 3:
            edit()

        elif choice == 4:
            remove()

        elif choice == 5:
            exit(0)
