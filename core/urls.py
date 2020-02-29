from django.urls import path
from core import views

urlpatterns = [
    path('', views.ssignup, name='decider '),
    path('admin/pages', views.admins, name = 'admins'),
    path('signup/decide', views.ssignup, name = 'decider'),
    path('user/home', views.users_page, name = 'user_home'),
    path('callscreen/<int:pk>',views.incoming, name = 'incoming' ),
]
