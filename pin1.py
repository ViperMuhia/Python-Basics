def check_pin():
    correct_pin = "1234"  # The correct PIN
    max_attempts = 4  # Maximum number of attempts
    attempts = 0  # Counter for attempts
    while attempts < max_attempts:
        entered_pin = input(f"Attempt {attempts + 1}/{max_attempts}: Please enter your PIN: ")
        if entered_pin == correct_pin:
            print("PIN accepted. Access granted.")
            break
        else:
            print("Incorrect PIN.")
            attempts += 1
    else:
        print("Too many incorrect attempts. Access blocked.")
check_pin()

