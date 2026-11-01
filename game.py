
import pygame

from snake import Snake
from food import Food
from score_manager import ScoreManager


class Game:

    def __init__(self):

        # Khoi tao cua so
        self.width = 800
        self.height = 600

        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        # Mau sac
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 200, 0)
        self.GRAY = (50, 50, 50)
        self.RED = (255, 0, 0)
        self.BLUE = (40, 100, 220)

        # Khu vuc choi
        self.board_x = 40
        self.board_y = 100
        self.board_width = 720
        self.board_height = 450
        self.cell_size = 30

        # Tao cac doi tuong
        self.snake = Snake()
        self.food = Food()
        self.score_manager = ScoreManager()

        self.food.generate(self.snake.body)

        # Trang thai game
        self.game_over = False
        self.running = True
        self.start_menu = True
        self.paused = False

        # Toc do
        self.game_speed = 7

        # Font chu
        self.title_font = pygame.font.Font(None, 50)
        self.score_font = pygame.font.Font(None, 35)
        self.game_font = pygame.font.Font(None, 65)
        self.button_font = pygame.font.Font(None, 40)
        self.speed_font = pygame.font.Font(None, 30)

        # Nut bat dau
        self.start_button = pygame.Rect(
            300, 350, 200, 65
        )

        # Nut choi lai
        self.restart_button = pygame.Rect(
            300, 320, 200, 65
        )
                # Nut tam dung
        self.pause_button = pygame.Rect(
            650, 20, 120, 40
        )

        # Nut tiep tuc
        self.resume_button = pygame.Rect(
            300, 320, 200, 60
        )
                # Nut quay ve Menu
        self.menu_button = pygame.Rect(
            300, 400, 200, 60
        )
       # =================================
    # XU LY SU KIEN
    # =================================

    def handle_events(self):

        for event in pygame.event.get():

            # Thoat game
            if event.type == pygame.QUIT:
                self.running = False

            # Xu ly ban phim
            if event.type == pygame.KEYDOWN:

                # Chi dieu khien khi dang choi
                if not self.game_over and not self.start_menu:

                    # Nhan P de tam dung hoac tiep tuc
                    if event.key == pygame.K_p:
                        self.paused = not self.paused

                    # Dieu khien ran khi khong tam dung
                    elif not self.paused:

                        direction = self.snake.direction

                        if event.key == pygame.K_RIGHT and self.snake.direction != (-30, 0):
                            self.snake.direction = (30, 0)

                        elif event.key == pygame.K_LEFT and self.snake.direction != (30, 0):
                            self.snake.direction = (-30, 0)

                        elif event.key == pygame.K_UP and self.snake.direction != (0, 30):
                            self.snake.direction = (0, -30)

                        elif event.key == pygame.K_DOWN and self.snake.direction != (0, -30):
                            self.snake.direction = (0, 30)

            # Xu ly nhan chuot
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                # Neu dang o Menu
                if self.start_menu:

                    if self.start_button.collidepoint(event.pos):
                        self.start_menu = False

                # Neu Game Over
                elif self.game_over:

                    if self.restart_button.collidepoint(event.pos):
                        self.reset_game()

                # Neu dang tam dung
                elif self.paused:

                    # Nhan nut TIEP TUC
                    if self.resume_button.collidepoint(event.pos):
                        self.paused = False

                    # Nhan nut QUAY VE MENU
                    elif self.menu_button.collidepoint(event.pos):
                        self.start_menu = True
                        self.paused = False
                        self.reset_game()

                # Neu dang choi
                else:

                    if self.pause_button.collidepoint(event.pos):
                        self.paused = True
    
    # =================================
    # CAP NHAT TRANG THAI GAME
    # =================================

    def update(self):

        # Khong cap nhat khi Game Over, o Menu hoac tam dung
        if self.game_over or self.start_menu or self.paused:
            return

        # Tinh vi tri dau moi
        head_x, head_y = self.snake.body[0]

        new_head = (
            head_x + self.snake.direction[0],
            head_y + self.snake.direction[1]
        )

        # Kiem tra co an thuc an khong
        grow = new_head == self.food.position

        # Di chuyen ran
        self.snake.move(grow)

        # Neu an thuc an
        if grow:

            self.score_manager.increase_score()

            self.food.generate(self.snake.body)

            # Tang toc do theo diem
            self.game_speed = min(
                10 + self.score_manager.score // 3,
                20
            )

        # Kiem tra va cham voi tuong
        head_x, head_y = self.snake.body[0]

        if (
            head_x < self.board_x
            or head_x >= self.board_x + self.board_width
            or head_y < self.board_y
            or head_y >= self.board_y + self.board_height
        ):

            self.game_over = True

        # Kiem tra va cham voi than
        if self.snake.body[0] in self.snake.body[1:]:

            self.game_over = True

    # =================================
    # VE KHU VUC CHOI
    # =================================

    def draw_board(self):

        pygame.draw.rect(
            self.screen,
            self.WHITE,
            (
                self.board_x,
                self.board_y,
                self.board_width,
                self.board_height
            ),
            2
        )

        # Ve luoi doc
        for x in range(
            self.board_x,
            self.board_x + self.board_width,
            self.cell_size
        ):

            pygame.draw.line(
                self.screen,
                self.GRAY,
                (x, self.board_y),
                (x, self.board_y + self.board_height)
            )

        # Ve luoi ngang
        for y in range(
            self.board_y,
            self.board_y + self.board_height,
            self.cell_size
        ):

            pygame.draw.line(
                self.screen,
                self.GRAY,
                (self.board_x, y),
                (self.board_x + self.board_width, y)
            )

    # =================================
    # VE BANG GAME OVER
    # =================================

    def draw_game_over(self):

        # Lop nen toi
        overlay = pygame.Surface(
            (self.width, self.height)
        )

        overlay.set_alpha(180)
        overlay.fill(self.BLACK)

        self.screen.blit(overlay, (0, 0))

        # Khung thong bao
        panel_rect = pygame.Rect(
            200, 170, 400, 260
        )

        pygame.draw.rect(
            self.screen,
            self.WHITE,
            panel_rect,
            border_radius=15
        )

        pygame.draw.rect(
            self.screen,
            (35, 35, 35),
            panel_rect.inflate(-6, -6),
            border_radius=12
        )

        # Chu GAME OVER
        game_text = self.game_font.render(
            "GAME OVER",
            True,
            self.RED
        )

        game_rect = game_text.get_rect(
            center=(self.width // 2, 220)
        )

        self.screen.blit(game_text, game_rect)

        # Diem cuoi cung
        final_score = self.score_font.render(
            f"YOUR SCORE: {self.score_manager.score}",
            True,
            self.WHITE
        )

        final_rect = final_score.get_rect(
            center=(self.width // 2, 275)
        )

        self.screen.blit(final_score, final_rect)

        # Nut CHOI LAI
        pygame.draw.rect(
            self.screen,
            self.BLUE,
            self.restart_button,
            border_radius=12
        )

        button_text = self.button_font.render(
            "CHOI LAI",
            True,
            self.WHITE
        )

        button_rect = button_text.get_rect(
            center=self.restart_button.center
        )

        self.screen.blit(button_text, button_rect)
    #
    
    def draw_menu(self):

        # Mau nen
        self.screen.fill((12, 25, 35))

        # Ve cac cham trang tri
        for x in range(30, self.width, 50):
            for y in range(30, self.height, 50):
                pygame.draw.circle(
                    self.screen,
                    (25, 45, 55),
                    (x, y),
                    2
                )

        # Khung tieu de
        title_box = pygame.Rect(150, 100, 500, 100)

        pygame.draw.rect(
            self.screen,
            (20, 45, 55),
            title_box,
            border_radius=20
        )

        pygame.draw.rect(
            self.screen,
            (40, 220, 130),
            title_box,
            width=3,
            border_radius=20
        )

        # Tieu de
        title = self.title_font.render(
            "SNAKE GAME",
            True,
            (70, 255, 150)
        )

        title_rect = title.get_rect(
            center=(self.width // 2, 150)
        )

        self.screen.blit(title, title_rect)

        # Dong mo ta
        subtitle = self.score_font.render(
            "WELCOME TO THE SNAKE WORLD",
            True,
            (180, 210, 210)
        )

        subtitle_rect = subtitle.get_rect(
            center=(self.width // 2, 240)
        )

        self.screen.blit(subtitle, subtitle_rect)

        # Ve hinh con ran trang tri
        for i in range(5):
            pygame.draw.circle(
                self.screen,
                (40, 220 - i * 15, 120),
                (320 + i * 35, 300),
                14
            )

        # Dau ran
        pygame.draw.circle(
            self.screen,
            (100, 255, 130),
            (495, 300),
            17
        )

        # Mat ran
        pygame.draw.circle(
            self.screen,
            (255, 255, 255),
            (500, 294),
            4
        )

        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            (501, 294),
            2
        )

        # Bang diem cao
        score_box = pygame.Rect(230, 355, 340, 60)

        pygame.draw.rect(
            self.screen,
            (25, 55, 65),
            score_box,
            border_radius=15
        )

        pygame.draw.rect(
            self.screen,
            (50, 180, 150),
            score_box,
            width=2,
            border_radius=15
        )

        high_score_text = self.score_font.render(
            f"HIGH SCORE: {self.score_manager.high_score}",
            True,
            (255, 220, 90)
        )

        high_score_rect = high_score_text.get_rect(
            center=score_box.center
        )

        self.screen.blit(high_score_text, high_score_rect)

        # Nut bat dau
        pygame.draw.rect(
            self.screen,
            (30, 190, 100),
            self.start_button,
            border_radius=18
        )

        pygame.draw.rect(
            self.screen,
            (100, 255, 160),
            self.start_button,
            width=3,
            border_radius=18
        )

        button_text = self.button_font.render(
            "PLAY GAME",
            True,
            (255, 255, 255)
        )

        button_rect = button_text.get_rect(
            center=self.start_button.center
        )

        self.screen.blit(button_text, button_rect)

        # Huong dan
        guide = self.score_font.render(
            "USE ARROW KEYS TO MOVE",
            True,
            (140, 170, 180)
        )

        guide_rect = guide.get_rect(
            center=(self.width // 2, 500)
        )

        self.screen.blit(guide, guide_rect)

        pygame.display.update()

    # =================================
    # VE GIAO DIEN GAME
    # =================================

    def draw(self):
        if self.start_menu:
            self.draw_menu()
            return
        self.screen.fill(self.BLACK)

        # Tieu de
        title = self.title_font.render(
            "SNAKE GAME",
            True,
            self.GREEN
        )

        self.screen.blit(title, (280, 30))

        # Diem
        score_text = self.score_font.render(
            f"SCORE: {self.score_manager.score}",
            True,
            self.WHITE
        )

        self.screen.blit(score_text, (40, 65))
        # Diem cao nhat
        high_score_text = self.score_font.render(
            f"HIGH SCORE: {self.score_manager.high_score}",
            True,
            self.WHITE
        )

        self.screen.blit(high_score_text, (280, 65))
        # Toc do
        speed_text = self.speed_font.render(
            f"SPEED: {self.game_speed}",
            True,
            self.WHITE
        )

        self.screen.blit(speed_text, (600, 70))

        
        # Ve cac doi tuong
        self.draw_board()
        self.snake.draw(self.screen)
        self.food.draw(self.screen)

        # Neu dang choi: hien thi nut TAM DUNG
        if not self.paused and not self.game_over:

            pygame.draw.rect(
                self.screen,
                self.BLUE,
                self.pause_button,
                border_radius=8
            )

            pause_text = self.button_font.render(
                "TAM DUNG",
                True,
                self.WHITE
            )

            pause_rect = pause_text.get_rect(
                center=self.pause_button.center
            )

            self.screen.blit(pause_text, pause_rect)
             
        # Neu dang tam dung: hien thi nut TIEP TUC
        if self.paused:

            # Lop nen toi
            overlay = pygame.Surface(
                (self.width, self.height)
            )

            overlay.set_alpha(150)
            overlay.fill(self.BLACK)

            self.screen.blit(overlay, (0, 0))

            # Chu TAM DUNG
            paused_text = self.game_font.render(
                "TAM DUNG",
                True,
                self.WHITE
            )

            paused_rect = paused_text.get_rect(
                center=(self.width // 2, 220)
            )

            self.screen.blit(paused_text, paused_rect)

            # Nut TIEP TUC
            pygame.draw.rect(
                self.screen,
                self.GREEN,
                self.resume_button,
                border_radius=10
            )

            resume_text = self.button_font.render(
                "TIEP TUC",
                True,
                self.WHITE
            )

            resume_rect = resume_text.get_rect(
                center=self.resume_button.center
            )

            self.screen.blit(resume_text, resume_rect)
                                    # Nut QUAY VE MENU
            pygame.draw.rect(
                self.screen,
                self.BLUE,
                self.menu_button,
                border_radius=10
            )

            menu_text = self.button_font.render(
                "VE MENU",
                True,
                self.WHITE
            )

            menu_rect = menu_text.get_rect(
                center=self.menu_button.center
            )

            self.screen.blit(menu_text, menu_rect)


        # Hien thi GAME OVER
        if self.game_over:

            self.draw_game_over()

        pygame.display.update()

    # =================================
    # KHOI DONG LAI GAME
    # =================================

    def reset_game(self):

        self.snake = Snake()

        self.food = Food()
        self.food.generate(self.snake.body)

        self.score_manager.reset_score()

        self.game_speed = 10

        self.game_over = False
        self.paused = False
    # =================================
    # VONG LAP CHINH
    # =================================

    def run(self):

        while self.running:

            self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(self.game_speed)
