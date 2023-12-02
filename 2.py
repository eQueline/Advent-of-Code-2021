import re
import utils

input_str = utils.get_input("2")


def parse_input(input_str):
    course = []
    for line in input_str.split('\n'):
        match = re.match(r'(\w+) (\d+)', line).groups()
        course.append((match[0], int(match[1])))
    return course


def solve_p1(input_str):
    course = parse_input(input_str)
    position, depth = 0, 0
    for command in course:
        match command[0]:
            case 'forward':
                position += command[1]
            case 'up':
                depth -= command[1]
            case 'down':
                depth += command[1]
    return position * depth


def solve_p2(input_str):
    course = parse_input(input_str)
    position, aim, depth = 0, 0, 0
    for command in course:
        match command[0]:
            case 'forward':
                position += command[1]
                depth += aim * command[1]
            case 'up':
                aim -= command[1]
            case 'down':
                aim += command[1]
    return position * depth


part1 = utils.time_function(solve_p1, input_str)
print("Part 1:", part1)
part2 = utils.time_function(solve_p2, input_str)
print("Part 2:", part2)
