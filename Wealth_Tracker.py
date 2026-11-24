class Transaction:
    next_id = 1
    def __init__(self, title, amount, transaction_type, category, date):
        self.id = Transaction.next_id
        Transaction.next_id += 1
        self.title = title
        self.amount = amount
        self.transaction_type = transaction_type
        self.category = category
        self.date = date

    def __str__(self):
        return f"{self.id}|{self.title}|{self.amount}|{self.transaction_type}|{self.category}|{self.date}"
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        if amount <= 0:
            raise ValueError("Invalid!")
        self._amount = amount
   
    @property
    def transaction_type(self):
        return self._transaction_type
    
    @transaction_type.setter
    def transaction_type(self,transaction_type):
        if transaction_type not in ["Expense", "Income"]:
            raise ValueError("Invalid input , Enter [Expense or Income]")
        self._transaction_type = transaction_type

transactions = []

def main():
    while  True:
      print("\n=== WealthTrack ===")
      print('''
           1. Add transaction
           2. View transaction
           3. Financial summary
           4. Update transaction
           5. Delete transaction
           6. Exit
''')  
      try:
         choice = int(input("Choose[1,2 etc..]: "))
      except ValueError:
          print("Enter integer!")
          choice = int(input("Choose[1,2 etc..]: "))
      if choice == 1:
        get = get_info()
        transactions.append(get)
        print(get)

      elif choice == 2:
          if not transactions:
              print("Not found")
          else:
              for item in transactions:
                  print(item)

      elif choice == 3:
          income, expenses , balance = calculate_balance()
          print(f"Income: {income}")
          print(f"Expense: -{expenses}")
          print(f"Balance: ${balance}")
           
      elif choice == 4:
          go = update_transaction()
          print(go)

      elif choice == 5:
          gos = delete_transaction()
          print(gos)

      elif choice == 6:
          print("Thanks!")
          break

def get_info():
      title  = input("Enter the title: ")
      try:
         amount = float(input("Enter amount: "))
      except ValueError:
          print("Enter number")
          amount = float(input("Enter amount: "))
      transaction_type = input("Enter transaction type: ")
      category = input("Enter category: ")
      date = input("Enter date[year-month-day]: ")
      return Transaction(title,amount,transaction_type,category,date)

def calculate_balance():
    total_income = 0
    total_expenses = 0
    for item in transactions:
        if item.transaction_type == "Income":
            total_income += item.amount
        elif item.transaction_type == "Expense":
            total_expenses += item.amount
        else:
            print("Something went wrong pls enter again!")

    balance = total_income - total_expenses
    return total_income,total_expenses,balance

def update_transaction():
    id = int(input("Enter your id: "))
    for item in transactions:
        if id == item.id:
            chg = input("Which info do you want to change?: ")
            if chg in ["title", "amount", "transaction_type", "category", "date"]:
                chs = input("Enter the new value: ")
                if chg == "amount":
                    chs = float(chs)

                setattr(item, chg, chs)
                return "Transaction updated successfully!"
            else:
               return "Invalid attribute!"
    else:
        return "Transaction not found!"
                
def delete_transaction():
    id = int(input("Enter your id: "))
    for item in transactions:
        if id == item.id:
            transactions.remove(item)
            return "Transaction deleted successfully!" 
    else:
        return "Transaction not found!"
    
if __name__ == "__main__":
    main()
