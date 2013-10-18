# Approach 1 - typing numbers without meaning
# Uses only math
print (96.0 + 194.0 + 163.0) / 3

# Approach 2 - applying labels to the numbers
# Uses variables and math
hobbits = 96.0
dwarves = 194.0
humans = 163.0
totalRaces = 3
mean = (hobbits + dwarves + humans) / totalRaces
print mean

# Approach 3 - adding context to the numbers
# Uses a list of numbers, variables, and some functions
lifeExpectancies = [96.0, 194.0, 163.0]
sumYears = sum( lifeExpectancies )
numberRaces = len( lifeExpectancies )
mean = sumYears / numberRaces
print mean
