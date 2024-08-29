def check_pin():
    correct_pin = "1234"  # The correct PIN
    max_attempts = 4  # Maximum number of attempts

    for attempt in range(1, max_attempts + 1):
        entered_pin = input(f"Attempt {attempt}/{max_attempts}: Please enter your PIN: ")
        if entered_pin == correct_pin:
            print("PIN accepted. Access granted.")
            return
        else:
            print("Incorrect PIN.")

    print("Too many incorrect attempts. Access blocked.")

# Run the function
check_pin()


