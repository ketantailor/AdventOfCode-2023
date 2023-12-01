#!/usr/bin/env python3


from collections.abc import Iterable


NUMBERS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def read_lines(input_file_name: str, strip = True) -> Iterable[str]:
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


def get_calibration_value(s: str) -> int:
    first = next(filter(str.isdigit, s))
    last = next(filter(str.isdigit, s[::-1]))

    return int(first + last)


def get_calibration_value_2(s: str) -> int:
    first, last = '', ''

    for i in range(len(s)):
        if s[i].isdigit():
            first = s[i]
            break
        for k, v in NUMBERS.items():
            if s[i:].startswith(k):
                first = v
                break
        if first:
            break

    for i in range(len(s) - 1, -1, -1):
        if s[i].isdigit():
            last = s[i]
            break
        for k, v in NUMBERS.items():
            if s[i:].startswith(k):
                last = v
                break
        if last:
            break

    return int(first + last)


if __name__ == '__main__':
    print('Advent of Code: Day 01')
    lines = read_lines('input.txt')

    ans1 = sum(map(get_calibration_value, lines))
    print(f'Part 1: {ans1}')  # 55208

    ans2 = sum(map(get_calibration_value_2, lines))
    print(f'Part 2: {ans2}')  # 54578
