from django.db import models

class Ingredient(models.Model):
    name         = models.CharField(max_length=50, verbose_name='ingrediente')

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name         = models.CharField(max_length=200, verbose_name='nome da pizza')
    
    ingredientes = models.ManyToManyField(Ingredient, through='IngredientPizza', through_fields=('pizza', 'ingredient'))
    description  = models.TextField(verbose_name='descrição', null=True, blank=True)
    portion      = models.IntegerField(verbose_name='fatias')
    price        = models.DecimalField(max_digits=10, verbose_name='preço',decimal_places=2)
    
    @property
    def get_ingredients(self):
        ingreds = IngredientPizza.objects.filter(pizza=self.id)
        return ' '.join([ i for i in ingreds ])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.name}"

class IngredientPizza(models.Model):
    pizza         = models.ForeignKey(Pizza, on_delete=models.PROTECT)
    ingredient    = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity     = models.DecimalField(max_digits=10, verbose_name='quantidade',decimal_places=2)
    measurem_unit = models.CharField(max_length=20, verbose_name='unidade de medida')
    
    class Meta:
        unique_together = ('ingredient','pizza')
    def __str__(self):
        return f"{self.ingredient} - {self.pizza}"
    
    # @property
    # def quantity(self):
    #     return f"{self._quantity} {self.measurem_unit}"
    
    # @quantity.setter
    # def set_quantity(self, _input):
    #     this_input = _input.strip().split()
    #     qty        = this_input[0]
    #     unit       = ' '.join(this_input[1:])
        
    #     self._quantity     = float(qty)
    #     self.measurem_unit = unit
