from django.contrib import admin
from .models import iris

# admin.site.register(iris)
# Register your models here.

@admin.register(iris)
class IrisAdmin(admin.ModelAdmin):
    list_display = ('sepal_length', 'sepal_width', 'petal_length', 'petal_width','get_species')
    fields = [('sepal_length', 'sepal_width'),('petal_length', 'petal_width'),'species']

    def get_species(self,obj):
        return obj.get_species_display()
    get_species.short_description = "Species"