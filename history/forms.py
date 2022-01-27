from django import forms
from history.models import Profile

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['file']