# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The game is a number guessing game built with Streamlit where the player tries to guess a secret number within a limited number of attempts, with hints and a scoring system based on how quickly they guess correctly. The bugs found included reversed hints that told the player to go lower when they should go higher, a Hard difficulty range that was smaller than Normal difficulty, and guess validation that was hardcoded to 1-100 and ignored the actual difficulty range. The fixes applied were correcting the comparison logic in `check_guess`, updating `get_range_for_difficulty` to return `1-200` for Hard, and updating `parse_guess` to use the dynamic `low` and `high` range values. All game logic was refactored out of `app.py` and into `logic_utils.py` to separate concerns and make the code testable.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Player selects "Normal" difficulty from the sidebar — the game sets a secret number between 1 and 100 with 8 attempts allowed.
2. Player enters a guess of 40 and clicks "Submit Guess" — the game returns "📈 Go HIGHER!" since the secret is higher than 40.
3. Player enters a guess of 70 — the game returns "📉 Go LOWER!" since the secret is lower than 70.
4. Player enters a guess of 55 — the game returns "🎉 Correct!" and balloons appear on screen.
5. Score is calculated based on the number of attempts used and displayed in the win message.
6. Player clicks "New Game" — all state resets cleanly, a new secret number is generated, and the input field clears.

## 🧪 Test Results

```
===================================================================== test session starts =====================================================================
platform win32 -- Python 3.13.14, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\omadi\Documents\GitHub\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0, dash-4.1.0, timeout-2.4.0
collected 9 items

tests\test_game_logic.py .........                                                                [100%]

====================================================================== 9 passed in 0.11s ======================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]