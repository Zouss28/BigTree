from django import forms
from .models import Link

class BigtreeForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('title','link')