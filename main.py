class Game:

    def __init__(self):
        self.questionDict = {
                "done":["Woohoo! I guessed correctly! Try again?", "1", "stop"],
                "wrong":["Oops! Something went wrong! Try again?", "1", "stop"],
                "1":["Welcome to the game! Think of a design pattern and answer these following yes/no question?", "2", "stop"],
                "2":["Does it provide the oject creation mechanisms that enhance the flexabilities of the existing codes?", "3", "4"],
                "3":["Does it ensure that you have at most one instance of a class in your application?", "5", "6",],
                "5":["is it the Singleton Design Pattern?", "done", "wrong"],
                "6":["is it the Builder Design Pattern?", "done", "wrong"],
                "4":["Is it respobsible for how classes communicate with each others?", "7", "8"],
                "7":["Does it provide a mechanism to the context to change it's behavior?","9", "10"],
                "9":["Is changing behavior built into it's scheme?", "11", "12"],
                "10":["Does it allow a group of objects to be notified when some state changes? ", "13", "14"],
                "11":["Is it the state pattern?", "done", "wrong"],
                "12":["Is it the strategy pattern?", "done", "wrong"],
                "13":["Is it the Observer Pattern?", "done", "wrong"],
                "14":["Is it the Commander Pattern", "done", "wrong"],
                "8":["Does it explain how to assemble objects and classes into a larger structure and simplifies the structure by indentifiying the relationship", "15", "stop"],
                "15":["Does it attach additional behavior to an object dynamically at run time", "16", "17"],
                "16":["is it the Decorator Pattern?", "done", "wrong"],
                "17":["Is it the Adapter Pattern?", "done", "wrong"]
            }
    
    def answerYes(self, nextQuestion):
        self.showQuestion(nextQuestion)

    def answerNo(self, nextQuestion):
        self.showQuestion(nextQuestion)

    def stopGame(self):
        exit()

    def showQuestion(self, question):
        quesText = question[0]
        ansYes = question[1]
        ansNo = question[2]
        print(quesText+"\n"+ansYes+"\n"+ansNo+"\n")
        print("(1)Yes or (2)No?: ")
        ans = str(input())
        if ans == "1":
            self.answerYes(self.questionDict[str(ansYes)])
        if ans == "2":
            if question[2] == "stop":
                self.stopGame()
            else:    
                self.answerNo(self.questionDict[question[2]])
        else:
            self.showQuestion(question)                   

    def gameStart(self):
        self.showQuestion(self.questionDict["1"])




runGame = Game()

runGame.gameStart()
