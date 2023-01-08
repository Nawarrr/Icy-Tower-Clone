from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from rectangle import Rectangle
import random


class Platform(Rectangle):
    PLATFORM_HEIGHT = 0.1

    def __init__(self, y: float) -> None:
        self.y = y
        self.randomize_platform()
        self.height = self.PLATFORM_HEIGHT

    def randomize_platform(self):
        self.x = random.uniform(-1, 1)
        self.width = random.uniform(0.3, 1)
        while self.x + self.width > 1:
            self.x = random.uniform(-1, 1)
