#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # base cases:
  # There is only one way to eat zero cookies
  # if n == 0:
  #   return 1 
  # There is only one way to eat one cookie
  # if n == 1:
  #   return 1
  # There are 2 total ways to eat 2 cookies: [1,1], [2]
  # if n == 2:
  #   return 2
  if cache != None and cache[n] != 0:
    return cache[n]
  if n == 0:
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  result = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
  if cache != None:
    cache[n] = result 
  # print('cache array', cache)
  return result

print(eating_cookies(50, [0 for i in range(51)]))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')