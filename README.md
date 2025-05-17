# 🧠 Kahoot AI Agent

An AI-powered agent built to play [Kahoot!](https://kahoot.it) quizzes automatically. This project combines web automation with real-time question processing using language models to answer questions accurately and quickly.

## 🎯 Project Goals

- Automate joining and interacting with Kahoot games using Playwright.
- Extract quiz questions and answer choices in real time.
- Use an AI agent (LLM) to determine the best answer.
- Automatically select the correct answer on the quiz interface.
- Optimize speed, accuracy, and resilience against anti-bot detection.

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **[Playwright](https://playwright.dev/python/)** for browser automation.
- **LLM (OpenAI GPT or local model)** for question answering.
- Optional: Local trivia cache or retrieval-based augmentation for speed.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/kahoot-ai-agent.git
cd kahoot-ai-agent
```

### 2. Create and Activate a Virtual Environment

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not yet created, run:

```bash
pip freeze > requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install
```

---

## 📦 Project Structure

```
kahoot-ai-agent/
│
├── agent/                  # AI logic for answering questions
│   └── model.py
├── automation/             # Playwright automation scripts
│   └── kahoot_bot.py
├── utils/                  # Utilities for parsing and logging
│   └── parser.py
├── main.py                # Entry point to run the agent
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## ✅ Example Usage
