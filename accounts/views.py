from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout

# Create your views here.
def login_view(request):
    form = AuthenticationForm(request,request.POST or None)
    
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('profile')
    
    return render(request, 'accounts/auth.html',{
        'form':form,
        'title':'Login',
        'btn_label':'Login',
    })
    
def logout_view(request):    
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'accounts/auth.html',{
        'form':None,
        'title':'Logout',
        'btn_label':'Logout',
        'description':'Are you sure you want to logout ?',
    })
    
def register_view(request):
    form = UserCreationForm(request.POST or None)
    
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/auth.html',{
        'form':form,
        'title':'register',
        'btn_label':'register',
    })