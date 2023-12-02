#!/usr/bin/env python3


from collections.abc import Iterable
import re


def read_lines(input_file_name: str, strip=True) -> Iterable[str]:
    """
    Open a file and return its contents as an iterable of strings.
    :param input_file_name: the file name
    :param strip: strip each line
    :return: Iterable[str]
    """
    with open(input_file_name, 'r') as f:
        if strip:
            return list(map(lambda s: s.strip(), f.readlines()))

        return f.readlines()


def get_max_values(line: str) -> dict:
    max_blue, max_red, max_green = 0, 0, 0
    split1 = line.split(': ')
    split2 = split1[1].split(';')
    for grab in split2:
        for match in re.findall(r'\d+\s\w+', grab):
            split3 = match.split()
            count = int(split3[0])
            color = split3[1]
            match color:
                case 'blue':
                    max_blue = max(max_blue, count)
                case 'red':
                    max_red = max(max_red, count)
                case 'green':
                    max_green = max(max_green, count)
    return {
        'max_blue' : max_blue,
        'max_red' : max_red,
        'max_green' : max_green,
    }


def game_is_possible(max_values: dict, blue: int, red: int, green: int) -> bool:
    return max_values['max_blue'] <= blue \
        and max_values['max_red'] <= red \
        and max_values['max_green'] <= green


def get_game_id(line: str):
    index = line.index(':')
    return int(line[5:index])


def power_cube(max_values: dict) -> int:
    return max_values['max_blue'] * max_values['max_red'] * max_values['max_green']


if __name__ == '__main__':
    print('Advent of Code: Day 02')
    lines = read_lines('input.txt')

    possible_games = filter(lambda l: game_is_possible(get_max_values(l), 14, 12, 13), lines)
    sum_of_game_ids = sum(map(get_game_id, possible_games))
    print(f'Part 1: {sum_of_game_ids}')  # 2156

    sum_power = sum(map(lambda l: power_cube(get_max_values(l)), lines))
    print(f'Part 1: {sum_power}')  # 66909
