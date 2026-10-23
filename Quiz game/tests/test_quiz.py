"""
Unit tests for QuizMaster
Compatible with both standard unittest and pytest.
"""
import unittest
import tkinter as tk
from quiz_game import QUESTIONS_POOL, QuizGameApp


class TestQuestionBank(unittest.TestCase):
    """Validate data integrity of the question bank."""

    def test_pool_is_not_empty(self):
        self.assertGreaterEqual(
            len(QUESTIONS_POOL), 10, "Question pool should have at least 10 questions"
        )

    def test_question_schema(self):
        required_keys = {"question", "options", "answer", "category", "fact"}
        for idx, q in enumerate(QUESTIONS_POOL):
            missing = required_keys - set(q.keys())
            self.assertFalse(missing, f"Question at index {idx} is missing keys: {missing}")

    def test_valid_options_and_answer(self):
        for idx, q in enumerate(QUESTIONS_POOL):
            options = q["options"]
            self.assertIsInstance(options, list, f"Options in question {idx} must be a list")
            self.assertEqual(len(options), 4, f"Question {idx} should have exactly 4 options")
            self.assertEqual(len(set(options)), 4, f"Question {idx} contains duplicate options")

            ans = q["answer"]
            self.assertIsInstance(ans, int, f"Answer index in question {idx} must be an integer")
            self.assertTrue(0 <= ans < len(options), f"Answer index {ans} out of range in question {idx}")

    def test_non_empty_strings(self):
        for idx, q in enumerate(QUESTIONS_POOL):
            self.assertTrue(q["question"].strip(), f"Question {idx} has an empty question string")
            self.assertTrue(q["category"].strip(), f"Question {idx} has an empty category")
            self.assertTrue(q["fact"].strip(), f"Question {idx} has an empty fact string")


class TestQuizLogic(unittest.TestCase):
    """Test the core game flow and state transitions."""

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # keep window hidden during headless tests
        self.app = QuizGameApp(self.root)

    def tearDown(self):
        if self.app.timer_job:
            self.root.after_cancel(self.app.timer_job)
        self.root.destroy()

    def test_initial_state(self):
        self.assertEqual(self.app.score, 0)
        self.assertEqual(self.app.total_questions_per_round, 10)
        self.assertEqual(len(self.app.questions), 0)

    def test_game_round_flow(self):
        # Start game
        self.app.start_new_game()
        self.assertEqual(len(self.app.questions), 10)
        self.assertEqual(self.app.current_idx, 0)

        # Answer first question correctly
        correct_idx = self.app.questions[0]["answer"]
        self.app.handle_answer(correct_idx)
        self.assertEqual(self.app.score, 10)
        self.assertEqual(len(self.app.user_history), 1)
        self.assertTrue(self.app.user_history[0]["is_correct"])

        # Advance to question 2
        self.app.next_question()
        self.assertEqual(self.app.current_idx, 1)

        # Answer second question incorrectly
        wrong_idx = (self.app.questions[1]["answer"] + 1) % 4
        self.app.handle_answer(wrong_idx)
        self.assertEqual(self.app.score, 10)  # score shouldn't increase
        self.assertEqual(len(self.app.user_history), 2)
        self.assertFalse(self.app.user_history[1]["is_correct"])

        # Test timeout scenario (-1 index)
        self.app.next_question()
        self.assertEqual(self.app.current_idx, 2)
        self.app.handle_answer(-1)
        self.assertEqual(self.app.score, 10)
        self.assertFalse(self.app.user_history[2]["is_correct"])
        self.assertEqual(self.app.user_history[2]["selected"], "Timed Out")


if __name__ == "__main__":
    unittest.main()
