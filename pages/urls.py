from django.urls import path
from . import views
from .buggy_views import buggy_search # Import the buggy view

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('screen1/', views.screen1, name='screen1'),
    path('screen2/', views.screen2, name='screen2'),
    path('screen3/', views.screen3, name='screen3'),
    path('buggy_search/', buggy_search, name='buggy_search'), # Add the URL pattern for the buggy view
]
