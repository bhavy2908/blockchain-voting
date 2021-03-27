from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        voter_id = request.POST['voter']
        password = request.POST['password']

        user = auth.authenticate(username=voter_id, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/voting/vote')
        else:
            messages.info(request, 'Invalid credentials.')
            return redirect('/')
    else:
        return render(request, 'login/login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        voter = request.POST['voter']
        password = request.POST['password']
        password_c = request.POST['password_repeat']

        if password == password_c:
            if User.objects.filter(username=voter).exists():
                messages.info(request, "User already exists.")
                return redirect('/')
            user = User.objects.create_user(
                email=voter, password=password, first_name=name, last_name=name, username=voter)
            user.save()
            messages.info(request, 'User created succesfully.')
            return redirect('/')

        else:
            messages.info(request, 'Passwords don\'t match')
            return redirect('/register')
    else:
        return render(request, 'login/register.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, 'logged out sucessfully.')
        return redirect('/logout')
    return redirect('/')
