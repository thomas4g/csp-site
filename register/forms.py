from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length = 25, required = True)
    first_name = forms.CharField(max_length = 20, required = False)
    last_name = forms.CharField(max_length = 20, required = False)
    email = forms.EmailField(required = True)
    confirm_email = forms.EmailField(required = True)
    password = forms.CharField(max_length = 20, required = True, widget = forms.PasswordInput())
    confirm_password = forms.CharField(max_length = 20, required = True, widget = forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 25, required = True)
    password = forms. CharField(max_length = 20, required = True, widget = forms.PasswordInput())