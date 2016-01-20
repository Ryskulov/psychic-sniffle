from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.contrib.auth import logout
# Create your views here.



class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password'
            )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label


def singin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            django_login(request, user)
            message = "User is valid, active and authenticated"
            return redirect('/profile/')
        else:
            message = "The password is valid< but the account has bees disabled"
    else:
        message = "The username and password were incorrect"
    return render(request, 'accounts/signin.html', {'error_message': message})


def singup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = True
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('/signin/')
    return render(request, "accounts/singup.html", {'form': form})


def singout(request):
    logout(request)
    return redirect('/')