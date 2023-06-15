from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'new_price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['new_price', 'available']
    prepopulated_fields = {'slug' : ('name', )}