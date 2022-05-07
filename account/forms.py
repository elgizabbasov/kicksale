from django import forms
from .models import UserBase

class UserRegistrationForm(forms.Form):
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=100, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)
