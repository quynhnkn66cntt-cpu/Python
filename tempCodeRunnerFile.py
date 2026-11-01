        high_score_text = self.score_font.render(
            f"HIGH SCORE: {self.score_manager.high_score}",
            True,
            self.WHITE
        )

        self.screen.blit(high_score_text, (280, 65))