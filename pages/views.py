from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request, 'pages/welcome.html')

@login_required
def screen1(request):
    role = request.user.user_type.title() if hasattr(request.user, 'user_type') else 'User'
    return render(request, 'pages/screen1.html', {'role': role})

@login_required
def screen2(request):
    role = request.user.user_type.title() if hasattr(request.user, 'user_type') else 'User'
    return render(request, 'pages/screen2.html', {'role': role})

@login_required
def screen3(request):
    role = request.user.user_type.title() if hasattr(request.user, 'user_type') else 'User'
    return render(request, 'pages/screen3.html', {'role': role})

@login_required
def notifications(request): # added for notifications page
    # This is dummy data for now.
    current_notifications = [
        "Your profile was updated.",
        "You have a new message from Admin.",
    ]
    previous_notifications = [
        "Your password was changed a week ago.",
        "Welcome to the platform!",
    ]
    context = {
        'current_notifications': current_notifications,
        'previous_notifications': previous_notifications,
    }
    return render(request, 'pages/notifications.html', context)
