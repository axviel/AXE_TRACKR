from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        # Show error
        # todo implement error message
        return redirect('register')
      else:
        # Check email
        if User.objects.filter(email=email).exists():
          # Show error
          # todo implement error message
          return redirect('register')
        else:
          # Create the user
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          user.save()
          # Show success 
          # todo implement success message
          return redirect('login')
    else:
      # Show error
      # todo implement error message
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    # Get fields
    username = request.POST['username']
    password = request.POST['password']

    # Validate
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      # Login user
      auth.login(request, user)
      # Show success 
      # todo implement success message
      return redirect('dashboard')
    else:
      # Show error
      # todo implement error message
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    # Show success 
    # todo implement success message
    return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')