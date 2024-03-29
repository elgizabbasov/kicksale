from django.shortcuts import redirect, render
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import UserBase
from .forms import UserRegistrationForm, UserEditDetailsForm
from .token import account_activation_token
from orders.views import user_orders


@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(request, 'account/user/dashboard.html', {'orders': orders})

@login_required
def change_details(request):
    if request.method == 'POST':
        user_form = UserEditDetailsForm(instance=request.user, data=request.POST)
        
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditDetailsForm(instance=request.user)
        
    return render(request, 'account/user/change_details.html', {'form': user_form})

@login_required
def account_delete(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False # :)
    user.save()
    logout(request)
    return redirect('account:delete_profile') # Confirm account deletion

def account_register(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')
    
    if request.method == 'POST':
        userRegForm = UserRegistrationForm(request.POST)
        if userRegForm.is_valid():
            cd = userRegForm.cleaned_data
            
            user = UserBase(
                user_name = cd['user_name'],
                email = cd['email'],
                is_active = False
            )
            
            user.set_password(cd['password'])
            user.save()
            
            # Setup email
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('account/registration/activation_email.html', {
                'user': user, 
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return render(request, 'account/registration/register_confirm.html', {'form': userRegForm})
    else:
        userRegForm = UserRegistrationForm()
    
    return render(request, 'account/registration/register.html', {'form': userRegForm})

def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')
