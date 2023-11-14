from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def login_view(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.POST['return_to'])
    context = {"return_to_value": request.GET.get('next', '/all_staff/')}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/login/')