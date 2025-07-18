import csv
import os
file_path = "budget_data.csv"
if not os.path.exists(file_path):
    with open(file_path, mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["type", "amount", "balance"])

def show_menu():
    print("\n=== Budget Tracker ===")
    print("1.add Income")
    print("2.show balance")
    print("3.add expense")
    print("4. Show Transaction history")
    print("5.exit")

class Budgettracker:
   def __init__(self):
      self.transaction = []
      self.balance = 0

   def addincome(self,amount):
      try:
          amount = float(amount)
          self.balance += amount
          self.transaction.append(f"Income : {amount}")
          with open(file_path, mode = 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(["Income", amount, self.balance])
          print("Income added successfully !")
      except ValueError:
         print("enter a valid number")

   def showbalance(self):
      print(f"Your current balace is : Rs. {self.balance}")

   def addexpenses(self,amount):
       try:
          amount = float(amount)
          if amount <= self.balance:
           self.balance -= amount
           self.transaction.append(f"Expense : {amount}")
           with open(file_path, mode = 'a', newline = '') as file:
             writer = csv.writer(file)
             writer.writerow(["expenses", amount, self.balance])
           print("Expense entry done successfully .")
          else:
           print("Insufficient balance")
       
       except ValueError:
          print("Enter a valid number")

   def showhistory(self):
       try:
         with open(file_path, 'r') as file:
          reader = csv.reader(file)
          print("\n Transaction history")
          for row in reader:
             print(",".join(row))

       except Exception as e:
          print("File was not able to open", e)

   def exit(self):
       print("Exiting the app")
       return True   

def main():
    tracker = Budgettracker()
    while True:
     show_menu()
     choice = input("choose an option (1-5):")
     if choice == '1':
        amount = input("Enter the income")
        tracker.addincome(amount)

     elif choice == '2':
        tracker.showbalance()
     elif choice == '3':
        amount = input("Enter the expense")
        tracker.addexpenses(amount)
     elif choice == '4':
      tracker.showhistory()
     elif choice == '5':
        if tracker.exit():
          break
if __name__ == "__main__":
   main()