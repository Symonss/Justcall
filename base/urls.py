from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/admin/', views.AdminSignUpView.as_view(), name='admin_signup'),
    path('accounts/signup/users/', views.UserSignUpView.as_view(), name='user_signup'),
]
