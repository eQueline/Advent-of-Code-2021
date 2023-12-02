import utils

input_str = utils.get_input("3")


def parse_input(input_str):
    binary_list = []
    for line in input_str.split('\n'):
        binary_list.append([int(x) for x in line])
    return binary_list


def most_common_bit(binary_list, position):
    bitmap = 0
    for binary in binary_list:
        bitmap += binary[position] * 2 - 1
    return 1 if bitmap >= 0 else 0


def solve_p1(input_str):
    binary_list = parse_input(input_str)
    gamma, epsilon = '', ''
    for i in range(len(binary_list[0])):
        mcb = most_common_bit(binary_list, i)
        gamma += str(mcb)
        epsilon += str(1 - mcb)

    return int(gamma, 2) * int(epsilon, 2)


def get_rating(binary_list, mode):
    filtered_list = []
    for binary in binary_list:
        filtered_list.append(binary.copy())
    for i in range(len(filtered_list[0])):
        mcb = most_common_bit(filtered_list, i)
        filter_bit = mcb if mode else 1 - mcb
        filtered_list = [binary for binary in filtered_list if binary[i] == filter_bit]
        if len(filtered_list) == 1:
            rating_str = ''.join(str(x) for x in filtered_list[0])
            return int(rating_str, 2)


def solve_p2(input_str):
    binary_list = parse_input(input_str)
    return get_rating(binary_list, True) * get_rating(binary_list, False)


part1 = utils.time_function(solve_p1, input_str)
print("Part 1:", part1)
part2 = utils.time_function(solve_p2, input_str)
print("Part 2:", part2)
