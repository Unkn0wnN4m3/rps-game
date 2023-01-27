# Rock, paper or scissors game.
# Game from Microsoft OOP.


class Participant:

    def __init__(self, name) -> None:
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self) -> None:
        user_selection = input(
            str("\n{name}, select between rock, paper or scissor: ".format(
                name=self.name)))

        if user_selection not in ["rock", "paper", "scissor"]:
            raise Exception("Not a valid option [rock, paper, scissor]")
        else:
            self.choice = user_selection
            print("{name} selects {choice}".format(name=self.name,
                                                   choice=self.choice))

    def toNumericalChoice(self) -> int:
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,
        }
        return switcher[self.choice]

    def incrementPoint(self) -> None:
        self.points += 1


class GameRound:

    def __init__(self, p1, p2) -> None:
        self.rules = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print("\nRound resulted in a {result}".format(
            result=self.getResultAsString(result)))

        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self, result) -> str:
        res = {
            0: "draw",
            1: "win",
            -1: "loss",
        }
        return res[result]


class Game:

    def __init__(self, p1, p2) -> None:
        self.endGame = False
        self.participant = Participant(p1)
        self.secondParticipant = Participant(p2)

    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print(
                "\nGame ended, {p1name} has {p1points}, and {p2name} has {p2points}"
                .format(p1name=self.participant.name,
                        p1points=self.participant.points,
                        p2name=self.secondParticipant.name,
                        p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "\nIt's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(
                name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(
                name=self.secondParticipant.name)
        print(resultString)

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()


if __name__ == "__main__":
    print("\n+++ Rock, paper or scissors game +++\n")
    p1 = input(str("Tell me your name player 1: "))
    p2 = input(str("Tell me your name player 2: "))
    game = Game(p1, p2)
    game.start()
