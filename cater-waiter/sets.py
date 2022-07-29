from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            return f'{drink_name} Cocktail'

    return f'{drink_name} Mocktail'


def categorize_dish(dish_name, dish_ingredients):
    for category, category_name in zip(
        (VEGAN, VEGETARIAN, KETO, PALEO, OMNIVORE),
        ('VEGAN', 'VEGETARIAN', 'KETO', 'PALEO', 'OMNIVORE')):

        if all(ingredient in category for ingredient in dish_ingredients):
            return f'{dish_name}: {category_name}'

    return 'Error'


def tag_special_ingredients(dish):
    return (dish[0], set(ingredient for ingredient in dish[1] if ingredient in SPECIAL_INGREDIENTS))


def compile_ingredients(dishes):
    shopping_list = set()
    for ingredients in dishes:
        shopping_list.update(ingredients)

    return shopping_list


def separate_appetizers(dishes, appetizers):
    return list(set(dishes).difference(appetizers))


def singleton_ingredients(dishes, intersection):
    result = set()
    for dish in dishes:
        result.update(dish.difference(intersection))

    return result
