
from django.contrib import admin
from django.urls import path, include
from services.api.urls import router
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import dashboard




urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(router.urls)),
]
