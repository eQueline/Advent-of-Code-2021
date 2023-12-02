import utils

input_str = utils.get_input("4")


def parse_input(input_str):
    input_entries = input_str.split('\n\n')
    order = [int(x) for x in input_entries[0].split(',')]

    boards = []
    for input_entry in input_entries[1:]:
        boards.append(
            [[int(x) for x in row.split(' ') if x != ''] for row in input_entry.split('\n')]
        )
    return order, boards


def mark_board(board, board_map, number):
    for y, row in enumerate(board):
        for x, entry in enumerate(row):
            if entry == number:
                board_map[y][x] = True


def check_board(board_map):
    for i in range(len(board_map)):
        if False not in board_map[i]:
            return True

    for i in range(len(board_map[0])):
        if False not in [row[i] for row in board_map]:
            return True

    return False


def calculate_board_winning_score(board, board_map):
    entry_sum = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if not board_map[y][x]:
                entry_sum += board[y][x]
    return entry_sum


def get_winning_board(order, boards, first_win=True):
    board_maps = []
    board_wins = dict()
    for board in boards:
        board_maps.append([[False] * len(row) for row in board])
    for number in order:
        for i in range(len(boards)):
            mark_board(boards[i], board_maps[i], number)

            if check_board(board_maps[i]):
                board_wins[i] = (calculate_board_winning_score(boards[i], board_maps[i]) * number)
                # return first win or last win depending on first_win param
                if first_win or len(board_wins) == len(boards):
                    return board_wins[i]


def solve_p1(input_str):
    order, boards = parse_input(input_str)
    board_win = get_winning_board(order, boards)
    return board_win


def solve_p2(input_str):
    order, boards = parse_input(input_str)
    board_win = get_winning_board(order, boards, first_win=False)
    return board_win


part1 = utils.time_function(solve_p1, input_str)
print("Part 1:", part1)
part2 = utils.time_function(solve_p2, input_str)
print("Part 2:", part2)
