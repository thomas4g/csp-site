
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from register.forms import RegistrationForm
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return HttpResponse("This is the homepage")
    print("Someone went to the homepage")

def login(request):
    return HttpResponse("This is the login page")


#THIS IS HACKY AS HELL!
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            pass1 = form.cleaned_data['password1']
            pass2 = form.cleaned_data['password2']
            email1 = form.cleaned_data['email1']
            email2 = form.cleaned_data['email2']
            if User.objects.filter(username=username).count():
                return HttpResponseRedirect('/register/')
            if pass1 == pass2 and email1 == email2:
                user = User.objects.create_user(username, email1, pass1)
                try:
                    user.first_name = first
                except:
                    pass
                try:
                    user.last_name = last
                except:
                    pass
             
                    user.save()
                    return HttpResponseRedirect('/success/')
            else:
                return HttpResponseRedirect('/register/')
        else:
            return HttpResponseRedirect('/register/')
    else:
        form = RegistrationForm()
    return render(request, 'register/register.html', {'form' : form})

def thanks(request):
    return HttpResponse("thanks for registering!")