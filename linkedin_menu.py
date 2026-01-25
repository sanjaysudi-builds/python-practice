
# LINKEDIN MENU PROGRAM

def menu():
    print("\n--- LinkedIn Menu ---")
    print("1. View Profile")
    print("2. Create Post")
    print("3. Send Connection Request")
    print("4. Logout")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Viewing LinkedIn profile...")

    elif choice == "2":
        post = input("Write your post: ")
        print("Post published!")

    elif choice == "3":
        name = input("Enter name to connect: ")
        print(f"Connection request sent to {name}")

    elif choice == "4":
        print("Logged out successfully.")
        break

    else:
        print("Invalid choice. Try again.")