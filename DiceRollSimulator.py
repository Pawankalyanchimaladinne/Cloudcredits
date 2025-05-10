import random

num_dice = int(input("Enter number of dice: "))
sides = int(input("Enter number of sides per dice: "))

print("\nRolling the dice...\n")
for i in range(num_dice):
    result = random.randint(1, sides)
    print(f"Dice {i + 1}: {result}")
