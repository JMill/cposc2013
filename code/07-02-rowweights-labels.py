import pylab

# Type in data
cambridgeWeights = [188.5, 183, 194.5, 185, 214, 203.5, 186, 178.5, 109]
oxfordWeights = [186, 184.5, 204, 184.5, 195.5, 202.5, 174, 183, 109.5]

# Combine two lists into one list
totalWeights = cambridgeWeights + oxfordWeights

# Make a graph!
pylab.hist(totalWeights)
pylab.title("The Boat Race crew histogram")
pylab.xlabel("Weight in pounds")
pylab.ylabel("Number of members")
pylab.show()