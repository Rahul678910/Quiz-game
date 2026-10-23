"""
QuizMaster - A Modern, Interactive Python GUI Quiz Game
Built with Tkinter (Python standard library, no extra installation required)
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random

# Question bank containing 20 diverse, interesting questions
QUESTIONS_POOL = [
    {
        "question": "Which programming language was created by Guido van Rossum in 1991?",
        "options": ["Java", "Python", "C++", "Ruby"],
        "answer": 1,
        "category": "Technology",
        "fact": "Python was named after the British comedy troupe 'Monty Python', not the snake!"
    },
    {
        "question": "What is the capital city of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "answer": 2,
        "category": "Geography",
        "fact": "Canberra was chosen as a compromise between rival cities Sydney and Melbourne in 1908."
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["Ag", "Au", "Fe", "Gd"],
        "answer": 1,
        "category": "Science",
        "fact": "The symbol 'Au' comes from the Latin word 'aurum', meaning 'shining dawn'."
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Venus", "Jupiter", "Mars", "Saturn"],
        "answer": 2,
        "category": "Astronomy",
        "fact": "Mars appears red due to iron oxide (rust) on its surface."
    },
    {
        "question": "How many bits make up one byte?",
        "options": ["4", "8", "16", "32"],
        "answer": 1,
        "category": "Technology",
        "fact": "A 4-bit unit is also known colloquially as a 'nibble'."
    },
    {
        "question": "Which organ in the human body consumes the most energy (~20%)?",
        "options": ["Heart", "Liver", "Brain", "Lungs"],
        "answer": 2,
        "category": "Biology",
        "fact": "Even though it weighs about 2% of total body mass, the brain consumes 20% of resting energy."
    },
    {
        "question": "Who painted the famous masterpiece 'The Starry Night'?",
        "options": ["Pablo Picasso", "Vincent van Gogh", "Claude Monet", "Leonardo da Vinci"],
        "answer": 1,
        "category": "Art",
        "fact": "Van Gogh painted 'The Starry Night' in June 1889 while staying at Saint-Paul asylum."
    },
    {
        "question": "What is the fastest land animal in the world?",
        "options": ["Lion", "Cheetah", "Gazelle", "Pronghorn"],
        "answer": 1,
        "category": "Nature",
        "fact": "Cheetahs can accelerate from 0 to 60 mph (97 km/h) in under 3 seconds."
    },
    {
        "question": "Which ocean is the largest and deepest on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": 3,
        "category": "Geography",
        "fact": "The Pacific Ocean covers over 30% of the Earth's surface, larger than all land masses combined."
    },
    {
        "question": "In what year did the Apollo 11 mission land humans on the Moon?",
        "options": ["1965", "1969", "1972", "1961"],
        "answer": 1,
        "category": "History",
        "fact": "Neil Armstrong stepped onto the lunar surface on July 20, 1969."
    },
    {
        "question": "Which data structure uses LIFO (Last In, First Out) ordering?",
        "options": ["Queue", "Stack", "Array", "Linked List"],
        "answer": 1,
        "category": "Computer Science",
        "fact": "Call stacks in program execution operate on this exact LIFO principle."
    },
    {
        "question": "What is the hardest naturally occurring substance known on Earth?",
        "options": ["Titanium", "Graphene", "Diamond", "Quartz"],
        "answer": 2,
        "category": "Science",
        "fact": "Diamonds are made of pure carbon atoms arranged in a rigid diamond cubic crystal lattice."
    },
    {
        "question": "Which country produces the most coffee beans globally?",
        "options": ["Colombia", "Vietnam", "Ethiopia", "Brazil"],
        "answer": 3,
        "category": "Geography",
        "fact": "Brazil has been the world's largest producer of coffee for over 150 years."
    },
    {
        "question": "What does 'HTTP' stand for in web addresses?",
        "options": [
            "HyperText Transfer Protocol",
            "High Tech Transmission Path",
            "HyperText Tracking Program",
            "Hyper Tool Testing Platform"
        ],
        "answer": 0,
        "category": "Technology",
        "fact": "Tim Berners-Lee initiated HTTP alongside HTML and URLs at CERN in 1989."
    },
    {
        "question": "Which gas do plants primarily absorb during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": 2,
        "category": "Science",
        "fact": "Plants convert carbon dioxide and water into glucose and oxygen using sunlight."
    },
    {
        "question": "Who is credited with discovering penicillin in 1928?",
        "options": ["Louis Pasteur", "Alexander Fleming", "Marie Curie", "Robert Koch"],
        "answer": 1,
        "category": "Medicine",
        "fact": "Fleming discovered it accidentally after noticing mold contaminated one of his petri dishes."
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": 2,
        "category": "Geography",
        "fact": "The seven continents are Asia, Africa, North America, South America, Antarctica, Europe, and Australia."
    },
    {
        "question": "Which animal is the largest mammal ever known to have lived?",
        "options": ["African Elephant", "Blue Whale", "Megalodon", "Colossal Squid"],
        "answer": 1,
        "category": "Nature",
        "fact": "A blue whale can reach lengths of 100 feet (30m) and weigh up to 200 tons."
    },
    {
        "question": "In computer networking, what does 'DNS' stand for?",
        "options": [
            "Data Network System",
            "Domain Name System",
            "Digital Numbering Standard",
            "Dynamic Network Service"
        ],
        "answer": 1,
        "category": "Technology",
        "fact": "DNS acts as the phonebook of the internet, translating domain names into IP addresses."
    },
    {
        "question": "What is the speed of light in vacuum (approximate)?",
        "options": ["300,000 km/s", "150,000 km/s", "1,000,000 km/s", "30,000 km/s"],
        "answer": 0,
        "category": "Physics",
        "fact": "The exact speed of light is 299,792,458 meters per second."
    }
]


class QuizGameApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("QuizMaster - Interactive GUI Game")
        self.root.geometry("760x620")
        self.root.minsize(700, 560)
        self.root.configure(bg="#121826")

        # Color Palette
        self.BG_DARK = "#121826"
        self.CARD_BG = "#1f293d"
        self.CARD_INNER = "#28354f"
        self.ACCENT = "#4f46e5"
        self.ACCENT_HOVER = "#6366f1"
        self.TEXT_PRIMARY = "#f8fafc"
        self.TEXT_MUTED = "#94a3b8"
        self.CORRECT_COLOR = "#10b981"
        self.WRONG_COLOR = "#ef4444"
        self.TIMER_COLOR = "#f59e0b"
        self.TIMER_WARN = "#ef4444"

        # Game state
        self.total_questions_per_round = 10
        self.time_per_question = 15  # seconds
        self.questions = []
        self.current_idx = 0
        self.score = 0
        self.time_left = self.time_per_question
        self.timer_job = None
        self.selected_answered = False
        self.user_history = []  # records (question, selected, correct, fact)

        # Main Container
        self.container = tk.Frame(self.root, bg=self.BG_DARK)
        self.container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Center on screen
        self.center_window()

        # Show welcome screen
        self.show_welcome_screen()

    def center_window(self):
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2) - 20
        self.root.geometry(f"+{x}+{y}")

    def clear_container(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None
        for widget in self.container.winfo_children():
            widget.destroy()

    # ==========================
    # 1. WELCOME SCREEN
    # ==========================
    def show_welcome_screen(self):
        self.clear_container()

        card = tk.Frame(self.container, bg=self.CARD_BG, bd=0, relief=tk.FLAT)
        card.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        # Header badge
        badge = tk.Label(
            card,
            text="★ KNOWLEDGE CHALLENGE ★",
            font=("Helvetica", 10, "bold"),
            bg="#2e3856",
            fg="#a5b4fc",
            padx=14,
            pady=4
        )
        badge.pack(pady=(40, 10))

        # Title
        title = tk.Label(
            card,
            text="QuizMaster",
            font=("Helvetica", 32, "bold"),
            bg=self.CARD_BG,
            fg=self.TEXT_PRIMARY
        )
        title.pack(pady=(0, 6))

        subtitle = tk.Label(
            card,
            text="Test your knowledge across Science, Technology, Geography, History & more!",
            font=("Helvetica", 12),
            bg=self.CARD_BG,
            fg=self.TEXT_MUTED
        )
        subtitle.pack(pady=(0, 30))

        # Rules Box
        rules_frame = tk.Frame(card, bg=self.CARD_INNER, padx=24, pady=20)
        rules_frame.pack(fill=tk.X, padx=50, pady=(0, 30))

        rules_title = tk.Label(
            rules_frame,
            text="Game Rules & Features",
            font=("Helvetica", 12, "bold"),
            bg=self.CARD_INNER,
            fg=self.TEXT_PRIMARY
        )
        rules_title.pack(anchor="w", pady=(0, 10))

        rules = [
            f"•  {self.total_questions_per_round} randomized questions per game.",
            f"•  {self.time_per_question} seconds countdown per question.",
            "•  +10 points for each correct answer.",
            "•  Learn interesting facts after answering each question.",
            "•  Instant color feedback (Green = Correct, Red = Incorrect)."
        ]
        for rule in rules:
            r_lbl = tk.Label(
                rules_frame,
                text=rule,
                font=("Helvetica", 10),
                bg=self.CARD_INNER,
                fg="#cbd5e1",
                anchor="w"
            )
            r_lbl.pack(fill=tk.X, pady=2)

        # Buttons Frame
        btn_frame = tk.Frame(card, bg=self.CARD_BG)
        btn_frame.pack(pady=10)

        start_btn = tk.Button(
            btn_frame,
            text="Start Quiz Now  ➔",
            font=("Helvetica", 13, "bold"),
            bg=self.ACCENT,
            fg="#ffffff",
            activebackground=self.ACCENT_HOVER,
            activeforeground="#ffffff",
            bd=0,
            padx=32,
            pady=12,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.start_new_game
        )
        start_btn.pack(side=tk.LEFT, padx=10)

        quit_btn = tk.Button(
            btn_frame,
            text="Exit",
            font=("Helvetica", 12),
            bg="#334155",
            fg="#94a3b8",
            activebackground="#475569",
            activeforeground="#ffffff",
            bd=0,
            padx=20,
            pady=12,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.root.destroy
        )
        quit_btn.pack(side=tk.LEFT, padx=10)

    # ==========================
    # 2. START / ROUND SETUP
    # ==========================
    def start_new_game(self):
        # Pick random questions from pool
        self.questions = random.sample(
            QUESTIONS_POOL,
            min(self.total_questions_per_round, len(QUESTIONS_POOL))
        )
        self.current_idx = 0
        self.score = 0
        self.user_history = []
        self.show_question()

    # ==========================
    # 3. QUIZ INTERFACE
    # ==========================
    def show_question(self):
        self.clear_container()
        self.selected_answered = False
        self.time_left = self.time_per_question

        q_data = self.questions[self.current_idx]

        # Top Bar: Progress, Category & Score
        top_bar = tk.Frame(self.container, bg=self.BG_DARK)
        top_bar.pack(fill=tk.X, pady=(0, 10))

        # Question counter
        progress_text = f"Question {self.current_idx + 1} of {len(self.questions)}"
        self.counter_lbl = tk.Label(
            top_bar,
            text=progress_text,
            font=("Helvetica", 11, "bold"),
            bg=self.BG_DARK,
            fg="#a5b4fc"
        )
        self.counter_lbl.pack(side=tk.LEFT)

        # Category pill
        category_lbl = tk.Label(
            top_bar,
            text=q_data.get("category", "General"),
            font=("Helvetica", 9, "bold"),
            bg="#312e81",
            fg="#c7d2fe",
            padx=10,
            pady=2
        )
        category_lbl.pack(side=tk.LEFT, padx=15)

        # Score display
        self.score_lbl = tk.Label(
            top_bar,
            text=f"Score: {self.score}",
            font=("Helvetica", 12, "bold"),
            bg=self.BG_DARK,
            fg="#38bdf8"
        )
        self.score_lbl.pack(side=tk.RIGHT)

        # Timer Badge
        self.timer_lbl = tk.Label(
            top_bar,
            text=f"⏱ {self.time_left}s",
            font=("Helvetica", 11, "bold"),
            bg="#27272a",
            fg=self.TIMER_COLOR,
            padx=10,
            pady=2
        )
        self.timer_lbl.pack(side=tk.RIGHT, padx=12)

        # Progress Bar Frame (Canvas for smooth custom styling)
        self.progress_canvas = tk.Canvas(
            self.container,
            height=6,
            bg="#1e293b",
            highlightthickness=0
        )
        self.progress_canvas.pack(fill=tk.X, pady=(0, 15))
        pct = (self.current_idx) / len(self.questions)
        self.root.update_idletasks()
        cw = self.container.winfo_width()
        self.progress_canvas.create_rectangle(
            0, 0, int(cw * pct), 6, fill=self.ACCENT, outline=""
        )

        # Main Question Card
        card = tk.Frame(self.container, bg=self.CARD_BG, padx=28, pady=22)
        card.pack(fill=tk.BOTH, expand=True)

        # Question text
        q_label = tk.Label(
            card,
            text=q_data["question"],
            font=("Helvetica", 15, "bold"),
            bg=self.CARD_BG,
            fg=self.TEXT_PRIMARY,
            wraplength=640,
            justify=tk.LEFT
        )
        q_label.pack(anchor="w", pady=(0, 20))

        # Options Container
        self.option_buttons = []
        options_frame = tk.Frame(card, bg=self.CARD_BG)
        options_frame.pack(fill=tk.BOTH, expand=True)

        prefixes = ["A", "B", "C", "D"]
        for i, option_text in enumerate(q_data["options"]):
            btn_text = f"  {prefixes[i]}.  {option_text}"
            btn = tk.Button(
                options_frame,
                text=btn_text,
                font=("Helvetica", 11),
                bg=self.CARD_INNER,
                fg=self.TEXT_PRIMARY,
                activebackground=self.ACCENT,
                activeforeground="#ffffff",
                bd=0,
                padx=16,
                pady=11,
                anchor="w",
                cursor="hand2",
                relief=tk.FLAT,
                command=lambda opt_idx=i: self.handle_answer(opt_idx)
            )
            btn.pack(fill=tk.X, pady=5)
            self.option_buttons.append(btn)

        # Feedback & Fact Card (initially hidden or empty)
        self.feedback_frame = tk.Frame(card, bg=self.CARD_BG)
        self.feedback_frame.pack(fill=tk.X, pady=(10, 0))

        # Next button (hidden until answered)
        self.next_btn = tk.Button(
            card,
            text="Next Question  ➔",
            font=("Helvetica", 11, "bold"),
            bg=self.ACCENT,
            fg="#ffffff",
            activebackground=self.ACCENT_HOVER,
            activeforeground="#ffffff",
            bd=0,
            padx=24,
            pady=9,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.next_question
        )

        # Start question timer
        self.run_timer()

    # ==========================
    # 4. TIMER LOGIC
    # ==========================
    def run_timer(self):
        if self.time_left > 0:
            color = self.TIMER_WARN if self.time_left <= 5 else self.TIMER_COLOR
            self.timer_lbl.config(
                text=f"⏱ {self.time_left}s",
                fg=color
            )
            self.time_left -= 1
            self.timer_job = self.root.after(1000, self.run_timer)
        else:
            self.timer_lbl.config(text="⏱ 0s", fg=self.TIMER_WARN)
            # Timeout triggered
            self.handle_answer(-1)

    # ==========================
    # 5. ANSWER HANDLING
    # ==========================
    def handle_answer(self, selected_index: int):
        if self.selected_answered:
            return
        self.selected_answered = True

        # Stop timer
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        q_data = self.questions[self.current_idx]
        correct_idx = q_data["answer"]

        # Disable all option buttons
        for btn in self.option_buttons:
            btn.config(cursor="arrow", state=tk.DISABLED)

        # Determine outcome
        is_correct = (selected_index == correct_idx)
        is_timeout = (selected_index == -1)

        if is_correct:
            self.score += 10
            self.score_lbl.config(text=f"Score: {self.score}")
            self.option_buttons[selected_index].config(
                bg=self.CORRECT_COLOR,
                fg="#ffffff"
            )
            status_text = "✓ Correct! (+10 pts)"
            status_color = self.CORRECT_COLOR
        else:
            if not is_timeout and selected_index >= 0:
                self.option_buttons[selected_index].config(
                    bg=self.WRONG_COLOR,
                    fg="#ffffff"
                )
            # Highlight correct answer
            self.option_buttons[correct_idx].config(
                bg=self.CORRECT_COLOR,
                fg="#ffffff"
            )
            if is_timeout:
                status_text = "⏰ Time's up! Here is the correct answer."
                status_color = self.TIMER_WARN
            else:
                status_text = "✗ Incorrect! Here is the correct answer."
                status_color = self.WRONG_COLOR

        # Record history for review
        user_choice_text = (
            "Timed Out" if is_timeout else q_data["options"][selected_index]
        )
        self.user_history.append({
            "question": q_data["question"],
            "selected": user_choice_text,
            "correct": q_data["options"][correct_idx],
            "is_correct": is_correct,
            "fact": q_data.get("fact", "")
        })

        # Render Feedback & Fact
        status_lbl = tk.Label(
            self.feedback_frame,
            text=status_text,
            font=("Helvetica", 11, "bold"),
            bg=self.CARD_BG,
            fg=status_color
        )
        status_lbl.pack(anchor="w")

        fact_text = f"💡 Did you know? {q_data['fact']}"
        fact_lbl = tk.Label(
            self.feedback_frame,
            text=fact_text,
            font=("Helvetica", 10, "italic"),
            bg=self.CARD_BG,
            fg="#94a3b8",
            wraplength=640,
            justify=tk.LEFT
        )
        fact_lbl.pack(anchor="w", pady=(3, 0))

        # Show next button
        if self.current_idx + 1 < len(self.questions):
            self.next_btn.config(text="Next Question  ➔")
        else:
            self.next_btn.config(text="View Final Results  ★")

        self.next_btn.pack(side=tk.RIGHT, pady=(10, 0))

    def next_question(self):
        self.current_idx += 1
        if self.current_idx < len(self.questions):
            self.show_question()
        else:
            self.show_results_screen()

    # ==========================
    # 6. RESULTS SCREEN
    # ==========================
    def show_results_screen(self):
        self.clear_container()

        total = len(self.questions)
        max_score = total * 10
        percentage = int((self.score / max_score) * 100) if max_score > 0 else 0
        correct_count = sum(1 for item in self.user_history if item["is_correct"])

        # Determine Badge and Title
        if percentage == 100:
            badge = "🏆 PERFECT SCORE! 🏆"
            title = "Grandmaster Genius!"
            badge_color = "#f59e0b"
        elif percentage >= 80:
            badge = "🌟 EXCELLENT WORK! 🌟"
            title = "Trivia Master!"
            badge_color = "#10b981"
        elif percentage >= 60:
            badge = "👍 GOOD JOB! 👍"
            title = "Knowledge Enthusiast!"
            badge_color = "#38bdf8"
        elif percentage >= 40:
            badge = "📚 DECENT EFFORT 📚"
            title = "Keep Practicing!"
            badge_color = "#a5b4fc"
        else:
            badge = "🌱 LEARNING OPPORTUNITY 🌱"
            title = "Give it Another Shot!"
            badge_color = "#f87171"

        card = tk.Frame(self.container, bg=self.CARD_BG, padx=30, pady=24)
        card.pack(fill=tk.BOTH, expand=True)

        # Header Badge
        badge_lbl = tk.Label(
            card,
            text=badge,
            font=("Helvetica", 11, "bold"),
            bg="#272738",
            fg=badge_color,
            padx=14,
            pady=4
        )
        badge_lbl.pack(pady=(10, 8))

        # Big Title
        title_lbl = tk.Label(
            card,
            text=title,
            font=("Helvetica", 24, "bold"),
            bg=self.CARD_BG,
            fg=self.TEXT_PRIMARY
        )
        title_lbl.pack(pady=(0, 15))

        # Score Summary Box
        score_box = tk.Frame(card, bg=self.CARD_INNER, padx=24, pady=16)
        score_box.pack(fill=tk.X, padx=40, pady=(0, 20))

        score_display = tk.Label(
            score_box,
            text=f"{self.score} / {max_score}",
            font=("Helvetica", 28, "bold"),
            bg=self.CARD_INNER,
            fg="#38bdf8"
        )
        score_display.pack()

        stat_sub = tk.Label(
            score_box,
            text=f"Accuracy: {percentage}%  |  Correct: {correct_count}/{total} Questions",
            font=("Helvetica", 11),
            bg=self.CARD_INNER,
            fg=self.TEXT_MUTED
        )
        stat_sub.pack(pady=(4, 0))

        # Action Buttons
        btn_box = tk.Frame(card, bg=self.CARD_BG)
        btn_box.pack(pady=10)

        play_again_btn = tk.Button(
            btn_box,
            text="Play Again  🔄",
            font=("Helvetica", 12, "bold"),
            bg=self.ACCENT,
            fg="#ffffff",
            activebackground=self.ACCENT_HOVER,
            activeforeground="#ffffff",
            bd=0,
            padx=24,
            pady=10,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.start_new_game
        )
        play_again_btn.pack(side=tk.LEFT, padx=8)

        review_btn = tk.Button(
            btn_box,
            text="Review Answers  📋",
            font=("Helvetica", 12),
            bg="#334155",
            fg=self.TEXT_PRIMARY,
            activebackground="#475569",
            activeforeground="#ffffff",
            bd=0,
            padx=18,
            pady=10,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.show_review_screen
        )
        review_btn.pack(side=tk.LEFT, padx=8)

        home_btn = tk.Button(
            btn_box,
            text="Home Menu",
            font=("Helvetica", 12),
            bg="#272738",
            fg=self.TEXT_MUTED,
            activebackground="#3f3f46",
            activeforeground="#ffffff",
            bd=0,
            padx=16,
            pady=10,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.show_welcome_screen
        )
        home_btn.pack(side=tk.LEFT, padx=8)

    # ==========================
    # 7. REVIEW SCREEN
    # ==========================
    def show_review_screen(self):
        self.clear_container()

        header_bar = tk.Frame(self.container, bg=self.BG_DARK)
        header_bar.pack(fill=tk.X, pady=(0, 10))

        header_lbl = tk.Label(
            header_bar,
            text="Answer Review",
            font=("Helvetica", 16, "bold"),
            bg=self.BG_DARK,
            fg=self.TEXT_PRIMARY
        )
        header_lbl.pack(side=tk.LEFT)

        back_btn = tk.Button(
            header_bar,
            text="Back to Summary  ➔",
            font=("Helvetica", 10, "bold"),
            bg=self.ACCENT,
            fg="#ffffff",
            activebackground=self.ACCENT_HOVER,
            activeforeground="#ffffff",
            bd=0,
            padx=16,
            pady=6,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.show_results_screen
        )
        back_btn.pack(side=tk.RIGHT)

        # Scrollable container for question reviews
        canvas = tk.Canvas(self.container, bg=self.CARD_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.CARD_BG, padx=16, pady=16)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        def configure_canvas(event):
            canvas.itemconfig(canvas_window, width=event.width)

        canvas.bind("<Configure>", configure_canvas)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Mouse wheel support
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mousewheel)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for i, item in enumerate(self.user_history, start=1):
            is_correct = item["is_correct"]
            item_box = tk.Frame(
                scrollable_frame,
                bg=self.CARD_INNER,
                padx=16,
                pady=12,
                bd=0
            )
            item_box.pack(fill=tk.X, pady=6)

            tag_color = self.CORRECT_COLOR if is_correct else self.WRONG_COLOR
            tag_text = "✓ CORRECT" if is_correct else "✗ INCORRECT"

            top_row = tk.Frame(item_box, bg=self.CARD_INNER)
            top_row.pack(fill=tk.X)

            q_num_lbl = tk.Label(
                top_row,
                text=f"Q{i}. {item['question']}",
                font=("Helvetica", 11, "bold"),
                bg=self.CARD_INNER,
                fg=self.TEXT_PRIMARY,
                wraplength=540,
                justify=tk.LEFT
            )
            q_num_lbl.pack(side=tk.LEFT, anchor="w")

            status_tag = tk.Label(
                top_row,
                text=tag_text,
                font=("Helvetica", 9, "bold"),
                bg=tag_color,
                fg="#ffffff",
                padx=6,
                pady=2
            )
            status_tag.pack(side=tk.RIGHT, anchor="ne")

            # Answers details
            details_text = f"Your Answer: {item['selected']}"
            if not is_correct:
                details_text += f"   |   Correct Answer: {item['correct']}"

            ans_lbl = tk.Label(
                item_box,
                text=details_text,
                font=("Helvetica", 10),
                bg=self.CARD_INNER,
                fg=tag_color if not is_correct else "#86efac",
                anchor="w"
            )
            ans_lbl.pack(fill=tk.X, pady=(6, 2))

            if item.get("fact"):
                fact_lbl = tk.Label(
                    item_box,
                    text=f"Fact: {item['fact']}",
                    font=("Helvetica", 9, "italic"),
                    bg=self.CARD_INNER,
                    fg=self.TEXT_MUTED,
                    wraplength=600,
                    justify=tk.LEFT,
                    anchor="w"
                )
                fact_lbl.pack(fill=tk.X)


def main():
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
