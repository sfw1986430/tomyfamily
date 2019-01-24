from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
# from .forms import RegisterForm
# from .models import User

# Create your views here.

# def SignUpView(request):
#     if request.method == "POST":
#         register_form = RegisterForm(data=request.POST)
#         if register_form.is_valid():
#             new_user = register_form.save(commit=False)
#             new_user.set_password(register_form.cleaned_data['password'])
#             new_user.save()
#             return redirect(reverse('login'))
#     else:
#         register_form = RegisterForm()
#     return render(request, 'blog/signup.html', context={'form':register_form})
            
def SignUpView(request):
    if request.method == "POST":
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            return redirect(reverse('login'))
    else:
        register_form = UserCreationForm()

    return render(request, 'blog/signup.html', context={'form': register_form})

            