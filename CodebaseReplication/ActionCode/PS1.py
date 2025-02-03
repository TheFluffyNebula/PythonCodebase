import Action
import TileStatus
'''
getAction for problem set 1
method: if we see a dirty tile, go to it and clean it
'''
def getAction(self):
    curStatus = self.grid.getSquareStatus(self.i, self.j)
    leftStatus = self.grid.getSquareStatus(self.i, self.j - 1)
    rightStatus = self.grid.getSquareStatus(self.i, self.j + 1)
    aboveStatus = self.grid.getSquareStatus(self.i - 1, self.j)
    belowStatus = self.grid.getSquareStatus(self.i + 1, self.j)

    if curStatus == TileStatus.DIRTY:
        return Action.CLEAN
    if leftStatus == TileStatus.DIRTY:
        return Action.LEFT
    if belowStatus == TileStatus.DIRTY:
        return Action.DOWN
    if rightStatus == TileStatus.DIRTY:
        return Action.RIGHT
    if aboveStatus == TileStatus.DIRTY:
        return Action.UP
    return Action.DO_NOTHING
