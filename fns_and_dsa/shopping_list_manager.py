def display_menu():
    """Display the shopping list menu options."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to manage the shopping list."""
    shopping_list = []

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Add item
            item = input("Enter the item to add: ").strip()
            if item:  # ensure not empty
                shopping_list.append(item)
                print(f"Added '{item}' to the shopping list.")
            else:
                print("Item name cannot be empty.")

        elif choice == 2:
            # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == 3:
            # View list
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()