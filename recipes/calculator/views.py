from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def get_recipe(request, name):
    servings = 1
    if 'servings' in request.GET:
        try:
            servings = int(request.GET.get('servings'))
        except:
            pass
    pass
    cur_data = DATA.get(name).copy()
    for x in cur_data:
        cur_data[x] *= servings
    context = {
        'recipe': cur_data,
        'servings': servings
    }
    return render(request, 'calculator/index.html', context)



def omlet(request):
    return get_recipe(request, 'omlet')

def pasta(request):
    return get_recipe(request, 'pasta')

def buter(request):
    return get_recipe(request, 'buter')
