#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # looking through the tests it seems that the recipe and ingredients dictionaries all 
  # have similar keys thus meaning that this algorithm can be completed with only one 
  # loop 

  # create a new dictionary that will keep track of the number of batches each ingredient 
  # can make. batches = {}

  # loop through the recipe dictionary with a for in loop 
  #   if ingredients[key] < recipe[key] return 0 
  #   else:
  #     batches[key] = ingredients[key] // recipe[key]

  batches = {}

  for key in recipe:
    if key not in ingredients:
      return 0
    elif ingredients[key] < recipe[key]:
      return 0 
    else:
      batches[key] = ingredients[key] // recipe[key]

  # loop through the batches dictionary and find the smallest number of batches 
  minimum_batches = float('inf') 

  for key in batches:
    if minimum_batches > batches[key]:
      minimum_batches = batches[key]

  return minimum_batches

print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))
print(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 }))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))