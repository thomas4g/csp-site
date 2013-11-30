from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length = 100, required = True)
    first_name = forms.CharField(max_length = 20, required = False)
    last_name = forms.CharField(max_length = 20, required = False)
    email1 = forms.EmailField(required = True)
    email2 = forms.EmailField(required = True)
    password1 = forms.CharField(max_length = 20, required = True, widget = forms.PasswordInput())
    password2 = forms.CharField(max_length = 20, required = True, widget = forms.PasswordInput())
