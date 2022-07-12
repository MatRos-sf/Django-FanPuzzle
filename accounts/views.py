from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import LoginForms, CreateUserForm
from django.contrib import messages
from .models import Account

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
                #next/
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('home')
            else:
                #return HttpResponse("<h1>Something wrong!</h1>")
                messages.error(request,  "Email or password is incorrect")
            #next
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))

    else:
        return render(request, 'accounts/login.html', {'forms': forms})
    return render(request, 'accounts/login.html', {'forms': forms})



def logout_view(request):

    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return render(request, 'accounts/simple_template.html', {
            'title': 'Logout',
            'commo': "You can't logout if you aren't login!"
        })

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
            print("something wrong")
    else:
        forms = CreateUserForm()
        return render(request, "accounts/register.html", {"forms": forms})
    return render(request, "accounts/register.html", {"forms": forms})

from .filters import UserFilter
@login_required(login_url='/account/login/')
def search_user(request):
    f = UserFilter(request.GET, queryset=Account.objects.all())
    return render(request, 'accounts/search.html', {'filter': f})

class UserDetail(DetailView):
    model = Account
    template_name = 'accounts/user_detail.html'
    context_object_name = 'user'



