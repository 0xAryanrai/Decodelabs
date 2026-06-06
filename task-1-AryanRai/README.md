
**# 🤖 DecoBot — Rule-Based AI Chatbot

## 📌 Project Overview

DecoBot is a simple **Rule-Based AI Chatbot** built using Python as part of **Project 1** during the **DecodeLabs AI Internship (Batch 2026)**.

The chatbot uses a **dictionary-based intent matching system** along with basic input processing techniques to simulate conversational AI behavior without using Machine Learning or Neural Networks.

This project focuses on understanding the **fundamentals of conversational AI systems** using pure Python logic.

---

# 🚀 Features

* ✅ Greeting Responses
* ✅ Small Talk Support
* ✅ Joke Generation
* ✅ Date & Time Responses
* ✅ About / Help Commands
* ✅ Internship Information
* ✅ Exit Commands
* ✅ Input Sanitization
* ✅ Partial Keyword Matching
* ✅ O(1) Dictionary Lookup using `dict.get()`

---

# 🧠 Concepts Used

* Python Dictionaries (Hash Maps)
* Functions
* Loops
* String Processing
* Input Sanitization
* Rule-Based AI Logic
* IPO Model (Input → Process → Output)

---

# 📂 Project Structure

```bash
DecoBot/
│
├── chatbot.py       # Main chatbot source code
├── README.md        # Project documentation
```

---

# ⚙️ How It Works

The chatbot follows the **IPO Model**:

## 1️⃣ Input

User enters a message through the terminal.

## 2️⃣ Process

* Input is sanitized using:

  * Lowercasing
  * Whitespace removal
* The chatbot checks:

  * Exact dictionary match
  * Partial keyword match

## 3️⃣ Output

A predefined response is displayed to the user.

---

# ▶️ How to Run

## Step 1 — Clone Repository

```bash
git clone https://github.com/your-username/DecoBot.git
```

## Step 2 — Open Project Folder

```bash
cd DecoBot
```

## Step 3 — Run the Chatbot

```bash
python chatbot.py
```

---

# 💬 Example Conversation

```text
You: hello
DecoBot: Hey there! I'm DecoBot. How can I help you today?

You: tell me a joke
DecoBot: Why do programmers prefer dark mode? Because light attracts bugs!

You: bye
DecoBot: Goodbye! Come back anytime. Type 'exit' to shut me down.
```

---

# 🎯 Why This Project Matters

Understanding Rule-Based AI systems is an important first step toward becoming an AI Engineer.

This project helps in learning:

* Intent Recognition
* Conversation Flow
* Decision-Making Logic
* Pattern Matching
* Input Processing

Before building advanced AI systems using Machine Learning and NLP, understanding how rule-based systems work provides a strong foundation in AI problem-solving and chatbot architecture.

---

# 🛠️ Future Improvements

* Add GUI using Tkinter
* Add Speech Recognition
* Store Conversation History
* Add NLP-based Intent Detection
* Integrate Machine Learning Models
* Deploy as a Web App

---

# 👨‍💻 Author

**Aryan**
AI Intern — DecodeLabs (Batch 2026)

---

# 📜 License

This project is open-source and available for learning purposes.
**
