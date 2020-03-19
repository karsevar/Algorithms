#!/usr/bin/python

import sys

# create a helper function that can keep track of the 
# number of combinations and contain the current combination array 
# that will return when containing the right number of combinations specified by 
# n.

def rock_paper_scissors_helper(array, n=0, total_combinations=[], current_combinations=[]):
	
	# base case if current_combinations == n: return current_combinations 

  # recursive case: 
  # loop through the array (of rock paper scissors plays)
  # recursively call the rock_paper_scissors_helper function 
  # append the current_combinations array to total_combinations 
  # return total_combinations
  print(current_combinations)
  if n == 0:
    return [[]]

  if len(current_combinations) == n:
    total_combinations.append(current_combinations)
  else:
    for choice in range(len(array)):
      new_combination = current_combinations[:]
      new_combination.append(array[choice]) 
      rock_paper_scissors_helper(array, n, total_combinations, new_combination)

  return total_combinations

print(rock_paper_scissors_helper(['rock','paper','scissors'], n=3))
	




def rock_paper_scissors(n):
  total_combinations = []
  
  choices = ['rock','paper','scissors']
  total_combinations = rock_paper_scissors_helper(choices, n, total_combinations)
  
  
  return total_combinations

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')