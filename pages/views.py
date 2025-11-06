from django.shortcuts import render, redirect # Add redirect for unauthorized access
from django.contrib.auth.decorators import login_required
from accounts.models import User # Import User model to check user_type


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
def company_home(request):
    # Restrict access to only company users
    if request.user.user_type != User.UserType.COMPANY:
        return redirect('welcome') # Redirect if not a company user

    # Placeholder for Project objects.
    # In a real application, you would import and query your Project model here.
    all_projects = [
        {'id': 1, 'title': 'AI-Powered Chatbot for Customer Service', 'field': 'Artificial Intelligence', 'description': 'Developing a chatbot using natural language processing to enhance customer support experience.'},
        {'id': 2, 'title': 'Sustainable Energy Management System', 'field': 'Renewable Energy', 'description': 'A system to monitor and optimize energy consumption for commercial buildings using IoT.'},
        {'id': 3, 'title': 'Blockchain for Supply Chain Traceability', 'field': 'Blockchain', 'description': 'Implementing a decentralized ledger to track products from origin to consumer.'},
        {'id': 4, 'title': 'Personalized Learning Platform', 'field': 'Education Technology', 'description': 'An adaptive platform that customizes learning paths based on student performance and preferences.'},
        {'id': 5, 'title': 'Predictive Maintenance for Industrial Machinery', 'field': 'Manufacturing', 'description': 'Using machine learning to predict equipment failures and optimize maintenance schedules.'},
        {'id': 6, 'title': 'Smart City Traffic Management', 'field': 'Urban Planning', 'description': 'Developing an intelligent system to alleviate traffic congestion using real-time data.'},
    ]

    projects = all_projects
    query = request.GET.get('q')
    field_filter = request.GET.get('field')

    if query:
        projects = [p for p in projects if query.lower() in p['title'].lower() or query.lower() in p['description'].lower()]
    if field_filter and field_filter != 'All':
        projects = [p for p in projects if p['field'] == field_filter]

    # Get all unique fields for the filter dropdown
    available_fields = sorted(list(set([p['field'] for p in all_projects])))
    available_fields.insert(0, 'All') # Add 'All' option at the beginning

    context = {
        'projects': projects,
        'current_query': query if query else '',
        'current_field': field_filter if field_filter else 'All',
        'available_fields': available_fields,
    }
    return render(request, 'pages/company_home.html', context)
