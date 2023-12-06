from pathlib import Path

def readlines():
    input_file = Path(__file__).parent / 'input.txt'
    with open(input_file, 'r') as f:
        return f.readlines()

example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def parse_game_record(game_record):
    game_id, round_info = game_record[5:].split(':')
    rounds = []
    for r in round_info.strip().split(';'):
        _round = {}
        for count_colors in r.strip().split(','):
            count, color = count_colors.strip().split(' ')
            _round.update({color: int(count)})
        rounds.append(_round)
    return {'game_id': int(game_id), 'rounds': rounds}

game_bag = {'red': 12, 'green': 13, 'blue': 14}

def is_valid_game(game):
    for round in game['rounds']:
        for color, count in round.items():
            if count > game_bag[color]:
                return False
    return True

def sum_of_valid_game_ids(games):
    return sum(game['game_id'] for game in games if is_valid_game(game))

def find_min_pieces_per_color_in_game(game):
    min_pieces_per_color = {}
    for round in game['rounds']:
        for color, count in round.items():
            if color not in min_pieces_per_color:
                min_pieces_per_color[color] = count
            else:
                min_pieces_per_color[color] = max(min_pieces_per_color[color], count)
    return min_pieces_per_color

def power_of_game_bag_set(bag):
    _power = 1
    for count in bag.values():
        _power *= count
    return _power

def sum_power_of_game_bag_sets(games):
    sum_of_power = 0
    for game in games:
        min_pieces_per_color = find_min_pieces_per_color_in_game(game)
        sum_of_power += power_of_game_bag_set(min_pieces_per_color)
    return sum_of_power

if __name__ == '__main__':
    example_games = [parse_game_record(game) for game in example.split('\n')]
    assert sum_of_valid_game_ids(example_games) == 8

    input_games = [parse_game_record(game) for game in readlines()]
    assert sum_of_valid_game_ids(input_games) == 2406

    assert sum_power_of_game_bag_sets(example_games) == 2286

    assert sum_power_of_game_bag_sets(input_games) == 78375