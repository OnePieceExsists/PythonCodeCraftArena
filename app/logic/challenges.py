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
    c = float(c)
    f = c * 1.8 + 32
    return f"{c}°C = {f:.2f}°F"

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
    nums = [int(x) for x in [a, b, c, d, e]]
    return f"Min: {min(nums)}, Max: {max(nums)}, Average: {sum(nums)/5:.2f}"

def guess_random_number(guess):
    secret = random.randint(1, 100)
    if guess < secret:
        return f"Too low! Secret was {secret}."
    elif guess > secret:
        return f"Too high! Secret was {secret}."
    else:
        return "🎉 Correct! You guessed it."

def load_challenges_by_category(category_name):
    with open("data/challenges.json", encoding="utf-8") as f:
        challenges = json.load(f)
    return [c for c in challenges if c.get("category", "").lower() == category_name.lower()]


def time_to_seconds(h, m, s):
    h, m, s = int(h), int(m), int(s)
    return f"Total seconds: {h * 3600 + m * 60 + s}"

def count_characters(s):
    return f"Character count: {len(s)}"

def replace_spaces(s):
    return s.replace(" ", "_")

def reverse_string(s):
    return s[::-1]

def sort_three_numbers(a, b, c):
    nums = sorted([int(a), int(b), int(c)])
    return f"Sorted: {nums[0]}, {nums[1]}, {nums[2]}"

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

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return f"{n}! = {result}"

def reverse_string_v2(s):
    return s[::-1]

def ascii_value(c):
    return f"ASCII of '{c}' is {ord(c)}"

def password_check(password):
    return "Access granted" if password == "arena2025" else "Access denied"

def gcd(a, b):
    while b:
        a, b = b, a % b
    return f"GCD is {a}"

def triangle_height(area, base):
    return (2 * area) / base

def vowel_count(s):
    return sum(1 for c in s.lower() if c in "aeiou")

def is_palindrome(s):
    return "Palindrome" if s == s[::-1] else "Not a palindrome"

def kelvin_to_celsius(k):
    return k - 273.15

def convert_seconds(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h}:{m}:{s}"

def euro_to_dollar(euro):
    return round(euro * 1.1, 2)

def average_grade(grades):
    avg = sum(grades) / len(grades)
    return f"Average: {avg:.2f}"

def decimal_to_bin_hex(n):
    return f"Binary: {bin(n)}, Hex: {hex(n)}"

def array_rotate_right(arr):
    return [arr[-1]] + arr[:-1] if arr else []

def extract_initials(sentence):
    return ''.join(word[0].upper() for word in sentence.split())

def circle_area(r):
    return round(3.1416 * r * r, 2)

def bmi(height, weight):
    return round(weight / (height ** 2), 2)

def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

def string_lowercase(s):
    return s.lower()

def word_reverse(words):
    return list(reversed(words))

def fibonacci(n):
    seq = [0, 1]
    while seq[-1] + seq[-2] <= n:
        seq.append(seq[-1] + seq[-2])
    return seq

def count_letters_only(s):
    return sum(1 for c in s if c.isalpha())

def calc_age(birth_year, current_year):
    return current_year - birth_year

def ascii_art_triangle(n):
    return "\n".join("*" * i for i in range(1, n + 1))

def sum_even_digits(n):
    return sum(int(d) for i, d in enumerate(str(n)) if i % 2 == 1)

def weekday_from_number(n):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[n - 1] if 1 <= n <= 7 else "Invalid"

def abbreviate(phrase):
    return ''.join(word[0].upper() for word in phrase.split())

def simple_bubble_sort(nums):
    a = nums[:]
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def price_with_discount(qty, price):
    total = qty * price
    return total * 0.95 if qty > 100 else total

def hourglass(n):
    return "\n".join("*" * i for i in list(range(n, 0, -1)) + list(range(2, n + 1)))


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
    13: ("Count Characters", count_characters, ["s"]),
    14: ("Replace Spaces", replace_spaces, ["s"]),
    15: ("Reverse String", reverse_string, ["s"]),
    16: ("Sort Three Numbers", sort_three_numbers, ["a", "b", "c"]),
    17: ("Star Triangle", star_triangle, []),
    18: ("Count to Ten", count_to_ten, []),
    19: ("Sum to n (Formula)", sum_to_n, ["n"]),
    20: ("Prime Number Check", is_prime, ["n"]),
    21: ("Factorial", factorial, ["n"]),
    22: ("Reverse Text Again", reverse_string_v2, ["s"]),
    23: ("ASCII Value", ascii_value, ["c"]),
    24: ("Password Check", password_check, ["password"]),
    25: ("Greatest Common Divisor", gcd, ["a", "b"]),
    26: ("Triangle Height from Area", triangle_height, ["area", "base"]),
    27: ("Vowel Counter", vowel_count, ["s"]),
    28: ("Palindrome Check", is_palindrome, ["s"]),
    29: ("Kelvin to Celsius", kelvin_to_celsius, ["k"]),
    30: ("Convert Seconds to HH:MM:SS", convert_seconds, ["sec"]),
    31: ("Euro to Dollar Converter", euro_to_dollar, ["euro"]),
    32: ("Grade Average", average_grade, ["grades"]),
    33: ("Decimal to Binary & Hex", decimal_to_bin_hex, ["n"]),
    34: ("Array Right Rotation", array_rotate_right, ["arr"]),
    35: ("Extract Initials from Sentence", extract_initials, ["sentence"]),
    36: ("Circle Area", circle_area, ["r"]),
    37: ("BMI Calculator", bmi, ["height", "weight"]),
    38: ("Vowel Counter", count_vowels, ["s"]),
    39: ("String Lowercase", string_lowercase, ["s"]),
    40: ("Reverse Word List", word_reverse, ["words"]),
    41: ("Fibonacci Sequence", fibonacci, ["n"]),
    42: ("Letter Counter", count_letters_only, ["s"]),
    43: ("Calculate Age", calc_age, ["birth_year", "current_year"]),
    44: ("Triangle Pattern", ascii_art_triangle, ["n"]),
    45: ("Sum of Even-Position Digits", sum_even_digits, ["n"]),
    46: ("Day of the Week", weekday_from_number, ["n"]),
    47: ("Abbreviation Builder", abbreviate, ["phrase"]),
    48: ("Bubble Sort", simple_bubble_sort, ["nums"]),
    49: ("Bulk Price Discount", price_with_discount, ["qty", "price"]),
    50: ("Hourglass Pattern", hourglass, ["n"])
}
