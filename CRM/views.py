from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

next_redirect = ''

def login_view(request):
    global next_redirect
    if request.method == 'GET' and request.GET.get('next', 'None') != 'None':
        next_redirect = request.GET['next']
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_redirect)
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect('/login/')