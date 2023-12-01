from pathlib import Path

def find_first_and_last_digit(input_str):
    # Find the first digit
    first_digit = next((char for char in input_str if char.isdigit()), None)

    # Find the last digit
    reversed_str = input_str[::-1]
    last_digit = next((char for char in reversed_str if char.isdigit()), None)

    return first_digit, last_digit

def to_int(digits):
    return int(''.join(digits))


def sum_of_all_calibration_values(calibration_document):
    return sum(to_int(find_first_and_last_digit(line))  for line in calibration_document)


example = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
input_file = Path(__file__).parent / 'input.txt'

if __name__ == '__main__':
    assert sum_of_all_calibration_values(example) == 142

    with open(input_file, 'r') as f:
        solution = sum_of_all_calibration_values(f.readlines())
    assert solution == 55172