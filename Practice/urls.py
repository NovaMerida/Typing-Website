from django.urls import path
from . import views
app_name = "Practice"
urlpatterns = [
    path('', views.practice, name='Practice'),
]