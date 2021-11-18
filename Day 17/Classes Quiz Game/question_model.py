# Class to take in the text and answer from data.py


class Question:
    def __init__(self, q_text, q_answer) -> None:
        self.text = q_text
        self.answer = q_answer
