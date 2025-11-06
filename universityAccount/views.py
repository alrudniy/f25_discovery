from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from accounts.models import User  # 👈 import your custom User model

@login_required
def university_home(request):
    if request.user.user_type != User.UserType.UNIVERSITY:
        return HttpResponseForbidden("Access denied")
    return render(request, 'universityAccount/home.html', {'user': request.user})
