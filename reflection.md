# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The first time I ran the game, it looked like a normal guessing game with difficulty settings, scoring, and hints, but several features did not work correctly. One of the first bugs I noticed was that the hints were backwards because the game told me to "Go LOWER!" even when my guess was lower than the secret number. I also found that the New Game button did not fully reset the game, and I sometimes had to refresh the page before I could play again. Another issue was that the game accepted invalid guesses such as negative numbers and values outside the allowed range for the selected difficulty instead of displaying an error message.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input Used                             | Expected Behavior        | Actual Behavior                | Console Error / Output |
| -------------------------------------- | ------------------------ | ------------------------------ | ---------------------- |
| Guess of 1                             | "Go HIGHER!" hint        | "Go LOWER!" hint               | none                   |
| Clicked New Game after losing          | New game starts normally | Game still says "Game Over"    | none                   |
| Guess of -35                           | Invalid input message    | Guess accepted                 | none                   |
| Guess of -100                          | Invalid input message    | Guess accepted                 | none                   |
| Guess above 20 in Easy mode            | Invalid input message    | Guess accepted                 | none                   |
| Guess of 8, then 4 with 1 attempt left | One remaining attempt    | "Out of attempts!" shown early | none                   |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude (via Claude.ai) as my primary AI assistant throughout this project to help me refactor code, write tests, and plan my fixes. One correct suggestion Claude made was identifying that the existing starter tests were broken because they compared `check_guess` results to a plain string instead of unpacking the tuple it actually returns. I verified this by reading the function definition and confirming the return value was `("Too High", "📉 Go LOWER!")`, then updated the tests accordingly and confirmed they passed. One misleading suggestion Claude made was an incorrect fix for the reversed hints bug, where it initially suggested flipping the comparison operator in `check_guess` in a way that still produced the wrong output for edge cases. I caught this by manually walking through the logic with specific values. For example, a guess of 60 against a secret of 50 should return "Too High", but the AI's suggested fix still returned the wrong result, so I reasoned through the correct comparison myself and verified it by running the game and then confirming it with pytest.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I verified each bug fix in two ways: by running the automated pytest suite and by manually testing the live game with `streamlit run app.py`. For the reversed hints bug, I ran a pytest case that called `check_guess(60, 50)` and asserted the outcome was `"Too High"`. This test would have failed on the original buggy code since the hints were flipped. For the Hard difficulty range bug, I wrote a test confirming `get_range_for_difficulty("Hard")` returns `(1, 200)` and that the Hard upper bound is greater than Normal's. All 9 tests passed when I ran `python -m pytest`. Claude helped me design the tests by suggesting the tuple unpacking pattern and writing targeted cases for each specific bug rather than generic ones.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
