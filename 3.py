# https://www.codewars.com/kata/5c1448e08a2d87eda400005f

def calculate_direction(direction):
    direction_map = {
        '↗': (-1, 1), '↘': (1, 1), '↖': (-1, -1), '↙': (1, -1),
        '↑': (-1, 0), '↓': (1, 0), '←': (0, -1), '→': (0, 1)
    }
    return direction_map.get(direction, None)

# calculates euclidean distance between two coordinates
def calculate_distance(coordinate1, coordinate2):
    return ((coordinate1[0] - coordinate2[0]) ** 2 + (coordinate1[1] - coordinate2[1]) ** 2) ** 0.5

def count_deaf_rats(town_square):
    rats = []
    piper = None

    for i in range(len(town_square)):
        print(f"Row {i}: {town_square[i]}")
        row = town_square[i]
        for j in range(len(row)):
            print(f"  Column {j}: {row[j]}")
            char = row[j]
            if char == 'P':
                print("Got piper at ", (i, j))
                piper = (i, j)
            elif char in ['↗', '↘', '↖', '↙', '↑', '↓', '←', '→']:
                rats.append((i, j, char))

    if not piper:
        return 0

    deaf_rats = 0
    for (rat_row, rat_column, direction) in rats:
        (row_diff, column_diff) = calculate_direction(direction)
        next_coordinate = (rat_row + row_diff, rat_column + column_diff)
        if calculate_distance(next_coordinate, piper) > calculate_distance((rat_row, rat_column), piper):
            print(f"Rat at ({rat_row}, {rat_column}) is deaf")
            deaf_rats += 1

    return deaf_rats


def assert_equals(actual, expected):
    if expected != actual:
        raise AssertionError(f"Expected {expected}, but got {actual}")

if __name__ == '__main__':
    s = """
    ↗ P
      ↘    ↖
      ↑
    ↗
    """.strip("\n").split("\n")
    assert_equals(count_deaf_rats(s), 1)

    s = """
            ↗
    P ↓   ↖ ↑
        ←   ↓
      ↖ ↙   ↙
    ↓ ↓ ↓
    """.strip("\n").split("\n")
    assert_equals(count_deaf_rats(s), 7)

    s = """
    ↘ ↓ ↙
    → P ←
    ↗ ↑ ↖
    """.strip("\n").split("\n")
    assert_equals(count_deaf_rats(s), 0)

    s = """
    ↖ ↑ ↗
    ← P →
    ↙ ↓ ↘
    """.strip("\n").split("\n")
    assert_equals(count_deaf_rats(s), 8)