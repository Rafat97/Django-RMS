from django.urls import path, include
from .views import get_restaurant_menu

urlpatterns = [
    # path('create/', add_employ,name='creating-employ'),
    path('restaurant-today/', get_restaurant_menu ,name='restaurant-today-menu'),
]
