from django.urls import path
from .views import home, clothes, singUp

urlpatterns = [
    path('', home, name='home'),
    path('clothes/', clothes, name='clothes'),
    path('singUp/', singUp, name='singUp'),
]