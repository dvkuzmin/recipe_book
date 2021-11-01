from django.http import HttpResponse
from django.shortcuts import render

from .models import Category, Dish, Ingredient, WeightOfIngredient, AmountOfIngredient

menu = [
    {'title': 'Главная', 'url_name': 'recipe:index'},
    {'title': 'Категории блюд', 'url_name': 'recipe:categories'},
    {'title': 'Все блюда', 'url_name': 'recipe:dishes'},
    {'title': 'Все ингредиенты', 'url_name': 'recipe:ingredients'},
]


def index(request):
    """Функция отображения главной страницы"""
    # context = {'title': 'Главная страница', 'menu': menu}
    query = request.GET.get('q')
    if query:
        dish = Dish.objects.filter(name__istartswith=query)
        ingredient = Ingredient.objects.filter(name__istartswith=query)
        if dish or ingredient:
            context = {'title': 'Результаты поиска', 'menu': menu, 'dish': dish, 'ingredient': ingredient}
            return render(request, 'recipe/index.html', context)
    context = {'title': 'Главная страница', 'menu': menu}
    return render(request, 'recipe/index.html', context)

def categories(request):
    """Функция отображения категорий"""
    category_list = Category.objects.all()
    context = {'title': 'Категории', 'menu': menu, 'category_list': category_list}
    return render(request, 'recipe/categories.html', context)


def dish_detail(request, dish_id):
    """Функция отображения блюда"""
    dish = Dish.objects.get(pk=dish_id)
    context = {'title': dish.name, 'menu': menu, 'dish': dish}
    return render(request, 'recipe/dish_detail.html', context)


def dishes(request):
    """Функция отображения всех блюд"""
    dish_list = Dish.objects.all()
    context = {'title': 'Блюда', 'menu': menu, 'dish_list': dish_list}
    return render(request, 'recipe/dishes.html', context)


def ingredients(request):
    """Функция отображения ингредиентов"""
    ingredient_list = Ingredient.objects.all()
    context = {'title': 'Ингредиенты', 'menu': menu, 'ingredient_list': ingredient_list}
    return render(request, 'recipe/ingredients.html', context)


def category_detail(request, category_id):
    """Функция отображения отдельной категории"""
    category = Category.objects.get(pk=category_id)
    context = {'title': category.name, 'menu': menu, 'category': category}
    return render(request, 'recipe/category_detail.html', context)


def ingredient_detail(request, ingredient_id):
    """Функция отображения ингредиентов"""
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    context = {'title': 'Ингредиенты', 'menu': menu, 'ingredient': ingredient}
    return render(request, 'recipe/ingredient_detail.html', context)