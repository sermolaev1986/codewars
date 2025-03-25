# https://www.codewars.com/kata/587136ba2eefcb92a9000027

class Player():
    def __init__(self, number):
        self.square = 0
        self.number = number

class SnakesLadders():

    def __init__(self):
        self.shortcuts = {
            # ladders
            2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94,
            # snakes
            99:80, 95:75, 92:88, 89:68, 74:53, 64:60, 62:19, 49:11, 46:25, 16:6
        }

        self.player1 = Player(1)
        self.player2 = Player(2)

        self.current_player = self.player1

    def play(self, die1, die2):
        if self.player1.square == 100 or self.player2.square == 100:
            return "Game over!"

        result = self.do_play(self.current_player, die1, die2)
        if die1 != die2:
            self.switch_player()

        return result

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def do_play(self, player, die1, die2):
        player.square += die1 + die2

        if player.square == 100:
            return "Player %s Wins!" % player.number

        if player.square > 100:
            player.square = 200 - player.square
        if player.square in self.shortcuts:
            player.square = self.shortcuts[player.square]

        return "Player %s is on square %s" % (player.number, player.square)
