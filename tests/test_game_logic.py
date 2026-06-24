from logic_utils import check_guess, get_range_for_difficulty, parse_guess

# --- check_guess tests (covers the reversed-hint bug fix) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # Bug fix: guess > secret should return "Too High", not "Too Low"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # Bug fix: guess < secret should return "Too Low", not "Too High"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# --- get_range_for_difficulty tests (covers the Hard range bug fix) ---

def test_hard_range_is_larger_than_normal():
    # Bug fix: Hard should use 1-200, not a smaller range than Normal
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high

def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 200)

# --- parse_guess tests ---

def test_parse_valid_guess():
    ok, value, err = parse_guess("50", 1, 100)
    assert ok is True
    assert value == 50
    assert err is None

def test_parse_empty_guess():
    ok, value, err = parse_guess("", 1, 100)
    assert ok is False
    assert err == "Enter a guess."

def test_parse_non_numeric_guess():
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False

def test_parse_out_of_range_guess():
    ok, value, err = parse_guess("150", 1, 100)
    assert ok is False