from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vertex1 = None
        self.vertex2 = None
        self.vertex3 = None
        self.vertex4 = None

    def draw(self, rotate=False) -> None:
        glBegin(GL_QUADS)
        if rotate:
            glRotate(10, 0, 0, 1)
            glTexCoord2f(0, 0)
            glVertex2f(self.x, self.y)

            glRotate(10, 0, 0, 1)
            glTexCoord2f(1, 0)
            glVertex2f(self.x + self.width, self.y)

            glRotate(10, 0, 0, 1)
            glTexCoord2f(1, 1)
            glVertex2f(self.x + self.width, self.y + self.height)

            glRotate(10, 0, 0, 1)
            glTexCoord2f(0, 1)
            glVertex2f(self.x, self.y + self.height)

        else:
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
