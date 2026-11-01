
import pygame

class Snake:
    def __init__(self):
        self.body = [(220, 220), (190, 220), (160, 220)]
        self.direction = (30, 0)
        self.cell_size = 30

    def move(self, grow=False):
        head_x, head_y = self.body[0]

        new_head = (
            head_x + self.direction[0],
            head_y + self.direction[1]
        )

        self.body.insert(0, new_head)

        if not grow:
            self.body.pop()

    def draw(self, screen):

        # Ve than ran
        for index, segment in enumerate(self.body):
            x, y = segment

            if index == 0:
                color = (50, 220, 80)
                radius = 10
            else:
                color = (20, 160, 60)
                radius = 9

            pygame.draw.circle(
                screen,
                color,
                (x + 10, y + 10),
                radius
            )

        # Ve mat ran
        head_x, head_y = self.body[0]

        if self.direction == (20, 0):
            eyes = [(head_x + 14, head_y + 5),
                    (head_x + 14, head_y + 14)]

        elif self.direction == (-20, 0):
            eyes = [(head_x + 5, head_y + 5),
                    (head_x + 5, head_y + 14)]

        elif self.direction == (0, -20):
            eyes = [(head_x + 5, head_y + 5),
                    (head_x + 14, head_y + 5)]

        else:
            eyes = [(head_x + 5, head_y + 14),
                    (head_x + 14, head_y + 14)]

        for eye in eyes:
            pygame.draw.circle(
                screen,
                (255, 255, 255),
                eye,
                4
            )

            pygame.draw.circle(
                screen,
                (0, 0, 0),
                eye,
                2
            )
