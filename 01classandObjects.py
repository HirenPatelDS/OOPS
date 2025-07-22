class ATM:
    """
    A simple ATM simulation class allowing users to:
    - Generate a new PIN
    - Change their PIN
    - Check balance
    - Withdraw money
    """

    def __init__(self):
        """
        Initializes an ATM account with no PIN and zero balance.
        Launches the main menu loop.
        """
        self.pin = ''
        self.balance = 0
        self.runMenu()

    def runMenu(self):
        """
        Repeatedly shows the ATM menu until the user chooses to exit.
        """
        while True:
            print("\nWelcome! How can I assist you?")
            print("1. Create PIN")
            print("2. Change PIN")
            print("3. Check Balance")
            print("4. Withdraw")
            print("5. Exit")

            choice = input("Enter your choice (1–5): ").strip()

            if choice == "1":
                self.createPin()
            elif choice == "2":
                self.changePin()
            elif choice == "3":
                self.showBalance()
            elif choice == "4":
                self.withdrawCash()
            elif choice == "5":
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please enter a number from 1 to 5.")

    def createPin(self):
        """
        Sets a new 4-digit PIN and allows initial deposit.
        """
        newPin = input("Set your 4-digit ATM PIN: ").strip()

        if len(newPin) == 4 and newPin.isdigit():
            self.pin = newPin
            print("PIN successfully created.")

            try:
                depositAmount = float(input("Enter amount to deposit: "))
                if depositAmount < 0:
                    print("Invalid amount. Deposit must be positive.")
                else:
                    self.balance = depositAmount
                    print(f"₹{self.balance:.2f} deposited successfully.")
            except ValueError:
                print("Invalid input. Deposit failed.")
        else:
            print("PIN must be exactly 4 digits.")

    def changePin(self):
        """
        Allows the user to change their existing PIN after verifying the old one.
        """
        attemptsLeft = 3
        while attemptsLeft > 0:
            currentPin = input("Enter your current PIN: ").strip()

            if currentPin == self.pin:
                newPin = input("Enter new 4-digit PIN: ").strip()
                if len(newPin) == 4 and newPin.isdigit():
                    self.pin = newPin
                    print("PIN updated successfully.")
                    return
                else:
                    print("New PIN must be exactly 4 digits.")
                    return
            else:
                attemptsLeft -= 1
                print(f"Incorrect PIN. Attempts left: {attemptsLeft}")

        print("Too many failed attempts. Session terminated.")

    def showBalance(self):
        """
        Displays the current balance.
        """
        print(f"Your current balance is: ₹{self.balance:.2f}")

    def withdrawCash(self):
        """
        Allows the user to withdraw money after checking for sufficient balance.
        """
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > self.balance:
                print("Insufficient balance.")
                print(f"Available balance: ₹{self.balance:.2f}")
            else:
                self.balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully.")
                print(f"Remaining balance: ₹{self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

# Create an ATM user session
atmUser = ATM()
