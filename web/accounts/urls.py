from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('logout/', views.logout, name='logout'),
    path('mypage/', views.mypage, name='mypage'),
    path('select/', views.change_food, name='change_food'),
    
]
