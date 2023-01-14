from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from typing import List, NewType
import functools
import operator
import pygame
from rectangle import Rectangle
from icy_man import IcyMan
from jumping_platform import Platform
from material import Material
import os


def iterate():
    glViewport(0, 0, 800, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# Pygame initialization
pygame.init()
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
pygame.display.gl_set_attribute(
    pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE
)
pygame.display.set_mode(
    (1, 1), pygame.OPENGL | pygame.DOUBLEBUF
)  # 1,1 will open a 1x1 pixel window
clock = pygame.time.Clock()

icy_man_x: float = -0.1
icy_man_y: float = -1
width: float = 0.1
height: float = 0.2
game_started: bool = False
icy_man = IcyMan(icy_man_x, icy_man_y, width, height)
platform1 = Platform(-0.5)
platform2 = Platform(0)
platform3 = Platform(0.5)
platform4 = Platform(-1)
platforms = [
    platform1,
    platform2,
    platform3,
    platform4,
]
background = Rectangle(-1, -1, 2, 2)
# The materials are set to none as a work around to avoid using Material() before initalizing pygame
man_material = None
platform_material = None
background_material = None
game_ended = False


def keys(k, x, y):
    global icy_man, game_started
    if k == GLUT_KEY_UP:
        icy_man.jump(0.6 + (icy_man.moment_right + icy_man.moment_left) / 2)
        game_started = True
        if icy_man.moment_left > 0:
            if icy_man.in_screen_left(icy_man.moment_left):
                icy_man.move_left(icy_man.moment_left / 2)

            icy_man.moment_left = 0
        elif icy_man.moment_right > 0:
            if icy_man.in_screen_right(icy_man.moment_right / 2):
                icy_man.move_right(icy_man.moment_right / 2)

            icy_man.moment_right = 0
    if k == GLUT_KEY_RIGHT:
        if icy_man.in_screen_right():
            icy_man.move_right(0.05)

    if k == GLUT_KEY_LEFT:
        if icy_man.in_screen_left():
            icy_man.move_left(0.05)
    if k == GLUT_KEY_DOWN:
        if game_ended:
            os.execl(sys.executable, sys.executable, *sys.argv)


def text(x, y, color, text):
    glColor(*color)
    glRasterPos2d(x, y)
    glutBitmapString(GLUT_BITMAP_HELVETICA_18, str(text).encode("ascii"))
    glColor(1, 0, 0)


def end_screen():
    final_background = Rectangle(-1, -1, 2, 2)
    final_background_material = Material("res/background1.png")
    man_material.destroy()
    platform_material.destroy()
    background_material.destroy()
    final_background_material.use()
    final_background.draw()
    text(-0.5, 0.3, (0, 0, 0), "You Lost")
    text(-0.2, 0, (0, 0, 0), "Your Score is " + str(icy_man.get_score()))
    return


def game_screen():
    """
    This function is called for every frame to show the screen.
    """
    global clock, icy_man, platforms, man_material, platform_material, background_material, game_started, game_ended

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0, 1.0, 1.0)
    iterate()
    if not game_started:
        text(-0.5, 0.3, (1, 1, 1), "Welcome to a simplified version of Icy Tower")
        text(-0.2, 0, (1, 1, 1), "Press [UP] to start")

    elif game_ended:
        final_background = Rectangle(-1, -1, 2, 2)
        final_background_material = Material("res/background1.png")
        man_material.destroy()
        platform_material.destroy()
        background_material.destroy()
        final_background_material.use()
        final_background_material.destroy()
        final_background.draw()
        text(-0.1, 0.1, (0, 0, 0), "You Lost")
        text(-0.15, 0, (0, 0, 0), "Your Score is " + str(icy_man.get_score()))
    else:
        # materials instances instantiation
        if not man_material:
            man_material = Material("res/body.png")
        if not platform_material:
            platform_material = Material("res/icy2.png")
        if not background_material:
            background_material = Material("res/background.png")

        # Drawing
        background_material.use()
        background.draw()

        for platform in platforms:
            platform_material.use()
            platform.draw()

        man_material.use()
        icy_man.draw()
        # print(icy_man.moment_left, icy_man.moment_right)
        # Gravity
        if game_started:

            if not functools.reduce(
                operator.or_, map(icy_man.is_standing_on, platforms)
            ):
                icy_man.move_down(0.01)

            for platform in platforms:
                platform.move_down(
                    0.003 * (platform.acceleration_factor**platform.level)
                )
            if icy_man.y + icy_man.height < -1:
                # End Game
                game_ended = True

        for platform in platforms:
            if platform.y + platform.height < -1:
                platform.randomize_platform()
                platform.y = 1
                platform.level += 1
                icy_man.inc_score()
                print(icy_man.get_score())

        clock.tick(40)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL")
glutSpecialFunc(keys)
glutDisplayFunc(game_screen)
glutIdleFunc(game_screen)
glutMainLoop()
