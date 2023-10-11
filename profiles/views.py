from django.shortcuts import render,redirect
from .forms import Profile_page_Form
from django.contrib.auth.decorators import login_required 
from .models import Profile

# Create your views here.
@login_required
def profile_page_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    initial_data = {'image_url':profile.image_url}
    form = Profile_page_Form(request.POST or None,instance=user, initial=initial_data)
    if form.is_valid():
        image_url = form.cleaned_data.get('image_url')
        profile = Profile.objects.get(user = user)
        profile.image_url = image_url
        profile.save()
        form.save()
        return redirect('profile')
    return render(request,'profiles/profile.html',{
        'form':form,
        'btn_label':'Update'
    })
        
