# --- Configuration and Data Storage ---
# Global list to store all item records
item_history = []

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def login():
    """Admin login function with retry loop."""
    print("=== Admin Login ===")
    while True:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print("\nLogin successful! Welcome, Admin.\n")
            return True
        else:
            print("\nInvalid username or password. Please try again.\n")

def stranger_finds_item():
    """Registers a new item with 'Pending' status."""
    print("\n--- Stranger reports a lost item ---")
    print("(Type 'exit' at any time to cancel)")

    item_name = input("Enter the name of the lost item: ").strip()
    if item_name.lower() == 'exit': return

    item_desc = input("Enter a description of the item: ").strip()
    if item_desc.lower() == 'exit': return
    
    new_item = {
        'name': item_name,
        'desc': item_desc,
        'status': 'Pending'
    }
    item_history.append(new_item)
    print(f"Admin has registered '{item_name}' as Pending.\n")

def owner_claims_item():
    """Attempts to claim a 'Pending' item by verifying description."""
    print("\n--- Owner claims an item ---")
    print("(Type 'exit' at any time to cancel)")

    target_name = input("Enter the name of the item you lost: ").strip()
    if target_name.lower() == 'exit': return

    # Find the item
    found_item = None
    for item in item_history:
        # Only match if it's the right name AND it is still pending
        if item['name'].lower() == target_name.lower() and item['status'] == 'Pending':
            found_item = item
            break
    
    if found_item:
        print(f"Item '{target_name}' found. Please verify ownership.")
        claimed_desc = input("Enter the description of the item: ").strip()
        if claimed_desc.lower() == 'exit': return

        # --- NEW VERIFICATION STEP ---
        confirm = input("Is this description accurate? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Claim cancelled. returning to menu.")
            return
        # -----------------------------

        if claimed_desc.lower() == found_item['desc'].lower():
            print(f"Verification successful! You have claimed '{found_item['name']}'.")
            found_item['status'] = 'Claimed'
        else:
            print("Description does not match. Claim failed.")
    else:
        print("No pending lost item found with that name.")

def show_current_items():
    """Shows only items that are currently lost (Pending)."""
    print("\n--- Currently Lost Items (Pending) ---")
    pending_found = False
    for item in item_history:
        if item['status'] == 'Pending':
             print(f"- Name: {item['name']} | Description: {item['desc']}")
             pending_found = True
             
    if not pending_found:
        print("No items are currently listed as lost.")

def view_history():
    """Shows ALL items ever registered and their status."""
    print("\n--- Full Item History ---")
    if not item_history:
        print("History is empty.")
    else:
        for index, item in enumerate(item_history, 1):
            print(f"{index}. Name: {item['name']} | Status: [{item['status']}]")
            print(f"   Description: {item['desc']}")

def show_menu():
    """Displays the main menu options."""
    print("\n===========================")
    print("   Lost and Found Menu")
    print("===========================")
    print("1. Report a lost item (Stranger)")
    print("2. Claim an item (Owner)")
    print("3. Show current lost items")
    print("4. View full history & status")
    print("5. Exit")

def main():
    """Main program loop."""
    login()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            stranger_finds_item()
        elif choice == '2':
            owner_claims_item()
        elif choice == '3':
            show_current_items()
        elif choice == '4':
            view_history()
        elif choice == '5':
            print("Exiting Lost and Found system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()