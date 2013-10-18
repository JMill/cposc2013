#!/usr/bin/python -tt
# Copyright 2013 Jonathan B. Miller

# 'A Gentle Guide to Python', by Jonathan B. Miller, for LASTS 2013
# https://bitbucket.org/JMill/lasts2013py

# Basic string and integer exercises
# Fill in the code for the functions below. 
# The starter code for each function includes a 'return'
# which is merely a placeholder for your code.
# It's okay if you do not complete every part of this exercise. 
# When you run this script, 'OK' will be printed when each function
# is correct.


# A. add2plus2
# This is a 'function'. When someone writes add2plus2(), we want it to 'return' a 4. 
# Just add a tiny bit of code after the 'return' statement below.
def add2plus2():
  return # +++ your code here +++

# B. weArePSU
# If someone calls weArePSU(), we want it to return "PSU".
def weArePSU():
  return # +++ your code here +++

# C. lasts
# Return a sentence that says "This is LASTS 2013"
def lasts():
  return # +++ your code here +++

# D. aBigWhat
# Penn State is a Big ____ school. Calculate and return the 
# number as the product (multiplication) of at least 2 
# other numbers. 
def aBigWhat():
  return # +++ your code here +++

# E. givingBack
# This function receives an input that we'll call 'whatever'. 
# Write the function to 'return' what was given to it.
def givingBack(whatever):
  return # +++ your code here +++

# F. givingBackMore
# Similar 'givingBack()' above, givingBackMore receives input called
# 'word'. Make the function return two 'word's (whatever the word is).
# (Hint: you can multiply words by two by writing'* 2'.)
def givingBackMore(word):
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
  print 'add2plus2'
  test(add2plus2(), 4)

  print
  print 'weArePSU'
  test(weArePSU(), "PSU")

  print
  print 'lasts'
  test(lasts(), "This is LASTS 2013")

  print
  print 'aBigWhat'
  test(aBigWhat(), 10)

  print
  print 'givingBack'
  test(givingBack('lion'), 'lion')
  test(givingBack('lady lion'), 'lady lion')

  print
  print 'givingBackMore'
  test(givingBackMore('cha'), 'chacha')
  test(givingBackMore('repeat'), 'repeatrepeat')



if __name__ == '__main__':
  main()
