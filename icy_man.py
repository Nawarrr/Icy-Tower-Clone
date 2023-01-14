from rectangle import Rectangle
from typing import NewType

rectangle = NewType("Rectangle", object)


class IcyMan(Rectangle):
    PRECESION_CONSTANT: int = 100

    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        super().__init__(x, y, width, height)
        self.__score = 0
        self.jumps = 2
        self.moment_left = 0
        self.moment_right = 0

    def is_standing_on(self, rectangle: rectangle) -> bool:
        if (
            (self.x > rectangle.x and self.x < rectangle.x + rectangle.width)
            or (
                self.x + self.width > rectangle.x
                and self.x + self.width < rectangle.x + rectangle.width
            )
        ) and (
            int(self.y * self.PRECESION_CONSTANT)
            == int((rectangle.y + rectangle.height) * self.PRECESION_CONSTANT)
        ):
            self.jumps = 2
            return True
        else:
            return False

    def in_screen_right(self, distance_jumped=0):
        return self.x + self.width + distance_jumped < 1

    def in_screen_left(self, distance_jumped=0):
        print(self.x, distance_jumped)
        return self.x > -1 + distance_jumped

    def jump(self, distance: float) -> None:
        if self.jumps > 0:
            self.move_up(distance)
        self.jumps -= 1

    def get_score(self):
        return self.__score

    def inc_score(self):
        self.__score += 1

    def move_right(self, distance: float) -> None:
        self.moment_right += distance
        self.moment_left = 0
        return super().move_right(distance)

    def move_left(self, distance: float) -> None:
        self.moment_left += distance
        self.moment_right = 0
        return super().move_left(distance)
