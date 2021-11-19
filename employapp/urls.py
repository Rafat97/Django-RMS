from django.urls import path, include
from .views import EmployAddView
# EmployApiView,
urlpatterns = [
    # path('create/', add_employ,name='creating-employ'),
    path('create/', EmployAddView.as_view(), name='showing-employ'),
]
