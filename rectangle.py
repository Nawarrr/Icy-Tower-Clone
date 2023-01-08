from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self) -> None:
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex2f(self.x, self.y)
        glTexCoord2f(1, 0)
        glVertex2f(self.x + self.width, self.y)
        glTexCoord2f(1, 1)
        glVertex2f(self.x + self.width, self.y + self.height)
        glTexCoord2f(0, 1)
        glVertex2f(self.x, self.y + self.height)
        glEnd()

    def move_right(self, distance: float) -> None:
        self.x += distance

    def move_left(self, distance: float) -> None:
        self.x -= distance

    def move_up(self, distance: float) -> None:
        self.y += distance

    def move_down(self, distance: float) -> None:
        self.y -= distance
