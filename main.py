class Game:

    questionDict = {
            "1":["this is question 1", "2", "stop"], "2":["This is question 2", "3", "4"], "3":["This is question 3", "1", "stop",],
            "4":["This is question 4", "1", "stop"]    
        }
    
    def answerYes(self, nextQuestion):
        self.showQuestion(nextQuestion[0])

    def answerNo(self, nextQuestion):
        self.showQuestion(nextQuestion[0])

    def stopGame(self):
        exit()

    def showQuestion(self, question):
        print(question[0], "\n")
        print("(1)Yes or (2)No?: ")
        ans = input()
        if ans == "1":
            self.answerYes(self.questionDict[1])
            
        if ans == "2":
            if nextN == "stop":
                self.stopGame()
            else:    
                self.answerNo(self.questionDict[2])
        
        else:
            self.showQuestion(question)                   

    def gameStart(self):
        run = "go"




runGame = Game

runGame.gameStart()
