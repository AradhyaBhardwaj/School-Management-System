# from channels.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def loginPage(request):
    return render(request, 'login.html')



def doLogin(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(['POST'])

    user = authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        user_type = user.user_type
        if user_type == '1':
            return redirect('admin_home')
        elif user_type == '2':
            return redirect('staff_home')
        elif user_type == '3':
            return redirect('student_home')

    messages.error(request, "Invalid login credentials. Please check your email and password.")
    return redirect('login')



def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


