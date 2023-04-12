while True:
    print("Please choose an option:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    choice = input("Enter your choice (1-4): ")

    if choice.isdigit():
        choice = int(choice)
        if choice >= 1 and choice <= 4:
            break
    print("Invalid choice. Please enter a number between 1 and 4.")


if choice == 1:
    print("Option 1 selected.")
elif choice == 2:
    print("Option 2 selected.")
elif choice == 3:
    print("Option 3 selected.")
elif choice == 4:
    print("Option 4 selected.")
