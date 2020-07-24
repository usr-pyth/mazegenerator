import maze
import pygame as pg
import sys

frameRate = 0
width = 1000
height = 1000
ct = int(input("Input Size \n"))
anim = False
if input("Would You Like The Generation To Be Animated? (y/n) \n") == "y":
    anim = True
    while frameRate <= 0:
        frameRate = int(
            input("Input Framerate \n (Limited By Computer Specs, Positive Nonzero Number) \n"))
scl = int(width / ct)
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Python Maze Generator | Generating...")
maze = maze.Maze(ct, ct, scl, screen, frameRate)
maze.Generate(anim)


while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit()
    maze.currentCell = None
    maze.Show()
    pg.display.flip()
    pg.image.save(
        screen, f'maze__{ct}x{ct}_maze.jpg')
