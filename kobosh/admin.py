from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Category, Product,PaymentUser
# from .models import PaymentUser
from django.contrib.auth.admin import UserAdmin

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



class CustomUserAdmin(UserAdmin):
    model = PaymentUser
    list_display = ('email', 'full_name', 'is_staff', 'phone_number', 'address', 'city', 'state', 'zip_code',  )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'full_name')
    ordering = ('email',)

# Register the CustomUserAdmin with the admin site
admin.site.register(PaymentUser, CustomUserAdmin)