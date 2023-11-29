class Game:

    def buildDictionary(self):
        questionDict = {}
        return questionDict

    def answerYes(self, nextQuestion):
        self.showQuestion(nextQuestion, "1", "2")

    def answerNo(self, nextQuestion):
        self.showQuestion(nextQuestion, "1,", "2")

    def stopGame(self):
        exit()

    def showQuestion(self, question, nextY, nextN):
        print(question, "\n")
        print("(1)Yes or (2)No?: ")
        ans = input()
        if ans == "1":
            self.answerYes(nextY)
            
        if ans == "2":
            if nextN == "stop":
                self.stopGame()
            else:    
                self.answerNo(nextN)
        
        else:
            self.showQuestion(question, nextY, nextN)                   

    def gameStart(self):
        run = "go"




runGame = Game

runGame.gameStart()
