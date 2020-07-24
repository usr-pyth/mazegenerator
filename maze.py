import pygame as pg
import cell


class Maze:
    def CheckFinished(self):
        ct = 0
        for i in range(self.cols):
            for j in range(self.rows):
                if self.maze[i][j].visited:
                    ct += 1
        return ct == self.cols * self.rows

    def GenStep(self):
        if self.currentCell == None:
            self.currentCell = self.maze[self.startCoords[0]
                                         ][self.startCoords[1]]
            self.stack.append(self.currentCell)
        else:
            self.currentCell.visited = True
            self.currentCell = self.currentCell.PickNextCell()

    def Generate(self, animated):
        while not self.done:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    sys.exit()
            self.done = self.CheckFinished()
            self.GenStep()
            if animated:
                self.Show()
                pg.time.wait(int(1000 / self.frameRate))
        pg.display.set_caption("Python Maze Generator | Finished")

    def Show(self):
        self.screen.fill((150, 150, 150))
        for i in range(self.cols):
            for j in range(self.rows):
                self.maze[i][j].Show()
        pg.display.flip()

    def __init__(self, rows, cols, scl, screen, fr):
        self.rows = rows
        self.cols = cols
        self.maze = []
        self.scl = scl
        self.currentCell = None
        self.startCoords = [0, 0]
        self.finishCoords = [rows-1, cols-1]
        self.done = False
        self.screen = screen
        self.stack = []
        self.frameRate = fr
        for i in range(cols):
            col = []
            for j in range(rows):
                col.append(cell.Cell(i, j, self, screen))
            self.maze.append(col)
