import random
import json, os

def load_all_challenges():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data'))
    print("Resolved data path:", base)
    
    levels = ['beginner', 'intermediate', 'advanced', 'pro']
    challenge_pool = {}

    for level in levels:
        path = os.path.join(base, f"{level}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"{level}: loaded {len(data)} challenges ✅")
                challenge_pool[level] = data
        except Exception as e:
            print(f"{level}: ❌ error loading - {e}")
            challenge_pool[level] = []

    return challenge_pool


def sum_two_numbers(a, b):
    return f"Sum: {a + b}"

def rectangle_area(width, height):
    return f"Area: {width * height}"

def celsius_to_fahrenheit(c):
    f = c * 1.8 + 32
    return f"{c}°C is {f:.2f}°F"

def uppercase_name(name):
    return f"Uppercase: {name.upper()}"

def sum_from_one_to_n(n):
    return f"Sum from 1 to {n}: {sum(range(1, n + 1))}"

def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def simple_calculator(a, op, b):
    try:
        if op == "+":
            return str(a + b)
        elif op == "-":
            return str(a - b)
        elif op == "*":
            return str(a * b)
        elif op == "/":
            return str(a / b) if b != 0 else "❗ Cannot divide by zero."
        else:
            return "❗ Invalid operator."
    except:
        return "❗ Error in calculation."

def multiplication_table():
    table = ""
    for i in range(1, 11):
        row = "\t".join(f"{i}×{j}={i*j}" for j in range(1, 11))
        table += row + "\n"
    return table

def list_of_squares(n):
    squares = [str(i**2) for i in range(1, n + 1)]
    return "Squares: " + ", ".join(squares)

def min_max_avg(a, b, c, d, e):
    nums = [a, b, c, d, e]
    return f"Min: {min(nums)}, Max: {max(nums)}, Average: {sum(nums)/5:.2f}"

def guess_random_number(guess):
    secret = random.randint(1, 100)
    if guess < secret:
        return f"Too low! Secret was {secret}."
    elif guess > secret:
        return f"Too high! Secret was {secret}."
    else:
        return "🎉 Correct! You guessed it."

def time_to_seconds(h, m, s):
    return f"Total seconds: {h * 3600 + m * 60 + s}"

def count_characters(text):
    return f"Character count: {len(text)}"

def replace_spaces(text):
    return text.replace(" ", "_")

def reverse_string(text):
    return f"Reversed: {text[::-1]}"

def sort_three_numbers(a, b, c):
    nums = sorted([a, b, c])
    return f"Sorted: {nums}"

def star_triangle():
    return "\n".join("*" * i for i in range(1, 6))

def count_to_ten():
    for_part = " ".join(str(i) for i in range(1, 11))
    while_part = ""
    i = 1
    while i <= 10:
        while_part += str(i) + " "
        i += 1
    return f"For loop: {for_part}\nWhile loop: {while_part.strip()}"

def sum_to_n(n):
    return f"Sum to {n}: {n * (n + 1) // 2}"

def is_prime(n):
    if n < 2:
        return f"{n} is not a prime."
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"{n} is not a prime."
    return f"{n} is a prime number."


challenges = {
    1: ("Sum Two Numbers", sum_two_numbers, ["a", "b"]),
    2: ("Rectangle Area", rectangle_area, ["width", "height"]),
    3: ("Celsius to Fahrenheit", celsius_to_fahrenheit, ["c"]),
    4: ("Uppercase Name", uppercase_name, ["name"]),
    5: ("Sum from 1 to n", sum_from_one_to_n, ["n"]),
    6: ("Even or Odd", even_or_odd, ["n"]),
    7: ("Simple Calculator", simple_calculator, ["a", "op", "b"]),
    8: ("Multiplication Table", multiplication_table, []),
    9: ("List of Squares", list_of_squares, ["n"]),
    10: ("Min, Max, Average", min_max_avg, ["a", "b", "c", "d", "e"]),
    11: ("Guess the Number", guess_random_number, ["guess"]),
    12: ("Time to Seconds", time_to_seconds, ["h", "m", "s"]),
    13: ("Count Characters", count_characters, ["text"]),
    14: ("Replace Spaces", replace_spaces, ["text"]),
    15: ("Reverse String", reverse_string, ["text"]),
    16: ("Sort Three Numbers", sort_three_numbers, ["a", "b", "c"]),
    17: ("Star Triangle", star_triangle, []),
    18: ("Count to Ten", count_to_ten, []),
    19: ("Sum to n (Formula)", sum_to_n, ["n"]),
    20: ("Prime Number Check", is_prime, ["n"])
}
