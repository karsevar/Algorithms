#!/usr/bin/python

import argparse

def find_max_profit(prices):

  # checking if the list is in descending order:
  flag = 0
  index = 0 

  if sorted(prices, reverse=True) == prices:

  	return -min(prices)



  k = 0 # array index
  high_index = 0

  highest = 0 
  lowest = max(prices) 

  while k <= len(prices)-1:

    if lowest > prices[k] and k != len(prices)-1:

      lowest = prices[k]

      high_index = k

      while high_index <= len(prices)-1:

      	if highest < prices[high_index]:
      		highest = prices[high_index]
      	
      	high_index += 1

    k += 1

    print('lowest', lowest )
    print('highest', highest)
    

  return highest - lowest
  # find the minimum buying price 

  # find the maximum selling price 

  # constraint the algorithm will have to use a buying price that happens before 
  # the highest selling price 


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))