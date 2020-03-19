#!/usr/bin/python

import sys

def making_change(amount, denominations, currentCoin=0):
  # base case:
  # if amount == 0 return 1
  # if amount < 0 return 0 
  
  # recursive case:
  # variable that holds number of combos 
  # loop that loops through the denominations array and 
  # recursively subtracts the amount with the coin denomination
  # within the recursive call 
  if amount == 0:
    return 1
  if amount < 0:
    return 0 

  nCombos = 0
  
  for coin in range(currentCoin, len(denominations)):
    # print('current coin', coin)
    new_amount = amount - denominations[coin]
    nCombos += making_change(new_amount, denominations, coin)

  return nCombos 

print(making_change(350,[1, 5, 10, 25, 50],0))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")