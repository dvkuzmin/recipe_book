from django.urls import path

from . import views

app_name = 'recipe'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('<int:dish_id>/details/', views.dish_detail, name='dish_detail'),
    path('dishes/', views.dishes, name='dishes'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('<int:category_id>/category', views.category_detail, name='category_detail'),
    path('<int:ingredient_id>/ingredient_detail/', views.ingredient_detail, name='ingredient_detail'),
]