from django.urls import path
from .views import home_page, success_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('success/', success_page, name='success_page')
]