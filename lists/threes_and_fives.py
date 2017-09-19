Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.

threes_and_fives = [x for x in range(1, 16) if not(x % 3) or not(x % 5)]
