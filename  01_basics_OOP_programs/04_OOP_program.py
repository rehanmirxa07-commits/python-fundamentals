class BankCard:
    def __init__(self, card_holder):
        self.card_holder = card_holder
        self.statement = []
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        self.statement.append(f"Deposited: ₹{amount}")
        print(f"Deposited: ₹{amount} to the bank account")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount  # Correctly update instance balance
            self.statement.append(f"Withdrew: ₹{amount}")  # Save to history
            print(f"Withdrew: ₹{amount} from the bank account")
            print(f"Available balance: ₹{self.balance}")
        else:
            print("Insufficient funds!")

    def show_statement(self):
        print(f"Card Holder: {self.card_holder}")
        print(f"Current Balance: ₹{self.balance}")
        print("Statement:")
        for transaction in self.statement:
            print(f"- {transaction}")


# --- TEST EXECUTION ---
my_card = BankCard("Rehan")

my_card.deposit(int(input("Enter the amount to deposit: ")))
my_card.withdraw(int(input("Enter the amount to withdraw: ")))
my_card.withdraw(int(input("Enter the amount to withdraw: ")))
my_card.show_statement()


            



        




            


       




    
        
        
        