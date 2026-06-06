import time
import os



def slow_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Database

recommendation_data = {
    "Technology": {
        "items": [
            {"name": "AI & Machine Learning Masterclass", "score": 96},
            {"name": "Python Programming Bootcamp",        "score": 93},
            {"name": "Data Science Handbook",              "score": 89},
            {"name": "Cybersecurity Fundamentals Guide",   "score": 85},
            {"name": "Cloud Computing with AWS",           "score": 82},
        ]
    },
    "Fitness": {
        "items": [
            {"name": "30-Day Workout Planner",             "score": 95},
            {"name": "Healthy Diet & Nutrition Program",   "score": 91},
            {"name": "Yoga for Beginners",                 "score": 87},
            {"name": "Weight Loss Blueprint",              "score": 84},
            {"name": "Running & Endurance Training",       "score": 80},
        ]
    },
    "Gaming": {
        "items": [
            {"name": "Mechanical Gaming Keyboard Guide",   "score": 94},
            {"name": "Top Action Games of the Year",       "score": 90},
            {"name": "Esports Strategy Guide",             "score": 86},
            {"name": "FPS Training & Aim Pack",            "score": 83},
            {"name": "Gaming Setup Optimization",          "score": 79},
        ]
    },
    "Music": {
        "items": [
            {"name": "Guitar Lessons for Beginners",       "score": 97},
            {"name": "Music Production Masterclass",       "score": 92},
            {"name": "Piano Course from Scratch",          "score": 88},
            {"name": "Audio Mixing & Editing Toolkit",     "score": 85},
            {"name": "Music Theory Fundamentals",          "score": 81},
        ]
    },
    "Movies": {
        "items": [
            {"name": "IMDB Top 250 Watchlist",             "score": 95},
            {"name": "Sci-Fi Classics Collection",         "score": 91},
            {"name": "Thriller Movie Pack",                "score": 87},
            {"name": "Award-Winning Documentaries",        "score": 84},
            {"name": "Directors' Cut Series",              "score": 80},
        ]
    },
    "Books": {
        "items": [
            {"name": "Atomic Habits — James Clear",        "score": 98},
            {"name": "Deep Work — Cal Newport",            "score": 93},
            {"name": "Rich Dad Poor Dad",                  "score": 89},
            {"name": "Self Development Collection",        "score": 85},
            {"name": "The Psychology of Money",            "score": 82},
        ]
    }
}



def get_recommendations(user_interests):
    matched_items = []

    for interest in user_interests:
        interest = interest.strip().title()

        if interest in recommendation_data:
            for item in recommendation_data[interest]["items"]:
                matched_items.append({
                    "category": interest,
                    "name":     item["name"],
                    "score":    item["score"]
                })

    # Sort by score descending
    matched_items.sort(key=lambda x: x["score"], reverse=True)
    return matched_items



def display_results(matched_items):
    if not matched_items:
        slow_print("\nNo matching interests found.")
        slow_print("Please choose from the available categories.")
        return

    total     = len(matched_items)
    avg_score = round(sum(i["score"] for i in matched_items) / total)
    top_score = matched_items[0]["score"]

    slow_print("\n" + "=" * 55)
    slow_print("             TOP RECOMMENDATIONS FOR YOU")
    slow_print("=" * 55)

    print(f"\n  Total Recommendations : {total}")
    print(f"  Average Match Score   : {avg_score}%")
    print(f"  Top Match Score       : {top_score}%")
    print("-" * 55)

    for index, rec in enumerate(matched_items, start=1):
        bar_filled = int(rec["score"] / 5)
        bar        = "█" * bar_filled + "░" * (20 - bar_filled)
        print(f"\n{index:>2}. {rec['name']}")
        print(f"    Category : {rec['category']}")
        print(f"    Match    : [{bar}] {rec['score']}%")
        print("    " + "-" * 50)

def main():
    clear()

    slow_print("=" * 55)
    slow_print("       ADVANCED AI RECOMMENDATION SYSTEM")
    slow_print("=" * 55)

    slow_print("\nAVAILABLE INTEREST CATEGORIES:\n")
    for category in recommendation_data.keys():
        print(f"  • {category}")

    while True:
        user_input = input(
            "\nEnter your interests separated by commas\n> "
        ).strip()

        if not user_input:
            print("Please enter at least one interest.")
            continue

        user_interests = [i.strip() for i in user_input.split(",")]

        # Check if any interest is valid
        valid = [i.title() for i in user_interests if i.title() in recommendation_data]
        invalid = [i for i in user_interests if i.title() not in recommendation_data]

        if invalid:
            print(f"\n  Note: '{', '.join(invalid)}' not found in categories. Skipping.")

        if not valid:
            slow_print("\nNone of your interests matched. Please try again.")
            continue

        slow_print("\nAnalyzing your preferences...")
        time.sleep(1.2)

        results = get_recommendations(valid)
        display_results(results)

        # Ask to search again
        while True:
            choice = input(
                "\nSearch again? (yes / no): "
            ).strip().lower()

            if choice == "yes":
                clear()
                slow_print("=" * 55)
                slow_print("       ADVANCED AI RECOMMENDATION SYSTEM")
                slow_print("=" * 55)
                slow_print("\nAVAILABLE INTEREST CATEGORIES:\n")
                for category in recommendation_data.keys():
                    print(f"  • {category}")
                break

            elif choice == "no":
                slow_print("\nThank you for using the system!")
                slow_print("=" * 55)
                return

            else:
                print("Invalid input. Type yes or no.")



if __name__ == "__main__":
    main()
