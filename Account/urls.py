from django.urls import path
from . import views
app_name = "Account"
urlpatterns = [
    path('Create', views.AccountCreateView, name='AccountCreate'),
    path('Login', views.AccountLoginView, name='AccountLogin'),
    path('Account', views.AccountUpdateView, name='Account'),
]