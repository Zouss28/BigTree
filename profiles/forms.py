from django import forms
from django.contrib.auth.models import User

class Profile_page_Form(forms.ModelForm):
    image_url = forms.URLField(required=False)
    class Meta:
        model = User
        fields =  ['username', 'first_name', 'last_name', 'email', 'image_url']
        help_texts = {
            'username': None,
            'email': None,
        }