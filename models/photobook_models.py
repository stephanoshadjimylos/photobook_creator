from builtins import object


class SingleSquare(object):
    def __init__(self, position, photobook_width, photobook_height):
        self.mode = 0
        self.image_height = 700
        self.image_width = 700
        self.position = (
            (photobook_width - self.image_width) // 2,
            (photobook_height - self.image_height) // 2,
        )


class TwoVertical(object):
    def __init__(self, position, photobook_width, photobook_height):
        self.mode = 1
        self.image_height = 710
        self.image_width = 340
        if position == "left":
            self.position = (
                (photobook_width - self.image_width) // 16,
                (photobook_height - self.image_height) // 2,
            )
        else:
            self.position = (
                (photobook_width - self.image_width) - 25,
                (photobook_height - self.image_height) // 2,
            )


class TwoHorizontal(object):
    def __init__(self, position, photobook_width, photobook_height):
        self.mode = 2
        self.image_height = 340
        self.image_width = 710
        if position == "top":
            self.position = (
                (photobook_width - self.image_width) // 2,
                (photobook_height - self.image_height) // 16,
            )
        else:
            self.position = (
                (photobook_width - self.image_width) // 2,
                (photobook_height - self.image_height) - 25,
            )


class FourSquares(object):
    def __init__(self, position, photobook_width, photobook_height):
        self.mode = 3
        self.image_height = 325
        self.image_width = 325
        if position == "topLeft":
            self.position = (
                (photobook_width - self.image_width) // 16,
                (photobook_height - self.image_height) // 16,
            )
        elif position == "topRight":
            self.position = (
                (photobook_width - self.image_width) - 25,
                (photobook_height - self.image_height) - 405,
            )
        elif position == "bottomRight":
            self.position = (
                (photobook_width - self.image_width) - 25,
                (photobook_height - self.image_height) - 25,
            )
        elif position == "bottomLeft":
            self.position = (
                (photobook_width - self.image_width) // 16,
                (photobook_height - self.image_height) - 25,
            )


class OneVerticalOneSquare(object):
    def __init__(self, position, photobook_width, photobook_height):
        self.mode = 4
        if position == "left":
            self.image_height = 710
            self.image_width = 340
            self.position = (
                (photobook_width - self.image_width) // 16,
                (photobook_height - self.image_height) // 2,
            )
        else:
            self.image_height = 325
            self.image_width = 325
            self.position = (
                (photobook_width - self.image_width) - 25,
                (photobook_height - self.image_height) // 2,
            )


class SingleHorizontal(object):
    def __init__(self, position, photobook_width, photobook_height):
        self.mode = 5
        self.image_height = 500
        self.image_width = 710
        self.position = (
            (photobook_width - self.image_width) // 2,
            (photobook_height - self.image_height) // 2,
        )
