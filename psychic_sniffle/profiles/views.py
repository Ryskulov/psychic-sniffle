from django.shortcuts import render
from .models import Profile
from django import forms
# Create your views here.


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profiles/profile.html')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'avatar', 'birthday', 'status', 'phone'
        )


def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    form = ProfileEditForm(
        request.POST or None,
        request.FILES or None,
    instance=profile
    )

    if form.is_valid():
            profile_form = form.save(commit=False)
            profile_form.user = request.user
            profile_form.save()
            return redirect('/profile/')
    return render(request, 'profiles/profile_edit.html', {'form': form})


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
           'avatar', 'birthday', 'status', 'phone'
        )
