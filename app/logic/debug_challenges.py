from challenges import challenges
import traceback

def run_debug_suite():
    dummy_inputs = {
        "a": 5, "b": 3, "c": 10, "name": "Ilija", "op": "+", "n": 5,
        "height": 1.75, "weight": 70, "password": "arena2025",
        "grades": [1, 2, 3, 4, 5], "arr": [1, 2, 3, 4], "s": "Hello",
        "sentence": "Python Code Arena", "phrase": "Challenge Accepted",
        "nums": [5, 3, 1], "sec": 3755, "area": 25, "base": 5,
        "birth_year": 2000, "current_year": 2025, "qty": 150, "price": 9.99,
        "h": 1, "m": 2, "s": 3, "words": ["apple", "banana", "cherry"], 
        "s": "Hello World",              # used for string functions like lowercase, reverse, etc.
        "c": "A",                        # for ASCII character
        "phrase": "Code Arena Forever", # for abbreviation functions
        "sentence": "Python Rules Here",
        "words": ["code", "debug", "win"],
        "s": "Arena Debug Rocks",
        "c": "A",
        "words": ["apple", "banana", "cherry"],
        "c": "25",
        "a": 5,
        "b": 3,
        "d": 7,
        "e": 9,
        "h": 1,
        "m": 15,
        "s": 5,
}


    

    failed = []

    for cid, (title, func, args) in challenges.items():
        print(f"\n🔹 Challenge {cid}: {title}")
        try:
            arg_values = [dummy_inputs.get(arg, 1) for arg in args]
            output = func(*arg_values)
            print("   ✅ Output:", output)
        except Exception as e:
            print("   ❌ Error:", e)
            traceback.print_exc()
            failed.append((cid, title))

    print("\n=== Debug Summary ===")
    print(f"✅ Passed: {len(challenges) - len(failed)} / {len(challenges)}")
    if failed:
        print("❌ Failed Challenges:")
        for cid, title in failed:
            print(f"   - #{cid}: {title}")

if __name__ == "__main__":
    run_debug_suite()
