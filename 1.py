# https://www.codewars.com/kata/5384df88aa6fc164bb000e7d/python
class Player:
    # Constructor
    def __init__(self, cakes):
        pass

    # Decide who moves first
    def firstmove(self, cakes):
        return cakes > 1 and cakes % 4 != 2

    # Decide your next move
    def move(self, cakes, last):
        if cakes == 1:
            # Must take the last cake
            return 1

        # 2, 3, 6, 7, 10, 11, 14, 15, 18, 19, ...
        if cakes % 4 in [2, 3]:
            # have to take the losing 2 if 1 was the last (for 3, both 1 and 2 are winning)
            return 1 if last != 1 else 2
        # 4, 5, 8, 9, 12, 13, 16, 17, 20, 21, ...
        elif cakes % 4 in [0, 1]:
            # have to take the losing 2 if 3 was the last
            return 3 if last != 3 else 2


def plural(x):
    return f"{x} cake{('' if x == 1 else 's')}"


def game(n, opponent, debug=True):
    def debug_msg(msg):
        if debug:
            print(msg)

    cakes = n
    debug_msg(f"The game started: {plural(cakes)} on the table")
    players = [Player(cakes), opponent(cakes)]
    names = ["You", "Opponent"]
    outcomes = [False, True]
    current = 0 if players[0].firstmove(cakes) else 1
    last = 0
    while True:
        move = players[current].move(cakes, last)
        if not move in [1, 2, 3]: raise ValueError("Illegal move, must be 1, 2 or 3")
        if move == last: raise ValueError("Illegal move, cannot copy opponent's move")
        if move > cakes: raise ValueError("Illegal move, insufficient cakes on the table")
        cakes -= move
        last = move
        debug_msg(f"{names[current]} ate {plural(move)}, {plural(cakes)} left")
        if not cakes:
            debug_msg(f"{names[current]} ate the last cake!")
            return outcomes[current]
        if last == 1 and cakes == 1:
            debug_msg(f"{names[current]} led to the stalemate and lost!")
            return outcomes[current]
        current = 1 - current


class SampleAI:
    def __init__(self, cakes):
        pass

    def move(self, cakes, last):
        return 1 if last != 1 else 2


class GreedyAI:
    def __init__(self, cakes):
        pass

    def move(self, cakes, last):
        valid_moves = []
        for move in [1, 2, 3]:
            if move <= cakes and move != last:
                valid_moves.append(move)

        return max(valid_moves)


if __name__ == '__main__':
    opponents = [SampleAI, GreedyAI, Player]
    for opponent in opponents:
        print("----------------------------------------")
        print("Testing the game against", opponent.__name__)
        CASES = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        for cakes in CASES:
            result = game(cakes, opponent)
            print(result)
            if result is False:
                raise AssertionError("lost game to {} with {} cakes".format(opponent.__name__, cakes))
