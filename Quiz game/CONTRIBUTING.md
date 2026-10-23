# Contributing to QuizMaster

Thank you for your interest in improving **QuizMaster**! Contributions from the community are warmly welcomed.

---

## 🛠 How You Can Contribute

- **Add New Questions:** Expand the question bank across various topics and categories.
- **UI & UX Enhancements:** Propose cleaner visuals, accessibility improvements, or animations.
- **Bug Fixes:** Fix UI glitches, timer issues, or logic edge cases.
- **Translations / Localization:** Help add multilingual support.

---

## 🚀 Getting Started

1. **Fork the Repository:** Click the "Fork" button on GitHub.
2. **Clone your fork:**
   ```bash
   git clone https://github.com/<your-username>/quiz-game.git
   cd quiz-game
   ```
3. **Create a new branch:**
   ```bash
   git checkout -b feature/add-new-questions
   ```
4. **Make your changes:**
   - Follow PEP 8 style conventions.
   - If adding questions to `quiz_game.py`, ensure each question conforms to:
     ```python
     {
         "question": "What is ...?",
         "options": ["A", "B", "C", "D"],
         "answer": 0,  # 0-indexed integer (0=A, 1=B, 2=C, 3=D)
         "category": "Category Name",
         "fact": "Interesting fact or explanation."
     }
     ```
5. **Run tests:**
   ```bash
   python -m unittest discover -s tests -p "test_*.py"
   ```
6. **Commit & Push:**
   ```bash
   git commit -m "feat(questions): add 5 new astronomy questions"
   git push origin feature/add-new-questions
   ```
7. **Open a Pull Request:** Describe your changes clearly in your PR.

---

## 📜 Code of Conduct

Please be respectful, kind, and collaborative in all discussions and pull requests.
