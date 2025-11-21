from django.urls import path
from . import views
from . import buggy_view_fixed

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('screen1/', views.screen1, name='screen1'),
    path('screen2/', views.screen2, name='screen2'),
    path('screen3/', views.screen3, name='screen3'),
    path('notifications/', views.notifications, name='notifications'), # added for notifications page, 
    # URL for the Company Home Page (Dashboard)
    path('company/home/', views.company_home, name='company_home'),
    path('university/home/', views.university_home, name='university_home'),
    path('buggy/', buggy_view_fixed.buggy_search, name='buggy_search'),
]
