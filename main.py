import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 2

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 5,
    "C": 7,
    "D": 11
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


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


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(colums):
    for row in range(len(colums[0])):
        for i, column in enumerate(colums):
            if i != len(colums) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

        


def deposit():
    while True:
        amount = input("Quantos Reais voce gostaria de depositar? R$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("A quantidade deve ser maior que R$ 0,00 ")
        else:
            print("Por favor entre com um valor valido. Apenas numeros!")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Quantas linhas voce gostaria de apostar? (1-" + str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Entre com uma quantidade de linhas Valida.")
        else:
            print("Por favor entre com um valor valido. Apenas numeros!")

    return lines





def get_bet():
    while True:
        amount = input("Quanto voce gostaria de apostar em cada linha? R$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"A quantidade deve estar entre R$ {MIN_BET} - R$ {MAX_BET}. ")
        else:
            print("Por favor entre com um valor valido. Apenas numeros!")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Voce não tem saldo suficiente para apostar essa quantidade, seu saldo é de R$: {balance}")
        else:
            break

    print(f"Voce esta apostando R${bet} em {lines} linhas. Total da aposta é de: R$ {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Voce ganhou R${winnings}")
    print(f"Voce ganhou na linha ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    
    while True:
        print(f"Seu saldo é de R${balance} ")
        game = input("Aperte ENTER para jogar (S para Sair).")
        if game == "s":
            break
        balance += spin(balance)

    print(f"Voce saiu com um saldo de R$ {balance}")


print("================  BEM VINDO(A) À MAQUINA DE CAÇA-NIQUEIS  ================")
main()


