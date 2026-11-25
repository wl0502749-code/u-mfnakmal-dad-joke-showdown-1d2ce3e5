"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
The joke is a single line, well under the 200-character limit.
"""

import os

JOKE = "I got an air fryer for my birthday. Now I'm really winging it."


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 200 characters, not only
    # whitespace. Fail loudly instead of ever writing an invalid entry.
    joke = JOKE.strip()
    if not 1 <= len(joke) <= 200:
        raise ValueError(f"joke is {len(joke)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
