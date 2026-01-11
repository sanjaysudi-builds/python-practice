pin = "1234"
trials = 1

while trials<=3:
    input_pin = input(f"Trail-{trials} | PIN >> ")
    trials += 1
    if input_pin == pin:
        print("PIN accepted. You can proceed.")
        break
    else:
            print("Incorrect PIN. Try again.")
        