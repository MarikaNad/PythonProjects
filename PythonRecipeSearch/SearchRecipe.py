import requests


def recipe_search(ingredient):
    app_id = '1d372b70'
    app_key = 'ba06f0613ed360dd2e4bde7b762660a6'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))

    data = result.json()
    return data['hits']


recipe_list = []

def get_recipe():
    ingredient = input('Please enter an ingredient : ')

    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']

        print(recipe['label'])
        recipe_list.append('Name: ' + recipe['label'] + '\n')


        print(recipe['uri'])
        recipe_list.append('Link: ' + recipe['uri'] + '\n')


        for type_of_dish in recipe['dishType']:
            print(type_of_dish)
            recipe_list.append('Dish Type: ' + type_of_dish + '\n')

        print('Ingredients:\n')
        recipe_list.append('Ingredients:\n')

        for ingr in recipe['ingredients']:
            print(ingr['text'])
            recipe_list.append(ingr['text'] + '\n')

        print()


    with open('recipe_book.txt', 'w+') as file:
        file.writelines(recipe_list)

get_recipe()