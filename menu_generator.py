import random

main_courses = ["spaghetti", "hamburger", "steak", "tacos"]
sides = ["fries", "veggies", "fruit", "bread"]
desserts = ["ice cream", "pie", "cake", "cookies"]

full_meal = random.choice(main_courses) + " , "+random.choice(sides) + " , "+random.choice(desserts)
print(full_meal)
