board = [' ' for _ in range(9)]


# Функція друку ігрового поля
def print_board():
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")


# Функція перевірки виграшу
def check_win(mark):
    # Перевірка рядків
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == mark:
            return True
    # Перевірка стовпців
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == mark:
            return True
    # Перевірка діагоналей
    if board[0] == board[4] == board[8] == mark:
        return True
    if board[2] == board[4] == board[6] == mark:
        return True
    return False


# Старт гри
def play_game():
    print("Ласкаво просимо до гри Хрестики-ноліки!")
    print_board()
    while True:

        # Хід гравця 1
        choice = int(input("Гравець 1, виберіть квадрат (1-9): ")) - 1
        if board[choice] == ' ':
            board[choice] = 'X'
        else:
            print("Вибачте, цей квадрат уже зайнятий.")
            continue
        print_board()
        if check_win('X'):
            print("Вітаю! Гравець 1 виграє!")
            break
        if ' ' not in board:
            print("Це нічия!")
            break

        # Хід гравця 2
        choice = int(input("Гравець 2, виберіть квадрат (1-9): ")) - 1
        if board[choice] == ' ':
            board[choice] = 'O'
        else:
            print("Вибачте, цей квадрат уже зайнятий.")
            continue
        print_board()
        if check_win('O'):
            print("Вітаю! Гравець 2 виграє!")
            break


play_game()
