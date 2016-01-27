from django.shortcuts import render
from django.contrib.auth.models import User
from profiles.models import Profile
from django import forms
# Create your views here.
from django.http import JsonResponse


def profile(request):
    profile = request.user.profile
    return render(request, 'profiles/profile.html', {'profile': profile})


def profile_detail_public(request, username):
    user = User.objects.get(username=username)
    profile = user.profile
    if request.user.is_authenticated:
        return render(request, 'profiles/profile.html', {'profile': profile})

def profile_detail_private(request):
    profile = request.user.profile
    if request.user.is_authenticated:
        return render(request, 'profiles/profile_detail.html', {'profile': profile})


class ProfileEditForm(forms.ModelForm):
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
            return redirect('/profiles/')
    return render(request, 'profiles/profile_edit.html', {'form': form})

def add_favorite(request, place_id):
    place = Place.objects.get(place_id)
    request.user.profile.favorites.add(place)
    return JsonResponse({'status': 'OK'})