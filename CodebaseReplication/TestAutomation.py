import pathlib
import turtle
import grid, agent, TileStatus
import time

# A class for automating the testing of 
# a folder of maps
# @author Derek
class TestAutomation:

    # Quietly executes the environment
    def executeEnv(self, testFile: str):
        testFile = pathlib.Path(testFile)
        # Load in grid from files
        board = grid.grid(testFile)
        topLeftX = board.TOPLEFT_X + (board.SQUARE_SIZE / 2)
        topLeftY = -topLeftX - board.SQUARE_SIZE
        # Instantiage agent in board
        # my spelling go brrr
        robot = agent.agent(topLeftX, topLeftY, board.SQUARE_SIZE, board)

        # 200 timesteps
        for i in range(200):
            # Do the action
            robot.move()
            # time.sleep(0.05)

        print(board)

        ## Evaulate success
        # TODO: Make an evaluator class with modular evaluation
        # functions?
        nonWall = 0
        clean = 0
        for i in range(board.rows):
            for j in range(board.columns):
                if board.getSquareStatus(i, j) == TileStatus.TileStatus.CLEAN:
                    clean += 1
                if board.getSquareStatus(i, j) != TileStatus.TileStatus.WALL:
                    nonWall += 1
        print(f"clean: {clean}/{nonWall}")
        print(f"% cleaned: {clean/nonWall}")

    # Executes the environment with visualization
    # stolen from Jason lol
    def executeEnvViz(self, testFile: str):
        testFile = pathlib.Path(testFile)
        screen = turtle.Screen()

        board = grid.grid(testFile)
        board.drawGrid(10, 10)
        topLeftX = board.TOPLEFT_X + (board.SQUARE_SIZE / 2)
        topLeftY = -topLeftX - board.SQUARE_SIZE
        a = agent.agent(topLeftX, topLeftY, board.SQUARE_SIZE, board)

        for i in range(200):
            # print(i)
            a.move()
            turtle.update()
            time.sleep(0.05)

        board = a.grid
        print(board)
        nonWall = 0
        clean = 0
        # TODO: make grid a class and have a method that counts tiles cleaned?
        for i in range(board.rows):
            for j in range(board.columns):
                if board.getSquareStatus(i, j) == TileStatus.TileStatus.CLEAN:
                    clean += 1
                if board.getSquareStatus(i, j) != TileStatus.TileStatus.WALL:
                    nonWall += 1
        print(f"clean: {clean}/{nonWall}")
        print(f"% cleaned: {clean/nonWall}")

        screen.exitonclick()

    # Executes all maps in the given folder path
    def runAll(self, testFolder: str):
        testFolder = pathlib.Path(testFolder)
        if not testFolder.is_dir():
            print(fr"This isn't a folder ¯\_(ツ)_/¯\n{testFolder}")
            exit()
        # glob searching for any txt files
        for mapFile in testFolder.glob("*.txt"):
            # TODO: Figure out how i want to print stats
            self.executeEnv(mapFile)

# If this file is ran directly,
# run the test automation
if __name__ == "__main__":
    automation = TestAutomation()
    #automation.executeEnv("CodebaseReplication/PS1_Files/map1.txt")
    automation.runAll("CodebaseReplication/PS1_Files/map1.txt")
