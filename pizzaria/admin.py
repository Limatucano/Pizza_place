from pizzaria.forms import PizzaForm
from pizzaria.models import Ingredient, Pizza, IngredientPizza
from django.contrib import admin


# TabularInline
# class PizzaInLine(admin.TabularInline):
#     model  = Pizza
#     extra  = 0

# class IngredientInLine(admin.TabularInline):
#     model  = Ingredient
#     extra  = 0

class IngredientPizzaInLine(admin.TabularInline):
    model  = IngredientPizza
    extra  = 0

# Amin Page
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display  = ('name','get_ingredients','portion','price')
    search_fields = ['name','portion','price']
    inlines       = [IngredientPizzaInLine]
    
    form          = PizzaForm

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display  = ('name',)
    inlines       = [IngredientPizzaInLine]
    
