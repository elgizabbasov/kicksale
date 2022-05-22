from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from .models import UserBase


class UserRegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=100, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Register', css_class='btn-primary'))
        self.helper.form_method = 'POST'
    
    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)
        
    def clean_user_name(self):
        user_name = self.cleaned_data['user_name'].lower()
        n = UserBase.objects.filter(user_name=user_name)
        if n.count():
            raise forms.ValidationError(f"Please use another username, {user_name} is already taken")
        return user_name
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords dont match")
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        e = UserBase.objects.filter(email=email)
        if e.exists():
            raise forms.ValidationError(f"Please use another email, {email} has already been used")
        return email
    

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'login-password'}))


class UserEditDetailsForm(forms.ModelForm):
    user_name = forms.CharField(label='Username', min_length=4, max_length=100, help_text='Required')
    email = forms.EmailField(label='Email', max_length=200, help_text='You are not allowed to change your email address', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    first_name = forms.CharField(label='First Name', max_length=255)
    
    class Meta:
        model = UserBase
        fields = ('user_name', 'email', 'first_name',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save', css_class='btn-primary'))
        self.fields['user_name'].required = True
        self.fields['email'].required = True
