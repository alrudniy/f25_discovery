from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.university_home, name='university_home'),
    path('profile/', views.university_profile, name='university_profile'),        # optional
    path('dashboard/', views.university_dashboard, name='university_dashboard'),  # optional
]
