class Snake:
    def __init__(self, length, color):
        self.length = length
        self.color = color

    def display_info(self):
        print("Chiều dài:", self.length)
        print("Màu sắc:", self.color)


snake1 = Snake(3, "green")
snake2 = Snake(5, "red")

snake1.display_info()
snake2.display_info()