from django.contrib import admin

from . models import Category, Dish, Ingredient, WeightOfIngredient, AmountOfIngredient

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(WeightOfIngredient)
admin.site.register(AmountOfIngredient)