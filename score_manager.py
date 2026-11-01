
import json
import os


class ScoreManager:

    def __init__(self):

        # Diem hien tai
        self.score = 0

        # Ten file luu ky luc
        self.file_name = "high_score.json"

        # Doc ky luc khi khoi dong
        self.high_score = self.load_high_score()

    # Ham doc ky luc tu file JSON
    def load_high_score(self):

        if os.path.exists(self.file_name):

            try:
                with open(self.file_name, "r") as file:

                    data = json.load(file)

                    return data.get("high_score", 0)

            except (json.JSONDecodeError, OSError):
                return 0

        return 0

    # Ham tang diem
    def increase_score(self):

        self.score += 1

        # Kiem tra ky luc
        if self.score > self.high_score:

            self.high_score = self.score

            self.save_high_score()

    # Ham luu ky luc
    def save_high_score(self):

        data = {
            "high_score": self.high_score
        }

        with open(self.file_name, "w") as file:

            json.dump(data, file, indent=4)

    # Ham dat lai diem
    def reset_score(self):

        self.score = 0
