from django.contrib import admin
from .models import Restaurant,Menu,Item

# Register your models here.
@admin.register(Restaurant)
class AdminRestaurant(admin.ModelAdmin):
    pass

@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'is_active', )
    pass

@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ('id', 'menu', 'is_available', )
    pass