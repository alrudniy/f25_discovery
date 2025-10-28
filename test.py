import os
import shutil

# Function to create directories and files
def create_project_structure():
    project_name = 'discovery_hub'
    app_name = 'core'
    
    # Create main project directory if it doesn't exist
    if os.path.exists(project_name):
        shutil.rmtree(project_name)  # Clean up if exists (for re-running)
    os.mkdir(project_name)
    os.chdir(project_name)
    
    # Create Django project
    os.system('django-admin startproject config .')
    os.system(f'python manage.py startapp {app_name}')
    
    # Create templates and static directories
    templates_dir = os.path.join(app_name, 'templates')
    os.mkdir(templates_dir)
    static_dir = os.path.join(app_name, 'static')
    os.mkdir(static_dir)
    
    # Write basic HTML templates
    login_html = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
    <a href="{% url 'register' %}">Register</a> | <a href="{% url 'forgot_password' %}">Forgot Password?</a>
</body>
</html>
"""
    with open(os.path.join(templates_dir, 'login.html'), 'w') as f:
        f.write(login_html)
    
    register_html = """
<!DOCTYPE html>
<html>
<head><title>Register</title></head>
<body>
    <h2>Register</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
    <a href="{% url 'login' %}">Already have an account? Login</a>
</body>
</html>
"""
    with open(os.path.join(templates_dir, 'register.html'), 'w') as f:
        f.write(register_html)
    
    forgot_html = """
<!DOCTYPE html>
<html>
<head><title>Forgot Password</title></head>
<body>
    <h2>Forgot Password</h2>
    <form method="post">
        {% csrf_token %}
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <button type="submit">Reset Password</button>
    </form>
</body>
</html>
"""
    with open(os.path.join(templates_dir, 'forgot_password.html'), 'w') as f:
        f.write(forgot_html)
    
    # Write views.py
    views_content = """
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import PasswordResetView

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard')  # TODO: Implement dashboard
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

class ForgotPasswordView(PasswordResetView):
    template_name = 'forgot_password.html'
    email_template_name = 'password_reset_email.html'  # TODO: Create this template
    success_url = '/login/'  # Redirect after submission
"""
    with open(os.path.join(app_name, 'views.py'), 'w') as f:
        f.write(views_content)
    
    # Write urls.py for the app
    urls_content = """
from django.urls import path
from .views import register, login, ForgotPasswordView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
]
"""
    with open(os.path.join(app_name, 'urls.py'), 'w') as f:
        f.write(urls_content)
    
    # Update config/urls.py to include app urls
    main_urls_path = os.path.join('config', 'urls.py')
    with open(main_urls_path, 'r') as f:
        content = f.read()
    content = content.replace(
        'urlpatterns = [',
        f'from django.contrib import admin\nfrom django.urls import path, include\n\nurlpatterns = [\n    path(\'admin/\', admin.site.urls),\n    path(\'\', include(\'{app_name}.urls\')),\n'
    )
    with open(main_urls_path, 'w') as f:
        f.write(content)
    
    # Update settings.py for templates and installed apps
    settings_path = os.path.join('config', 'settings.py')
    with open(settings_path, 'r') as f:
        content = f.read()
    content = content.replace(
        'INSTALLED_APPS = [',
        f'INSTALLED_APPS = [\n    \'{app_name}\','
    )
    content = content.replace(
        "'DIRS': [],",
        f"'DIRS': [os.path.join(BASE_DIR, '{app_name}', 'templates')],"
    )
    with open(settings_path, 'w') as f:
        f.write(content)
    
    print(f"Project structure created in '{project_name}'. Run 'python manage.py migrate' and 'python manage.py runserver' to start.")

if __name__ == '__main__':
    create_project_structure()

