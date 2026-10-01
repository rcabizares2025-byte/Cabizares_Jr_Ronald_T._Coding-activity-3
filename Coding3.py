class BankAccount:
    def __init__(self, account_holder, initial_deposit=0.0):
        # Public attribute
        self.account_holder = account_holder

        # Non-public attribute for balance
        if initial_deposit >= 0:
            self._balance = initial_deposit
        else:
            raise ValueError("Initial deposit cannot be negative.")

        # Internal transaction log
        self._transactions = []

    @property
    def balance(self):
        """Getter for the current balance."""
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        """Setter that validates the new balance before assigning it."""
        if new_balance >= 0:
            self._balance = new_balance
        else:
            raise ValueError("Balance cannot be negative.")

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        self._balance += amount
        self._transactions.append(f"Deposited: +{amount:.2f} | New Balance: {self._balance:.2f}")
        return self._balance

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self._balance:
            raise ValueError("Insufficient balance for this withdrawal.")

        self._balance -= amount
        self._transactions.append(f"Withdrew: -{amount:.2f} | New Balance: {self._balance:.2f}")
        return amount

    def get_transaction_history(self):
        """Return a copy of the transaction log."""
        return self._transactions.copy()
    

if __name__ == "__main__":
    account = BankAccount("Bonifacio II Carandang", 1000.0)

    account.deposit(500)
    account.withdraw(200)

    print("Account Holder:", account.account_holder)
    print("Current Balance:", account.balance)
    print("Transaction History:")
    for entry in account.get_transaction_history():
        print(" -", entry)

    # Testing the property setter validation
    try:
        account.balance = -50
    except ValueError as e:
        print("Error caught:", e)
        