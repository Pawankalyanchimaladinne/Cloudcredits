import random

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don’t let yesterday take up too much of today.",
    "You learn more from failure than from success.",
    "It’s not whether you get knocked down, it’s whether you get up."
]

quote = random.choice(quotes)
print("\nHere’s a random quote for you:\n")
print(f"\"{quote}\"")
