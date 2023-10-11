from django.shortcuts import render, redirect
from .forms import BigtreeForm
from .models import Link
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def link_view(request,username):
    user = User.objects.filter(username = username).first()
    user_links = Link.objects.filter(user=user)
    return render(request, 'dashboard.html',{
        'user':user,
        'links':user_links
    })
    
    
@login_required    
def dashboard(request):
    form = BigtreeForm(request.POST or None)
    link = Link.objects.filter(user=request.user)
    if form.is_valid():
        form_obj = form.save(commit=False)
        form_obj.user = request.user
        form_obj.save()
        return redirect('Dashboard')
    return render(request,'links/real_dashboard.html',{
        'links':link,
        'form':form
    })
    
@login_required
def edit_link_view(request, id):
    instance =  Link.objects.get(id=id)
    form = BigtreeForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('Dashboard')
    return render(request, 'links/edit.html',{
        'form':form,
        
    })
    
@login_required
def delete_link_view(request, id):
    if request.method == 'POST':
        Link.objects.get(id=id).delete()
        return redirect('Dashboard')
    return render(request, 'links/delete.html')
        