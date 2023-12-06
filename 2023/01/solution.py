from pathlib import Path


def readlines():
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file, "r") as f:
        return f.readlines()


def find_first_and_last_digit(input_str):
    # Find the first digit
    first_digit = next((char for char in input_str if char.isdigit()), None)

    # Find the last digit
    reversed_str = input_str[::-1]
    last_digit = next((char for char in reversed_str if char.isdigit()), None)

    return first_digit, last_digit


def to_int(digits):
    return int("".join(digits))


def sum_of_all_calibration_values(calibration_document):
    return sum(to_int(find_first_and_last_digit(line)) for line in calibration_document)


def find_first_and_last_occuring_substring_from_list_of_substrings(
    input_str, substrings
):
    first_substring = None
    first_index = None
    last_substring = None
    last_index = None

    for substring in substrings:
        if substring in input_str:
            if first_substring is None:
                first_substring = substring
                first_index = input_str.index(substring)
                last_substring = substring
                last_index = input_str.rindex(substring)
            else:
                if input_str.index(substring) < first_index:
                    first_substring = substring
                    first_index = input_str.index(substring)
                if input_str.rindex(substring) > last_index:
                    last_substring = substring
                    last_index = input_str.rindex(substring)
    return first_substring, last_substring


digit_value_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def sum_of_all_calibration_values_with_letter_digits(calibration_document):
    total = 0
    for line in calibration_document:
        first, last = find_first_and_last_occuring_substring_from_list_of_substrings(
            line, digit_value_map.keys()
        )
        total += int(f"{digit_value_map[first]}{digit_value_map[last]}")
    return total


example = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
example_part_2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]
if __name__ == "__main__":
    assert sum_of_all_calibration_values(example) == 142

    input_lines = readlines()
    assert sum_of_all_calibration_values(input_lines) == 55172

    assert sum_of_all_calibration_values_with_letter_digits(example_part_2) == 281
    assert sum_of_all_calibration_values_with_letter_digits(input_lines) == 54925
