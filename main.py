class Game:
    
    questionDict = {}

    def answerYes(self, nextQuestion):
        pass

    def answerNo(self, nextQuestion):
        pass

    def showQuestion(self, question, nextY, nextN):
        print(question, "\n")
        print("(1)Yes or (2)No?: ")
        ans = input()
        if ans == "1":
            self.answerYes(nextY)
            
        if ans == "2":
            self.answerNo(nextN)
        
        else:
            print("Please type either 1 or 2")                    

    def gameStart():
        print("the game has started")



runGame = Game

runGame.gameStart()
