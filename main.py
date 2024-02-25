import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

# How many symbols of each type will be in the slot machine
symbols_count = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 10
}

# How much each symbol is worth
symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    """
    Check how much the player won and on which lines
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        # Get the first symbol of the line (transversal line)
        symbol = columns[0][line]
        for column in columns:
            # Check if the symbol is the same in the whole line
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        # Will execute if the for loop does not break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a slot machine spin. 
    """
    all_symbols = []
    # Create a list with all the symbols
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Create the columns of the slot machine spin by randomly choosing a symbol from the list
    columns = []
    for _ in range(cols):
        column = []
        # Copy original list
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    # Return the columns, this is a matrix of the slot machine spin but in transposed form (rows are columns and columns are rows)
    return columns


def print_slot_machine(columns):
    """
    Print the slot machine spin in a human readable format (transposed matrix)
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(column[row], end=" | ") if i != len(
                columns) - 1 else print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit ? $")
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
        lines = input(
            f"Enter the number of lines to bet on (1-{str(MAX_LINES)}) ? : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a valid number of lines (1-{MAX_LINES})")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line ? : ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET}$ - {MAX_BET}$.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is : {balance}$")
        else:
            break

    print(
        f"You are betting {bet}$ on {lines} lines. Total bet is equal is equal to {total_bet}$")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f"You won : {winnings} $")
    print(f"You won on lines :", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is : {balance} $")
        answer = input("Presse enter to play. (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with : {balance}$")


main()
