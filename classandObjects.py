class ATM:
    """
    A simple ATM class that holds a user's PIN and account balance.
    """

    def __init__(self, userPin: str, initialBalance: float):
        """
        Initializes the ATM with a user's PIN and starting balance.

        Args:
            userPin (str): The 4-digit PIN code.
            initialBalance (float): Starting account balance.
        """
        self.pin = userPin
        self.balance = initialBalance

    def __repr__(self):
        return f"<ATM(PIN={self.pin}, Balance={self.balance})>"


# Create an ATM object with PIN and balance
atmUser = ATM("1234", 1000.0)

# Print the type of the object
print(type(atmUser))  # <class '__main__.ATM'>

        