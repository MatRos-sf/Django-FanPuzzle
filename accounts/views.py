from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForms, CreateUserForm
from django.contrib import messages

# Create your views here.
#https://stackoverflow.com/questions/65951430/django-login-says-invalid-password-even-for-correct-login-credential-even-though
def login_view(request):
    forms = LoginForms()
    if request.method == 'POST':
        forms = LoginForms(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            username = cd['email']
            password = cd['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                #return HttpResponse("<h1>Something wrong!</h1>")
                messages.error(request,  "Email or password is incorrect")

    else:
        return render(request, 'accounts/login.html', {'forms': forms})
    return render(request, 'accounts/login.html', {'forms': forms})



def logout_view(request):
    print(request)
    logout(request)
    return HttpResponse("<h1>Zostałeś wylogowany</h1>")

def create_user(request):
    #zrobić warunek zalogowany użytkownik nie może zakładać konta
    if request.method == 'POST':
        forms = CreateUserForm(request.POST)
        if forms.is_valid():
            new_user = forms.save(commit=False)
            new_user.set_password(
                forms.cleaned_data['password']
            )
            new_user.save()
            login(request, new_user)
            return redirect('home')
    else:
        forms = CreateUserForm()
        return render(request, "accounts/register.html", {"forms": forms})

