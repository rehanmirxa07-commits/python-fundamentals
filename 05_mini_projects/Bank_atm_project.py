# ======= BANK-ATM-LOGIC ======


class BankCard:
    
    def __init__(self, card_holder):
        self.card_holder = card_holder
        self.statement = []
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        self.statement.append(f"Deposited: ₹{amount}")
        print(f"Deposited: ₹{amount} to the bank account")
        print(f"Available balance: {self.balance}")
              

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

my_card = BankCard("Rehan")

print(f"Welcome to the Bank, {my_card.card_holder}!")

while True:
    print("\n--- WHAT WOULD YOU LIKE TO DO? ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Statement")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")

    if choice == "1":
        amount = int(input("enter your deposit: "))

        
        Pin = int(input("======= enter your pin:"))
        if Pin == 1803:
            my_card.deposit(amount)

        else:
            print("Wrong pin entered")

            
        print("Want to coninue ?: ")
        print("YES")
        print("NO")
        choice = input("select an option: ")
        if choice == "NO":
            break 
        

    elif choice == "2":
        amount = int(input("enter your withdrawl amount: "))
        Pin = int(input("======= enter your pin:"))
        if Pin == 1803:
            my_card.withdraw(amount)
        else:
            print("Wrong pin entered")
        print("Want to coninue ?: ")
        print("YES")
        print("NO")
        choice = input("select an option: ")
        if choice == "NO":
              break 
        
    elif choice == "3":
         Pin = int(input("======= enter your pin:"))
         if Pin == 1803:
             my_card.show_statement()
         else:
            print("Wrong pin entered")
            print("Want to coninue ?: ")
            print("YES")
            print("NO")
            choice = input("select an option: ")
            if choice == "NO":
                break 
                

    elif choice == "4":
        print("Thank you to use our bank!")
        break
    else:
        print("Invalid choice choose between: (1-4)")