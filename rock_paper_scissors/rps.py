#!/usr/bin/python

import sys

def rock_paper_scissors_helper(array, n=0):
	
	if len(array) == 0:
		return [[]] 
	else:
		game_array = []
		previous_combos = rock_paper_scissors_helper(array[n:], n+1)
		print('previous combos', previous_combos)
		if len(previous_combos[0]) == 3:
			return previous_combos
		for combo in previous_combos:
			for choices in array:
				game_array.append([choices] + combo)

	return game_array

def rock_paper_scissors(n):
  
  choices = [['rock'],['paper'],['scissors']]
  # base case for 0
  if n == 0:
    return [[]]
  if n == 1:
    return choices 
  for i in range(0, n):
    rock_list = [['rock'] + item for item in choices]
    paper_list = [['paper'] + item for item in choices]
    scissor_list = [['scissors'] + item for item in choices]
  
  return rock_list + paper_list + scissor_list

print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')