from django.contrib import admin
from .models import *


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category


admin.site.register(Category, ProductTypeAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    list_display_links = ('name',)  # Клік по полю для редагування
    search_fields = ["name"]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
