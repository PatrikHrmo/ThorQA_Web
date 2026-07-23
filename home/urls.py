from django.urls import path
from . views import home_view

app_name = "home"

urlpatterns = [
    path('home/', home_view, name='home'),
]