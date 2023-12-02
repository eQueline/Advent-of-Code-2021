import utils
from functools import reduce

input_str = utils.get_input("1")


def solve(input_str, window):
    inc_count = 0
    prev = None
    input_list = [int(x) for x in input_str.split('\n')]
    for i in range(window, len(input_list)+1):
        cur = reduce(lambda a, b: a + b, input_list[i - window:i])
        if prev is not None:
            inc_count += cur > prev
        prev = cur
    return inc_count


def solve_p1(input_str):
    return solve(input_str, 1)


def solve_p2(input_str):
    return solve(input_str, 3)


part1 = utils.time_function(solve_p1, input_str)
print("Part 1:", part1)
part2 = utils.time_function(solve_p2, input_str)
print("Part 2:", part2)
