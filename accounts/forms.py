from django import forms
from .models import Account
class LoginForms(forms.Form):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}
    ))

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean_email(self):
        user_email = self.cleaned_data.get('email')
        if not Account.objects.filter(email=user_email).exists():
            raise forms.ValidationError("User with this email doesn't exist!")
        return user_email

class CreateUserForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}
    ))
    passwordTwo = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}
    ))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'})
    )

    class Meta:
        model = Account
        fields = ('email', 'username', )

    def clean_passwordTwo(self):
        cd = self.cleaned_data
        if cd['password'] != cd['passwordTwo']:
            raise forms.ValidationError('Password must be the same!')
        return cd['password']

