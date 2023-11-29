class Game:
    
    questionDict = {
        "Welcome to the game! Thing of a design pattern and answer these yes/no questions! Ready?":["does it provide an object creation mechanism that enhances the flexibilities of the existing code?", "stop"],
        }

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
        while run == "go":
            self.showQuestion("Welcome to the game! Thing of a design pattern and answer these yes/no questions! Ready?", "does", "stop")





runGame = Game

runGame.gameStart()
