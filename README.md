# 🧠 QuizMaster - Python GUI Quiz Game

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue?style=for-the-badge)](https://github.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

**A sleek, responsive, and modern desktop quiz game built entirely in pure Python with Tkinter.**  
*Zero external pip dependencies required — runs out-of-the-box on any computer with Python!*

[Features](#-features) • [Quick Start](#-quick-start) • [How to Play](#-gameplay--controls) • [Architecture](#-project-structure) • [Customization](#-customizing-questions) • [Contributing](#-contributing)

</div>

---

## 🌟 Overview

**QuizMaster** is a standalone desktop trivia application designed to provide an engaging learning and gaming experience. It features a modern dark-mode aesthetic, countdown timer pressure, dynamic score calculation, instant answer feedback with educational trivia facts, and a comprehensive end-game answer review screen.

```
![Quiz Question Screen](Screenshot%202026-10-23%20111634.png)
```

---

## 📸 Screenshots

<div align="center">

| Quiz Question Screen | Results Screen |
|:---:|:---:|
| <img src="screenshots/quiz-question.png" alt="QuizMaster question screen" width="400"> | <img src="screenshots/quiz-results.png" alt="QuizMaster results screen" width="400"> |

</div>

---

## ✨ Features

- **🎨 Modern Dark UI:** Card-based interface with custom-styled progress bar and high-contrast typography.
- **⏱ Question Countdown Timer:** 15-second per-question timer with dynamic visual warnings ($\le 5$s turns red).
- **💡 Instant Feedback & Factoids:** Immediate color cues (Emerald Green for correct, Crimson Red for wrong) plus an educational *"Did you know?"* fact for every question.
- **📊 Real-time Scoring & Accuracy:** Instant score calculation ($+10$ points per correct answer) with a live progress indicator.
- **🏆 Results Screen & Badges:** Calculates percentage accuracy and awards custom achievement titles:
  - 🏆 *Grandmaster Genius* (100%)
  - 🌟 *Trivia Master* ($\ge 80\%$)
  - 👍 *Knowledge Enthusiast* ($\ge 60\%$)
  - 📚 *Keep Practicing* ($\ge 40\%$)
  - 🌱 *Learning Opportunity* ($< 40\%$)
- **📋 Full Review Mode:** Scrollable review view showing every question, your response, and the correct answer.
- **🎲 High Replay Value:** Built-in pool of diverse questions (Science, Tech, Geography, History, Pop Culture), randomly sampling 10 questions each round.
- **📦 Zero External Dependencies:** Built 100% with Python's standard library (`tkinter` & `ttk`).

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.8 or higher** installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/quiz-game.git
cd quiz-game
```

### 2. Run the Game

#### On Windows:
- **Terminal:**
  ```powershell
  python quiz_game.py
  # or
  python main.py
  ```
- **File Explorer:** Double-click [`run.bat`](file:///c:/Users/RAM%20DAS%20MURMU/OneDrive/Desktop/attame/Quiz%20game/run.bat) to launch instantly.

#### On macOS / Linux:
```bash
python3 quiz_game.py
```
*(On Linux distributions like Ubuntu/Debian, ensure Tkinter is installed via `sudo apt install python3-tk`).*

---

## 🎮 Gameplay & Controls

1. **Start Screen:** Click **"Start Quiz Now ➔"** to begin a fresh 10-question round.
2. **Select Answer:** Click any of the 4 choices (`A`, `B`, `C`, or `D`) before the 15-second timer expires.
3. **Learn:** Read the instant feedback and trivia fact.
4. **Advance:** Click **"Next Question ➔"** to progress.
5. **Results & Review:**
   - View your score, accuracy rate, and achievement badge.
   - Click **"Review Answers 📋"** to inspect mistakes.
   - Click **"Play Again 🔄"** for a new randomized set of questions.

---

## 📁 Project Structure

```text
Quiz game/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI matrix test runner
├── tests/
│   ├── __init__.py
│   └── test_quiz.py             # Automated unit tests (schema & logic)
├── .gitignore                   # Standard Python gitignore
├── CONTRIBUTING.md              # Contributor guidelines
├── LICENSE                      # MIT Open Source License
├── README.md                    # Project documentation
├── main.py                      # Application entry point
├── quiz_game.py                 # Core GUI application and question bank
├── requirements.txt             # Dependency specification
├── requirements-dev.txt         # Dev & test dependencies
└── run.bat                      # Windows double-click launcher
```

---

## ✏️ Customizing Questions

Adding or editing questions is straightforward! Open [`quiz_game.py`](file:///c:/Users/RAM%20DAS%20MURMU/OneDrive/Desktop/attame/Quiz%20game/quiz_game.py) and modify `QUESTIONS_POOL`:

```python
{
    "question": "What is the smallest unit of matter?",
    "options": ["Molecule", "Atom", "Electron", "Quark"],
    "answer": 1,  # 0-indexed: 0=Molecule, 1=Atom, 2=Electron, 3=Quark
    "category": "Physics",
    "fact": "Atoms consist of a nucleus surrounded by one or more electrons."
}
```

---

## 🧪 Running Automated Tests

The test suite validates question schema integrity, answer index bounds, and game state transitions:

```bash
# Using standard Python unittest (no extra packages needed):
python -m unittest discover -s tests -p "test_*.py"

# Or using pytest (if installed):
pytest tests/
```

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) to learn how to propose bug fixes, UI improvements, and new trivia questions.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
