import datetime
import csv

#objective 4 save expenses to a csv file
def save_expenses_csv(expenses, filename):
    #create a list of headers for csv file
    header = ['date', 'category', 'amount', 'description']
    #mode='w' is write mode
    #encoding='utf-8' is character encoding standard
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        #csv.DictWriter is a predefined class in Python's csv module and data is in a dictionary. Could use csv.writer if only in lists
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(expenses)
    print('Expenses saved to', filename)

#loading expenses at start of program
#parameter = filename
def load_expenses_csv(filename):
    #put expenses in a list
    expenses = []
    try:
        #use 'with' statement instead of file.close() after code runs
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                #convert amount back to a float b/c automatically stored as a string in csv file b/c it's a text file
                row['amount'] = float(row['amount'])
                expenses.append(row)
    except FileNotFoundError:
        print(f"{filename} not found. Starting with a blank expense list.")
    return expenses

#defining menu choices
def display_menu():
    print("\nMenu:")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Track budget")
    print("4. Save expenses")
    print("5. Exit")

#defining part of menu
def add_expense(expenses):
    date_inp = input('Please enter the expense date (YYYY-MM-DD): ')
    try:
        date_obj = datetime.datetime.strptime(date_inp, '%Y-%m-%d')
    except ValueError:
        print('Incorrect date format. Please enter YYYY-MM-DD.')
        return

    category_inp = input('Please enter the category of expense: ')
    if not category_inp:
        print("You must enter a category.")
        return

    cost_inp = input('Please enter how much you spent: ')
    try:
        cost_inp_float = float(cost_inp)
    except ValueError:
        print('Invalid amount. Please enter only numbers.')
        return

    description_inp = input('Please provide a brief description of the spend: ')
    if not description_inp:
        print("Description can't be left blank.")
        return

    expense_record = {
        'date': date_obj.strftime('%Y-%m-%d'),
        'category': category_inp,
        'amount': cost_inp_float,
        'description': description_inp
    }
    expenses.append(expense_record)
    print("Expense added!")

#defining part of menu
def view_expenses(expenses):
    print("These are your expenses:")
    #enumerate loops through the task_tracker starting at 1. instead of 0
    for i, expense in enumerate(expenses, start=1):
        #expense dictionary within a list using'keys'
        #f"{i}. for numbering 1, 2, 3 in the list. the period provides 1., 2., 3. 
        print(f"{i}. {expense['date']} - {expense['category']}: ${expense['amount']} - {expense['description']}")

#defining part of menu
def track_budget(expenses, budget):
    #sum expenses. create variable total_expense
    #'amount' key in each expense dictionary list
    total_expense = sum(expense['amount'] for expense in expenses)
     #formatting to for dollars and cents .2f ensures two decimal points
    print(f"Total expenses: ${total_expense:.2f}")
    if total_expense > budget:
        print("You are over this month's budget!")
    else:
        extra = budget - total_expense
        print(f"You are within budget this month! You have ${extra:.2f} remaining")

#defining part of menu
def save_expense():
    print('Your expense has been saved.')

#defining part of menu
def exit_program():
    print('You have exited the expense tracker.')

#defining main menu
def main_menu():
    #argument = expenses.csv passed to parameter filename
    expenses = load_expenses_csv('expenses.csv')
    #create variable budget and convert inputted string to float for calculation purposes
    budget = float(input("Enter your budget: "))

    while True:
        display_menu()
        select = input("Please enter your menu selection: ")
        #add expense
        if select == '1':
            add_expense(expenses)
        #show all expenses
        elif select == '2':
            view_expenses(expenses)
        #provide expenses and budget
        elif select == '3':
            track_budget(expenses, budget)
        #save
        elif select == '4':
            #call function: expenses and expenses.csv are the arguments. save_expense() calls argument expenses and uses expenses.csv to specify the filename
            save_expenses_csv(expenses, 'expenses.csv')
            save_expense()
        #save and exit
        elif select == '5':
            save_expenses_csv(expenses, 'expenses.csv')
            exit_program()
            break
        #feedback if error
        else:
            print("Invalid selection. Please enter 1-5 only.")

#__name__ is a built-in varialbe in Python assigned to the module name. __name__ is set to __main__ when run directly vs an imported script
if __name__ == "__main__":
    main_menu()