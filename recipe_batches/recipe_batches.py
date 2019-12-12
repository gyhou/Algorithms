#!/usr/bin/python


def recipe_batches(recipe, ingredients):
    i_key = list(recipe)[0]
    min_batch = ingredients[i_key]//recipe[i_key]
    for key in recipe:
        if key not in ingredients:
            return 0
        temp_batch = ingredients[key]//recipe[key]
        if temp_batch < min_batch:
            min_batch = temp_batch
    return min_batch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
