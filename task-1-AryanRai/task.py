# ============================================================
#   DecodeLabs | AI Internship | Project 1
#   Rule-Based AI Chatbot
#   Author  : AI Intern (Batch 2026)
#   Concept : IPO Model + Dictionary-based intent matching
# ============================================================

# ── KNOWLEDGE BASE (Hash Map / Dictionary) ──────────────────
# Using dict.get() for O(1) lookup instead of if-elif ladder.
# Add more intents here freely — no logic change needed.

RESPONSES = {
    # Greetings
    "hello"        : "Hey there! I'm DecoBot. How can I help you today?",
    "hi"           : "Hi!  What can I do for you?",
    "hey"          : "Hey! Great to see you. What's on your mind?",
    "good morning" : "Good morning! Hope you have a productive day!",
    "good evening" : "Good evening!  How was your day?",

    # About
    "who are you"  : "I'm DecoBot — a rule-based chatbot built during the DecodeLabs AI Internship (Batch 2026).",
    "what are you" : "I'm a rule-based AI chatbot. I respond to predefined inputs using a dictionary lookup — no ML, pure logic!",
    "your name"    : "My name is DecoBot. Built with  at DecodeLabs.",

    # Help
    "help"         : "I can respond to: greetings, questions about me, jokes, the time, and general chit-chat. Try 'hello' or 'tell me a joke'!",
    "what can you do" : "I can chat, crack a joke, tell you the date, and more. Just talk to me!",

    # Small talk
    "how are you"  : "I'm running at 100% efficiency! All systems operational.",
    "what's up"    : "Just processing inputs and generating outputs — the usual! ",
    "are you human": "Nope! I'm pure Python logic. No neural nets, just if-else and dictionaries.",

    # Fun
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! ",
    "another joke"  : "Why did the AI go to school? To improve its 'learning' rate! ",
    "fun fact"      : "Fun fact: The first chatbot, ELIZA, was created in 1966 at MIT. You're building on a 60-year-old tradition!",

    # DecodeLabs / Internship
    "what is decodelabs" : "DecodeLabs is a tech training organization based in Greater Lucknow, India. They run AI internship programs for students! 🇮🇳",
    "about internship"   : "This is the DecodeLabs AI Internship, Batch 2026. Project 1 is the Rule-Based Chatbot — you're living it right now!",

    # Date / Time
    "what is the date"  : __import__('datetime').date.today().strftime("Today is %A, %d %B %Y."),
    "what time is it"   : __import__('datetime').datetime.now().strftime("Current time: %I:%M %p"),

    # Farewell
    "bye"          : "Goodbye! Come back anytime. Type 'exit' to shut me down.",
    "goodbye"      : "See you later! Keep building cool things.",
    "see you"      : "See you! Stay curious.",
}

EXIT_COMMANDS = {"exit", "quit", "shutdown", "stop", "end"}

# ── PHASE 1: INPUT SANITIZATION
def sanitize(raw: str) -> str:
    """Lowercase + strip whitespace — normalize the raw feed."""
    return raw.lower().strip()

# ── PHASE 2: PROCESS (Intent Matching)
def get_response(clean_input: str) -> str:
    """
    Dictionary .get() → O(1) lookup.
    Falls back to a default message for unknown inputs.
    """
    
    # Direct match
    if clean_input in RESPONSES:
        return RESPONSES[clean_input]

    # Partial / keyword match (smarter fallback)
    for key in RESPONSES:
        if key in clean_input:
            return RESPONSES[key]

    # Default fallback
    return " I don't understand that yet. Type 'help' to see what I can do!"

# ── PHASE 3: OUTPUT + MAIN LOOP (Heartbeat) ─────────────────
def run_chatbot():
    print("=" * 55)
    print("   DecoBot — Rule-Based AI Chatbot")
    print("   DecodeLabs AI Internship | Batch 2026")
    print("   Type 'exit' to quit.")
    print("=" * 55)

    # ── THE INFINITE LOOP (stays alive until kill command) ──
    while True:

        # PHASE 1 — Raw Input
        raw_input = input("\nYou: ")

        # PHASE 1 — Sanitization
        clean_input = sanitize(raw_input)

        # Guard: empty input
        if not clean_input:
            print("DecoBot: Please type something!")
            continue

        # EXIT STRATEGY — Clean break command
        if clean_input in EXIT_COMMANDS:
            print("DecoBot: Shutting down... Goodbye! Great work today.")
            print("=" * 55)
            break

        # PHASE 2 — Process & Match Intent
        response = get_response(clean_input)

        # PHASE 3 — Output
        print(f"DecoBot: {response}")


# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
