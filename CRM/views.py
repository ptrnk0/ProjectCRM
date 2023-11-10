from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponse
import json


def my_view(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/client/insert_client/')
    return render(request, 'login.html', {})