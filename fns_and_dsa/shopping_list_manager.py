def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to the list.\n")

        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.\n")
            else:
                print("Item not found.\n")

        elif choice == '3':
            if len(shopping_list) == 0:
                print("Shopping list is empty.\n")
            else:
                print("Current Shopping List:")
                for i, it in enumerate(shopping_list, 1):
                    print(f"{i}. {it}")
                print()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
