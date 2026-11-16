# Name: Poshini Srinivasan
# Group letter: C
# Group number: "CL10"
#
# Q1 - WHAT GOES IN?
# scenarios_C.csv. is comma-separated and has 14 columns:
# Event, Day, three decisions, three reputation impacts, three budget impacts,
# and three outcome messages. Impacts look like +15 pts and -800 EUR.
#
# Q2 - WHAT HAPPENS EACH DAY?
# Show the day and gauges; show the event and A/B/C choices; ask until valid;
# apply the selected changes; show feedback; record the move; stop if a gauge is <= 0.
#
# Q3 - WHAT COMES OUT?
# Show fired/survived, final score and title, and best/worst reputation move.
# Append name, budget, reputation, title and date to results.csv.
#
# Q4 - WHAT COULD GO WRONG?
# Wrong choice: ask again. Missing CSV: show an error. Invalid impact: use zero.
# A gauge <= 0: end the game immediately. Blank player name: use Player.
#
# FEATURE CHOSEN: A - STREAK BONUS.
# Three reputation gains in a row give +500 EUR. It rewards consistent good choices.

import csv
import random
import re
from datetime import date

SCENARIO_FILE = "scenarios_C_completed.csv"
RESULTS_FILE = "results.csv"

def impact_number(value):
    """Convert text such as '+15 pts' or '-800 EUR' into an integer."""
    match = re.search(r"[+-]?\s*\d+", str(value))
    return int(match.group(0).replace(" ", "")) if match else 0

def load_scenarios():
    """Read all events and their three options from the CSV file."""
    result = []
    with open(SCENARIO_FILE, encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file):
            options = []
            for n in range(1, 4):
                options.append((row[f"Decision {n}"],
                                impact_number(row[f"Budget {n}"]),
                                impact_number(row[f"Reputation {n}"]),
                                row[f"Outcome {n}"]))
            result.append((row["Event"], options))
    return result

def ask_choice():
    """Ask repeatedly until A, B or C is entered."""
    while True:
        answer = input("Your choice (A, B or C): ").strip().lower()
        if answer in ("a", "b", "c"):
            return ord(answer) - ord("a")
        print("Please type A, B or C.")

def apply_choice(budget, reputation, option):
    """Return the updated budget and reputation as a tuple."""
    _, budget_change, reputation_change, _ = option
    return budget + budget_change, min(100, reputation + reputation_change)

def save_result(name, budget, reputation, title):
    """Append one game result to results.csv."""
    try:
        with open(RESULTS_FILE, encoding="utf-8") as file:
            has_header = bool(file.readline())
    except FileNotFoundError:
        has_header = False
    with open(RESULTS_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if not has_header:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])

def play_game():
    """Play ten shuffled days and report the final result."""
    name = input("Player name: ").strip() or "Player"
    events = load_scenarios()
    random.shuffle(events)
    budget, reputation = 10000, 50
    history = []
    streak = 0
    fired = ""

    for day, (event, options) in enumerate(events[:10], start=1):
        print(f"\\n--- Day {day} ---")
        print(f"Budget: {budget} EUR | Reputation: {reputation}/100")
        print(event)
        for i, option in enumerate(options):
            print(f"{chr(65+i)}: {option[0]}")
        option = options[ask_choice()]
        text, budget_change, rep_change, feedback = option
        history.append((day, text, rep_change))
        budget, reputation = apply_choice(budget, reputation, option)
        print(feedback)
        print(f"Budget {budget_change:+} EUR, Reputation {rep_change:+} pts")

        # Feature A: reward three positive reputation changes in a row.
        streak = streak + 1 if rep_change > 0 else 0
        if streak == 3:
            budget += 500
            streak = 0
            print("STREAK BONUS: +500 EUR")

        print(f"Budget: {budget} EUR | Reputation: {reputation}/100")
        if budget <= 0:
            fired = "Your budget reached zero or less."
            break
        if reputation <= 0:
            fired = "Your reputation reached zero or less."
            break

    if fired:
        title = "Fired"
        print("\\nYou are fired! " + fired)
    else:
        score = reputation + budget // 200
        if score < 95: title = "Eternal Intern"
        elif score < 120: title = "Growth Hacker"
        elif score < 140: title = "CMO Material"
        else: title = "Viral Legend"
        print(f"\\nQuarter survived! Final score: {score}")
        print(f"{name}, your title: {title}")

    if history:
        best = max(history, key=lambda move: move[2])
        worst = min(history, key=lambda move: move[2])
        print(f"Best move: day {best[0]}, {best[1]} ({best[2]:+} pts)")
        print(f"Worst move: day {worst[0]}, {worst[1]} ({worst[2]:+} pts)")
    save_result(name, budget, reputation, title)
    print("Saved in results.csv")

if __name__ == "__main__":
    try:
        play_game()
    except FileNotFoundError:
        print("ERROR: scenarios_C_completed.csv is missing. Keep it beside this Python file.")
    except (KeyError, ValueError) as error:
        print("There is a problem in the scenario CSV:", error)
