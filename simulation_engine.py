
import random
import sqlite3
from datetime import datetime

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

Rows = 3
Cols = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}  # fixed typo "2":5 → "D":2

# -----------------------
# Database Setup
# -----------------------
def init_db():
    conn = sqlite3.connect("simulation_results.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_id INTEGER,
        bet INTEGER,
        lines INTEGER,
        total_bet INTEGER,
        winnings INTEGER,
        outcome INTEGER,
        timestamp TEXT
    )
    """)
    conn.commit()
    conn.close()

def log_result(run_id, bet, lines, total_bet, winnings, outcome):
    conn = sqlite3.connect("simulation_results.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO results (run_id, bet, lines, total_bet, winnings, outcome, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (run_id, bet, lines, total_bet, winnings, outcome,
          datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# -----------------------
# Game Functions
# -----------------------
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def spin(balance, run_id):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount. Current balance: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet = ${total_bet}")

    slots = get_slot_machine_spin(Rows, Cols, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines if winning_lines else "None")

    outcome = winnings - total_bet  # net gain/loss

    # ---- Save to database ----
    log_result(run_id, bet, lines, total_bet, winnings, outcome)

    return outcome


# -----------------------
# Main Loop
# -----------------------
def main():
    init_db()
    balance = deposit()
    run_id = 1

    while True:
        print(f"\nCurrent balance: ${balance}")
        answer = input("Press enter to play (q to quit): ")
        if answer.lower() == "q":
            break
        balance += spin(balance, run_id)
        run_id += 1

    print(f"\nYou left with ${balance}")

if __name__ == "__main__":
    main()



# import random
# MAX_LINES = 3
# MAX_BET = 100
# MIN_BET = 1


# Rows = 3
# Cols = 3

# symbol_count = {"A" : 2,"B" : 4,"C" : 6,"D" : 8, }
# symbol_value = {"A": 5, "B": 4, "C": 3, "2": 5}


    
# def deposit():
#     while True:
#         amount = input("what would you like to deposite? $")
#         if amount.isdigit():
#             amount = int(amount)
#             if amount > 0:
#                 break
#             else:
#                 print("Amount must be greater than 0.") 
#         else:
#             print("Please enter a number.")   

#     return amount             

# def get_number_of_lines():
#     while True:
#         lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
#         if lines.isdigit():
#             lines = int(lines)
#             if 1 <= lines <= MAX_LINES:
#                 break
#             else:
#                 print("Enter a valid number of lines.")
#         else:
#             print("Please enter a number.") 

#     return lines


# def get_bet():
#     while True:
#         amount = input("what would you like to bet on each line? $")
#         if amount.isdigit():
#             amount = int(amount)
#             if MIN_BET <= amount <= MAX_BET:
#                break
#             else:
#                 print(f"amount must be between ${MIN_BET}-${MAX_BET}.")
#         else:
#             print("please enter a number.")  

#     return amount             
         
# def get_slot_machine_spin(rows,cols, symbols):
#     all_symbols = []
#     for symbol , symbol_count in symbols.items():
#            for _ in range(symbol_count):
#                all_symbols.append(symbol)

#     columns = []
#     for _ in range(cols):
#         column = []
#         current_symbols = all_symbols[:]
#         for _ in range(rows):
#             value = random.choice(current_symbols)
#             current_symbols.remove(value)
#             column.append(value)

#         columns.append(column)   

#     return columns    


# def print_slot_machine(columns):
#     for row in range(len(columns[0])):
#         for i, column in enumerate(columns):
#             if i!= len(columns)-1 :
#                 print(column[row], end = " | ")
#             else:
#                 print(column[row], end = "")   

#         print() 

# def check_winnings(columns, lines, bet, values): 
#     winnings = 0
#     winning_lines = []
#     for line in range(lines):
#         symbol = columns[0][line]
#         for column in columns:
#             symbol_to_check = column[line] 
#             if symbol != symbol_to_check:
#                 break
#         else:
#                 winnings += values[symbol] * bet
#                 winning_lines.append(line +1)

#     return winnings, winning_lines           



# def spin(balance):
#     lines = get_number_of_lines()
#     while True:
#         bet = get_bet()
#         Total_bet = bet * lines

#         if(Total_bet > balance):
#             print(f"you do not have enough balance to bet that amount, your current balance is : ${balance}")
#         else:
#             break    

#     print(f"you are betting ${bet} on {lines} lines, Total bet is equal to : ${Total_bet}")

#     slots = get_slot_machine_spin(Rows, Cols, symbol_count)
#     print_slot_machine(slots)
#     winning, winning_lines =  check_winnings(slots, lines, bet, symbol_value)
#     print(f"you won ${winning}.")
#     print(f"you won on lines:", *winning_lines)
#     return winning - Total_bet




# def main():
#     balance = deposit()
#     while True:
#         print(f"current balance is ${balance}")
#         answer = input("Press enter to play (q to quit).")
#         if answer == "q":
#             break
#         balance += spin(balance)

#     print(f"you left with $ {balance}")

 

# main()