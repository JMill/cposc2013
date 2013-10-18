#!/usr/bin/python -tt
# Copyright 2013 Jonathan B. Miller

# 'A Gentle Guide to Python', by Jonathan B. Miller, for LASTS 2013
# https://bitbucket.org/JMill/lasts2013py

# Basic string, integer, list, and if exercises
# Fill in the code for the functions below. 
# The starter code for each function includes a 'return'
# which is merely a placeholder for your code.
# It's okay if you do not complete every part of this exercise. 
# When you run this script, 'OK' will be printed when each function
# is correct.


# A. iLike
# Given an academic major, such as "English Lit", return the 
# sentence "I like English Lit". 
# (Hint: Try using '%s'.) 
def iLike(major):
  return # +++ your code here +++

# B. isLadida
# Given a string of characters, such as "banana" or "la di da",
# return True if the string matches "La di da", and False otherwise.
# (Hint: Use "==" to test if the left side is equivalent to the
# right side. e.g. "cow" == "cow" is True, but "cow" == "emu" is 
# False)
def isLadida(string):
  return # +++ your code here +++

# C. donuts
# Given an integer number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
# (Hint: the symbol for 'less than' is <, 'greater than' is >', and
# 'greater than or equal' is >=.)
def donuts(count):
  # +++ your code here +++
  return 

# D. summly
# Given a list of numbers, return the sum.
# (Hint: Python has a built-in 'sum()' function.)
def summly(list):
  return # +++ your code here +++




############ Do not edit below this line. ##################

# The test() function is used in main() to print
# what each function returns versus what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls above functions with a mix of inputs.
def main():
  print 'iLike'
  test(iLike('English'), "I like English")
  test(iLike('Art'), "I like Art")
  test(iLike('Chemistry'), "I like Chemistry")
  test(iLike('Food... Science'), "I like Food... Science")

  print
  print 'isLadida'
  test(isLadida('Ob la di'), False)
  test(isLadida('Ob la da'), False)
  test(isLadida('La di da'), True)

  print
  print 'donuts'
  test(donuts(2), 'Number of donuts: 2')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(20), 'Number of donuts: many')

  print
  print 'summly'
  test(summly([0,0,0]), 0)
  test(summly([1,2,2]), 5)
  test(summly([100,50.1,5]), 155.1)
  test(summly([-5,-2,3]), -4)




if __name__ == '__main__':
  main()
