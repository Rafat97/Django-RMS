"""rmscore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User, Group
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from restaurantapp.views import (
    RestaurantSet,
    ItemSet,
    MenuSet
)
from emailauth.views import EmailTokenObtainPairView,LogoutView
import employapp


schema_view = get_schema_view(
    openapi.Info(
        title="RMS API",
        default_version='v1',
        description=f"""Company needs internal service for its’ employees which helps them to make a decision
        on lunch place. Each restaurant will be uploading menus using the system every day
        over API and employees will vote for the menu before leaving for lunch.""",
    ),
    public=True,
)

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'restaurant', RestaurantSet)
router.register(r'menu', MenuSet)
router.register(r'item', ItemSet)

admin.site.site_header = "RMS Admin"
admin.site.site_title = "RMS Admin Portal"
admin.site.index_title = "Welcome to RMS Admin Portal"


urlpatterns = [
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),

    path('doc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),



    path('api/v1/token/', EmailTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/token/logout/', LogoutView.as_view(), name='token_logout'),

    path('api/v1/', include(router.urls)),
    path('api/v1/', include('restaurantapp.urls')),
    path('api/v1/employ/', include('employapp.urls')),
    path('api/v1/vote/', include('votingapp.urls')),



    # path('rest-auth/', include('rest_auth.urls')),
    # path('auth/registration/', include('rest_auth.registration.urls')),
    # path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
