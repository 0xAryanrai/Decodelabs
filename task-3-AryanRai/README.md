# 🎯 AI Recommendation System

A terminal-based personalized recommendation engine built in Python. Enter your interests and get ranked recommendations with match scores — no libraries, no setup, just run and go.

---

## 📸 Preview

```
=======================================================
       ADVANCED AI RECOMMENDATION SYSTEM
=======================================================

AVAILABLE INTEREST CATEGORIES:

  • Technology
  • Fitness
  • Gaming
  • Music
  • Movies
  • Books

Enter your interests separated by commas
> Technology, Music, Books

Analyzing your preferences...

=======================================================
             TOP RECOMMENDATIONS FOR YOU
=======================================================

  Total Recommendations : 15
  Average Match Score   : 89%
  Top Match Score       : 98%
-------------------------------------------------------

 1. Atomic Habits — James Clear
    Category : Books
    Match    : [███████████████████░] 98%
    --------------------------------------------------

 2. Guitar Lessons for Beginners
    Category : Music
    Match    : [███████████████████░] 97%
    --------------------------------------------------

 3. AI & Machine Learning Masterclass
    Category : Technology
    Match    : [███████████████████░] 96%
    --------------------------------------------------
```

---

## 🚀 Features

- **Multi-interest input** — enter multiple interests at once, separated by commas
- **Scored recommendations** — every item has a real match score (not random)
- **Visual progress bars** — see match strength at a glance using `█` bars
- **Summary stats** — total results, average score, and top score shown upfront
- **Invalid input handling** — unknown categories are skipped with a clear message
- **Search again** — loop without restarting the program
- **Typing effect** — smooth character-by-character output for a polished feel

---

## 📁 Project Structure

```
recommendation_system.py   ← main file (everything in one script)
README.md
```

---

## ▶️ How to Run

**Requirements:** Python 3.x — no external libraries needed.

```bash
python recommendation_system.py
```

Or on some systems:

```bash
python3 recommendation_system.py
```

---

## 🧠 How It Works

1. The program displays all available interest categories
2. You enter one or more interests (e.g. `Gaming, Music`)
3. The engine matches your input against a built-in database of items, each with a pre-defined match score
4. Results are sorted by score (highest first) and displayed with a visual bar
5. You can search again without restarting

### Matching Logic

```python
# Items are filtered by category match, then sorted by score
matched_items.sort(key=lambda x: x["score"], reverse=True)
```

Each item in the database has a manually curated relevance score (79–98%). When you select a category, all items from that category enter the results pool and are ranked globally across all your selected interests.

---

## 📦 Categories & Items

| Category   | Sample Recommendations                          |
|------------|--------------------------------------------------|
| Technology | AI & ML Masterclass, Python Bootcamp, AWS Guide |
| Fitness    | 30-Day Workout Planner, Yoga, Diet Program       |
| Gaming     | Esports Strategy Guide, FPS Training Pack        |
| Music      | Guitar Lessons, Music Production Masterclass     |
| Movies     | IMDB Top 250, Sci-Fi Classics, Thriller Pack     |
| Books      | Atomic Habits, Deep Work, Psychology of Money    |

---

## 🔧 Extending the Project

To add a new category or item, edit the `recommendation_data` dictionary in the script:

```python
"Travel": {
    "items": [
        {"name": "Budget Travel Guide", "score": 91},
        {"name": "Solo Travel Tips",    "score": 87},
    ]
}
```

---

## 👤 Author

**ARYAN RAI**
DecodeLabs_Internship — Project 3

---

## 📄 License

This project is open-source and available for learning purposes. **
