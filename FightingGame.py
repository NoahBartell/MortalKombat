import random
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QSpacerItem, QSizePolicy, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set up game class
        self.game = Game()

        #Window elements
        self.setWindowTitle("Fighting Game")
        
        self.mainWidget = QWidget()
        self.mainLayout = QGridLayout(spacing=0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainWidget.setLayout(self.mainLayout)
        
        self.mainLayout.addItem(QSpacerItem(5, 5, QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding), 0, 0)

        self.setFixedSize(QSize(1200, 800))
        self.setCentralWidget(self.mainWidget)

        #Styling
        borderRadius = 15
        buttonHeight = 32
        buttonFontSize = 50
        buttonFontWeight = "bold"
        buttonMargin = 10
        buttonPadding = 10
        buttonBaseStyle = f"border-radius: {borderRadius}px; height: {buttonHeight}px; font-size: {buttonFontSize}px; font-weight: {buttonFontWeight}; margin: {buttonMargin}px; padding: {buttonPadding}px; "
        redBackground = "background-color: red; "
        blueBackground = "background-color: blue; "
        greenBackground = "background-color: green; "
        purpleBackground = "background-color: purple; "
        orangeBackground = "background-color: orange; "
        labelFontSize = 50
        labelFontWeight = "bold"
        fontBaseStyle = f"font-size: {labelFontSize}px; font-weight: {labelFontWeight}; "


        #UI Components

        #labels
        self.yourMovesLabel = QLabel("Your Moves")
        self.yourMovesLabel.setStyleSheet(fontBaseStyle)
        self.moveChoosedLabel = QLabel("")
        self.moveChoosedLabel.setStyleSheet(fontBaseStyle)
        self.damageDealtLabel = QLabel("")
        self.damageDealtLabel.setStyleSheet(fontBaseStyle)
        self.movesLeftLabel = QLabel("Moves Left: 3")
        self.movesLeftLabel.setStyleSheet(fontBaseStyle)
        self.enemyDamageLabel = QLabel("")
        self.enemyDamageLabel.setStyleSheet(fontBaseStyle)
        self.playerHealthLabel = QLabel("Player Health: 100")
        self.playerHealthLabel.setStyleSheet(fontBaseStyle)
        self.enemyHealthLabel = QLabel("Enemy Health: 100")
        self.enemyHealthLabel.setStyleSheet(fontBaseStyle)
        self.gameStatusLabel = QLabel("")
        self.gameStatusLabel.setStyleSheet("font-size: 60px; font-weight: bold")

        #buttons
        self.punchButton = QPushButton("Punch")
        self.punchButton.setStyleSheet(buttonBaseStyle + redBackground)
        self.kickButton = QPushButton("Kick")
        self.kickButton.setStyleSheet(buttonBaseStyle + blueBackground)
        self.blockButton = QPushButton("Block")
        self.blockButton.setStyleSheet(buttonBaseStyle + greenBackground)
        self.specialButton = QPushButton("Special")
        self.specialButton.setStyleSheet(buttonBaseStyle + purpleBackground)
        self.fightButton = QPushButton("Fight")
        self.fightButton.setStyleSheet(buttonBaseStyle + orangeBackground)
        
        #Labels

        # Set size policy for buttons to expand horizontally and vertically
        self.punchButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.kickButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.blockButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.specialButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.fightButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        #Add components to layout
        self.mainLayout.addWidget(self.punchButton, 1, 0)
        self.mainLayout.addWidget(self.kickButton, 2, 0)
        self.mainLayout.addWidget(self.blockButton, 3, 0)
        self.mainLayout.addWidget(self.specialButton, 4, 0)
        self.mainLayout.addWidget(self.fightButton, 8, 0)
        self.mainLayout.addWidget(self.yourMovesLabel, 0, 0)
        self.mainLayout.addWidget(self.moveChoosedLabel, 6, 0)
        self.mainLayout.addWidget(self.damageDealtLabel, 1, 1)
        self.mainLayout.addWidget(self.movesLeftLabel, 7, 0)
        self.mainLayout.addWidget(self.enemyDamageLabel, 2, 1)
        self.mainLayout.addWidget(self.playerHealthLabel, 0, 1)
        self.mainLayout.addWidget(self.enemyHealthLabel, 4, 1)
        self.mainLayout.addWidget(self.gameStatusLabel, 8, 1)


        #Connect signals
        self.punchButton.clicked.connect(self.punchClicked)
        self.kickButton.clicked.connect(self.kickClicked)
        self.blockButton.clicked.connect(self.blockClicked)
        self.specialButton.clicked.connect(self.specialClicked)
        self.fightButton.clicked.connect(self.fightClicked)


        

    #Button functions
    def punchClicked(self):
        if len(self.game.yourMoves) < 3:
            moveString = ""
            self.game.AddMove("punch")
            self.movesLeftLabel.setText(f"Moves Left: {3 - len(self.game.yourMoves)}")
            for move in self.game.yourMoves:
                moveString += move + " "
            self.moveChoosedLabel.setText(moveString)
    def kickClicked(self):
        if len(self.game.yourMoves) < 3:
            moveString = ""
            for move in self.game.yourMoves:
                moveString += move + " "
            self.moveChoosedLabel.setText(moveString + "kick")
            self.game.AddMove("kick")
            self.movesLeftLabel.setText(f"Moves Left: {3 - len(self.game.yourMoves)}")
    def blockClicked(self):
        if len(self.game.yourMoves) < 3:
            moveString = ""
            for move in self.game.yourMoves:
                moveString += move + " "
            self.moveChoosedLabel.setText(moveString + "block")
            self.game.AddMove("block")
            self.movesLeftLabel.setText(f"Moves Left: {3 - len(self.game.yourMoves)}")
    def specialClicked(self):
        if len(self.game.yourMoves) < 3:
            moveString = ""
            for move in self.game.yourMoves:
                moveString += move + " "
            self.moveChoosedLabel.setText(moveString + "special")
            self.game.AddMove("special")
            self.movesLeftLabel.setText(f"Moves Left: {3 - len(self.game.yourMoves)}")
    def fightClicked(self):
        self.damageDealtLabel.setText("Damage Dealt to Enemy: " + self.game.RunMoves(self.game.yourMoves))
        self.game.enemyHealth -= int(self.game.RunMoves(self.game.yourMoves))
        self.enemyHealthLabel.setText("Enemy Health: " + str(self.game.enemyHealth))
        if self.game.enemyHealth <= 0:
            self.enemyHealthLabel.setText("Enemy Health: 0")
            self.gameStatusLabel.setText("You Won!")
            self.movesLeftLabel.setText("")
        self.game.ClearMoves()
        self.moveChoosedLabel.setText("")
        self.movesLeftLabel.setText("Moves Left: 3")
        damage = self.game.RunMoves(self.game.GetEnemyMoves())
        self.enemyDamageLabel.setText("Damage Dealt to Player: " + damage)
        self.game.health -= int(damage)
        self.playerHealthLabel.setText("Player Health: " + str(self.game.health))
        if self.game.health <= 0:
            self.playerHealthLabel.setText("Player Health: 0")
            self.gameStatusLabel.setText("You Lost!")
            self.movesLeftLabel.setText("")


class Game():
    #Game class to store game data
    def __init__(self):
        self.yourMoves = []
        self.enemyMoves = []
        self.fightingMoves = {
        "punch": 10,
        "kick": 15,
        "block": 5,
        "special": 20
    }
        self.health = 100
        self.enemyHealth = 100

    def AddMove(self, move):
        #Add a move to the list of moves
        self.yourMoves.append(move)

    def ClearMoves(self):
        #Clear the list of moves
        self.yourMoves = []

    def GetEnemyMoves(self):
        #Get the enemy moves
        self.enemyMoves = random.choices(list(self.fightingMoves.keys()), k=3)
        return self.enemyMoves

    def RunMoves(self, arr):
        #Run the moves in the array
        totalDamage = 0
        for move in arr:
            
            if move in self.fightingMoves:
                totalDamage += self.fightingMoves[move]
            else:
                print(f"ERR: Move {move} not found")
        return f"{totalDamage}"

    #Main function to run the program

app = QApplication(sys.argv)

window = MainWindow()
window.show()

while window.game.health > 0 and window.game.enemyHealth > 0:
    app.exec_()

app.quit()
#app.exec()
    # print("Welcome to the fighting game!")
    # print("Please enter 3 moves, you can choose from the following: ")
    # moves = []
    # for move in fightingMoves:
    #     print(f"{move}: {fightingMoves[move]}")
    # while len(moves) < 3:
    #     move = input(f"Enter move: ")
    #     if move in fightingMoves:
    #         moves.append(move)
    #     else:
    #         print(f"Move {move} not found")
    
    # RunMoves(moves)

    # enemyMoves = random.choices(list(fightingMoves.keys()), k=3)
    # print("Enemy attacks: ")
    # print(f"Enemy damage: {RunMoves(enemyMoves)}")


# if __name__ == "__main__":
#     main()
