from lib.Counter import Counter
from lib.Computer import Computer
from pick import pick


class Game():
    isGameRunning = True
    games = 0
    options = ["Kamień", "Papier", "Nożyce"]

    def __init__(self, gamesToPlay=1):
        self.gamesToPlay = gamesToPlay

    def initGame(self):
        computer = Computer(self.options)
        counter = Counter()
        playerOptions = self.options

        while(self.isGameRunning == True and self.games < self.gamesToPlay):
            self.games += 1
            title = "Wybierz mądrze:"
            playerChoice, index = pick(playerOptions, title,
                                       indicator='->', default_index=1)
            counter.checkRoundWinner(playerChoice, computer.choice())

            if self.games == self.gamesToPlay - 1:
                self.isGameRunning == False
                counter.checkWinner()


answerIsCorrect = False


def checkInputIsNum(input):
    try:
        int(input)
        return True
    except:
        return False


while(not answerIsCorrect):
    games = input("Ile rund chcesz rozegrać? -> ")
    if checkInputIsNum(games):
        answerIsCorrect = True
        game = Game(int(games))
        game.initGame()
    elif games == 'exit':
        answerIsCorrect = True
    else:
        print('Podaj liczbę, lub wyjdź słowem "exit"')
