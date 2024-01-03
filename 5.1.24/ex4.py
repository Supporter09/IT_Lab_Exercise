from Rectangle import Rectangle  # Assuming Rectangle class is defined in Rectangle.py

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, new_side):
        # if new_side <= 0:
        #     raise LengthException("Side must be greater than 0")
        self.width = new_side
        self.height = new_side

    def set_height(self, new_side):
        # if new_side <= 0:
        #     raise LengthException("Side must be greater than 0")
        self.width = new_side
        self.height = new_side