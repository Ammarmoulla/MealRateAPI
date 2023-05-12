from django.contrib import admin
from django.urls import path, include
from .views import MealViewset, RatingViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()
router.register('meals', MealViewset)
router.register('ratings', RatingViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),
    path('api-auth-token', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
