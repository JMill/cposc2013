# create the mean() function
def mean(myData):
    return sum(myData) / len(myData)

# Test the function
print "I know the average of 2.0, 2.0, and 5.0 to be 3.0."
print "My function says the average is:"
print mean( [2.0, 2.0, 5.0] )
print

# Calculate the rowing teams' means
cambridgeWeights = [188.5, 183, 194.5, 185, 214, 203.5, 186, 178.5, 109]
oxfordWeights = [186, 184.5, 204, 184.5, 195.5, 202.5, 174, 183, 109.5]

print "The average weight for Cambridge is:"
print mean(cambridgeWeights), "pounds"
print "and the average weight for Oxford is:"
print mean(oxfordWeights), "pounds"
print
print "This is a difference of:"
print mean(cambridgeWeights) - mean(oxfordWeights), "pounds "
