from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def university_home(request):
    """
    Homepage for university users.
    Only accessible to logged-in university accounts.
    """
    user = request.user  # Get the currently logged-in user
    context = {
        'user': user,
    }
    return render(request, 'universityAccounts/home.html', context)
