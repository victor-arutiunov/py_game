
class Character():
    """Class for creating characters with basic paramenters"""

    def __init__(self, x: int, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed


me = Character('rgg', 50, 50, 50, 'fef')

print(me.x)
