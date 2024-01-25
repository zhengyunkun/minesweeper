class Piece():
    def __init__(self, hasMine):
        self.hasMine = hasMine
        self.clicked = False
        self.flagged = False

    def getHasMine(self):
        return self.hasMine
    
    def getClicked(self):
        return self.clicked
    
    def getFlagged(self):
        return self.flagged
    
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumAround()

    def setNumAround(self):
        self.numAround = 0
        for neighbor in self.neighbors:
            if neighbor.getHasMine():
                self.numAround += 1

    def getNumAround(self):
        return self.numAround
    
    def toggleFlag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True

    def getNeighbors(self):
        return self.neighbors