import pygame as pg
import random


class Cell:
    def __init__(self, i, j, maze, screen):
        self.i = i
        self.j = j
        self.maze = maze
        self.walls = {"t": True, "b": True, "l": True, "r": True}
        self.visited = False
        self.screen = screen
        self.scl = maze.scl

    def GetNeighbors(self):
        n = {"l": None, "r": None, "t": None, "b": None}

        # Check Left
        if self.i > 0:
            n["l"] = self.maze.maze[self.i-1][self.j]

        if self.i <= 0 or n["l"].visited:
            n.pop("l")

        # Check Right
        if self.i < self.maze.cols - 1:
            n["r"] = self.maze.maze[self.i+1][self.j]
        if self.i >= self.maze.cols - 1 or n["r"].visited:
            n.pop("r")

        # Check Top
        if self.j > 0:
            n["t"] = self.maze.maze[self.i][self.j-1]
        if self.j <= 0 or n["t"].visited:
            n.pop("t")

        # Check Bottom
        if self.j < self.maze.rows - 1:
            n["b"] = self.maze.maze[self.i][self.j+1]
        if self.j >= self.maze.rows - 1 or n["b"].visited:
            n.pop("b")
        return n

    def PickNextCell(self):
        n = self.GetNeighbors()
        nextCell = None
        if len(n) > 0:
            ind = random.randint(0, len(n) - 1)
            k = list(n.keys())[ind]
            nextCell = n[k]
            if k == "l":
                self.walls["l"] = False
                nextCell.walls["r"] = False
            elif k == "r":
                self.walls["r"] = False
                nextCell.walls["l"] = False
            elif k == "t":
                self.walls["t"] = False
                nextCell.walls["b"] = False
            else:
                self.walls["b"] = False
                nextCell.walls["t"] = False
            self.maze.stack.append(nextCell)
        else:
            nextCell = self.maze.stack.pop(len(self.maze.stack) - 1)
        return nextCell

    def Show(self):
        c = None
        strokeWeight = 2
        startCell = self.maze.startCoords
        endCell = self.maze.finishCoords
        if self == self.maze.currentCell:
            c = (150, 50, 50)
        elif not self.visited:
            c = (100, 100, 100)
        elif self.maze.done and (self == self.maze.maze[endCell[0]][endCell[1]] or self == self.maze.maze[startCell[0]][startCell[1]]):
            c = (150, 50, 50)
        if c != None:
            pg.draw.rect(self.screen, c, pg.Rect(
                self.i * self.scl, self.j * self.scl, self.scl, self.scl))

        if self.walls["l"]:
            pg.draw.line(
                self.screen,
                (0, 0, 0),
                (self.i*self.scl, self.j * self.scl),
                (self.i*self.scl, (self.j+1)*self.scl),
                strokeWeight
            )
        if self.walls["r"]:
            pg.draw.line(
                self.screen,
                (0, 0, 0),
                ((self.i+1)*self.scl, self.j * self.scl),
                ((self.i+1)*self.scl, (self.j+1)*self.scl),
                strokeWeight
            )
        if self.walls["t"]:
            pg.draw.line(
                self.screen,
                (0, 0, 0),
                (self.i*self.scl, self.j * self.scl),
                ((self.i+1)*self.scl, self.j*self.scl),
                strokeWeight
            )
        if self.walls["b"]:
            pg.draw.line(
                self.screen,
                (0, 0, 0),
                (self.i*self.scl, (self.j+1) * self.scl),
                ((self.i+1)*self.scl, (self.j+1)*self.scl),
                strokeWeight
            )
