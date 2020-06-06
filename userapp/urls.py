from django.urls import path

from .views import *
app_name = 'userapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/',RegisterView.as_view(),name = 'register'),
    path('admin/login', AdminView.as_view(), name='adminhome'),
    path('admin/predict', AdminPredictView.as_view(), name='adminpredicthome'),


    
]
