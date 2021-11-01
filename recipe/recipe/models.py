from django.db import models


class Category(models.Model):
    """Категория блюда"""
    name = models.CharField(verbose_name='Название категории', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Dish(models.Model):
    """Название и описание рецепта блюда"""
    name = models.CharField(verbose_name='Название блюда', max_length=100)
    text = models.TextField(verbose_name='Рецепт', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Блюда'
        verbose_name = 'Блюдо'


class Ingredient(models.Model):
    """Название ингредиента"""
    name = models.CharField(verbose_name='Название ингредиента', max_length=100, null=True, blank=True)
    dish = models.ManyToManyField(Dish, verbose_name='Название блюда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Ингредиенты'
        verbose_name = 'Ингредиент'


class WeightOfIngredient(models.Model):
    """Вес ингредиента в граммах"""
    weight = models.FloatField(verbose_name='Вес в граммах', null=True, blank=True)
    ingredient = models.ForeignKey(Ingredient, verbose_name='Название ингредиента', on_delete=models.CASCADE, null=True, blank=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='Название блюда', null=True, blank=True)

    def __str__(self):
        return str(self.weight)

    class Meta:
        verbose_name_plural = 'Вес'
        verbose_name = 'Вес'


class AmountOfIngredient(models.Model):
    """Количество ингредиентов (штук)"""
    amount = models.IntegerField(verbose_name='Количество штук', null=True, blank=True)
    ingredient = models.ForeignKey(Ingredient, verbose_name='Название ингредиента', on_delete=models.CASCADE, null=True, blank=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='Название блюда',  null=True, blank=True)

    def __str__(self):
        return str(self.amount)

    class Meta:
        verbose_name_plural = 'Количество'
        verbose_name = 'Количество'




