"""
URL configuration for internship_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from core.views import health_check, login_view, logout_view, program_list, ProgramListCreateGenericAPIView, ProgramDetailGenericAPIView
from rest_framework.routers import DefaultRouter
from core.views import ProgramViewSet, ApplicationViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(
    r'programs-viewset',
    ProgramViewSet,
    basename='program-viewset'
)

router.register(
    r'applications',
    ApplicationViewSet,
    basename='application'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),
    path('login/', login_view),
    path('logout/', logout_view),
    path('programs/', program_list),
    path('api/programs/', ProgramListCreateGenericAPIView.as_view()),
    path('api/programs/<int:pk>/', ProgramDetailGenericAPIView.as_view()),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
    'api/token/',
    TokenObtainPairView.as_view(),
    name='token_obtain_pair',
    ),

    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh',
    ),
]