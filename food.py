
import pygame
import random


class Food:
    def __init__(self):
        self.cell_size = 30

        self.board_x = 40
        self.board_y = 100
        self.board_width = 720
        self.board_height = 450

        self.position = (300, 200)
        self.food_type = "apple"

        self.generate([])

    def generate(self, snake_body):

        while True:
            x = self.board_x + random.randrange(
                self.board_width // self.cell_size
            ) * self.cell_size

            y = self.board_y + random.randrange(
                self.board_height // self.cell_size
            ) * self.cell_size

            if (x, y) not in snake_body:
                self.position = (x, y)
                break

        # Chon ngau nhien loai thuc an
        self.food_type = random.choice([
            "apple", "orange", "strawberry",
            "grape", "heart"
        ])

    def draw(self, screen):

        x, y = self.position

        # Tao tam de ve thuc an
        center_x = x + 15
        center_y = y + 15

        if self.food_type == "apple":

            # Tao
            pygame.draw.circle(
                screen, (230, 40, 50),
                (center_x, center_y + 1), 8
            )

            # Cuong tao
            pygame.draw.line(
                screen, (100, 60, 20),
                (center_x, center_y - 6),
                (center_x + 2, center_y - 10), 2
            )

            # La
            pygame.draw.ellipse(
                screen, (50, 200, 80),
                (center_x + 1, center_y - 10, 7, 4)
            )

        elif self.food_type == "orange":

            # Qua cam
            pygame.draw.circle(
                screen, (255, 150, 20),
                (center_x, center_y), 8
            )

            # La cam
            pygame.draw.ellipse(
                screen, (40, 180, 60),
                (center_x - 2, center_y - 10, 7, 4)
            )

            # Anh sang
            pygame.draw.circle(
                screen, (255, 220, 120),
                (center_x - 3, center_y - 3), 2
            )

        elif self.food_type == "strawberry":

            # Dau tay
            pygame.draw.polygon(
                screen, (240, 40, 90),
                [
                    (center_x - 8, center_y - 3),
                    (center_x + 8, center_y - 3),
                    (center_x, center_y + 9)
                ]
            )

            # La dau
            pygame.draw.polygon(
                screen, (40, 190, 70),
                [
                    (center_x - 6, center_y - 5),
                    (center_x, center_y - 10),
                    (center_x + 6, center_y - 5)
                ]
            )

            # Hat dau
            pygame.draw.circle(
                screen, (255, 230, 100),
                (center_x - 2, center_y), 1
            )

            pygame.draw.circle(
                screen, (255, 230, 100),
                (center_x + 2, center_y + 3), 1
            )

        elif self.food_type == "grape":

            # Chum nho
            for dx, dy in [
                (-4, -3), (4, -3),
                (-7, 3), (0, 3), (7, 3),
                (0, 8)
            ]:
                pygame.draw.circle(
                    screen, (145, 60, 210),
                    (center_x + dx, center_y + dy), 4
                )

            # La nho
            pygame.draw.ellipse(
                screen, (50, 190, 70),
                (center_x - 3, center_y - 10, 8, 4)
            )

        elif self.food_type == "heart":

            # Trai tim xanh bien
            pygame.draw.circle(
                screen, (30, 190, 255),
                (center_x - 4, center_y - 3), 5
            )

            pygame.draw.circle(
                screen, (30, 190, 255),
                (center_x + 4, center_y - 3), 5
            )

            pygame.draw.polygon(
                screen, (30, 190, 255),
                [
                    (center_x - 9, center_y - 1),
                    (center_x + 9, center_y - 1),
                    (center_x, center_y + 10)
                ]
            )

            # Anh sang trai tim
            pygame.draw.circle(
                screen, (180, 240, 255),
                (center_x - 4, center_y - 4), 2
            )
