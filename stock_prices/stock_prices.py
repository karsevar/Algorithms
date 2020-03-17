#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # run a loop that will find the minimum profit price in the array 
  # save the value and the index position in a variable 

  # loop through the array again starting at the minimum price index and return
  # the maximum price for the time period 

  # if the minimum price is at the last index

  # minus the different between the two prices.

  profit = float('-inf')

  for index_i in range(len(prices)):
    for index_j in range(index_i+1, len(prices)):
      profit_amount = prices[index_j] - prices[index_i] 
      if profit < profit_amount:
        profit = profit_amount

  return profit


print(find_max_profit([10, 7, 5, 8, 11, 9]))
print(find_max_profit([100, 90, 80, 50, 20, 10]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))