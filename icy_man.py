from rectangle import Rectangle
from typing import NewType

rectangle = NewType("Rectangle", object)


class IcyMan(Rectangle):
    PRECESION_CONSTANT: int = 100

    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        super().__init__(x, y, width, height)
        self.__score = 0

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
            return True
        else:
            return False

    def in_screen_right(self):
        return self.x + self.width < 1

    def in_screen_left(self):
        return self.x > -1

    def jump(self, distance: float) -> None:
        self.move_up(distance)

    def get_score(self):
        return self.__score

    def inc_score(self):
        self.__score += 1
