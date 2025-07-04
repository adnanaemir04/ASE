from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm

from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        auth_login(request,newUser)
        messages.success(request,"Başarıyla Kayıt Oldunuz.")

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)
    
    
    """form = RegisterForm()
    context = {
        "form" : form,
        
    }
    
    return render(request,"register.html",context)"""

def login(request):
    form = LoginForm(request.POST or None)
    
    context = {
        "form" : form
    }
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password= password)
        
        if user is None:
            messages.info(request,"Kullanıcı adı veya Parola hatalı...")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yaptınız!")
        auth_login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
        
@login_required
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")
