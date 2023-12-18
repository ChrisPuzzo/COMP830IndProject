class Game:

    def __init__(self):
        self.questionDict = {
                "done":["Woohoo! I guessed correctly! Try again?", "1", "stop"],
                "wrong":["Oops! Something went wrong! Try again?", "1", "stop"],
                "1":["Welcome to the game! Think of a design pattern and answer these following yes/no question?", "2", "stop"],
                "2":["Does it provide the oject creation mechanisms that enhance the flexabilities of the existing codes?", "3", "4"],
                "3":["Does it ensure that you have at most one instance of a class in your application?", "5", "6",],
                "4":["Is it respobsible for how classes communicate with each other?"],
                "5":["is it the Singleton Design Pattern?", "done", "wrong"],
                "6":["is it the Builder Design Pattern?", "done", "wrong"],
                
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
