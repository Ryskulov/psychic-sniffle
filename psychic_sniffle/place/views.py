from django.shortcuts import render

from .models import Place
# Create your views here.


def show_list(request):
    return render(request, 'places/list.html', {})


def search(request):
    context = {}
    q = request.GET.get('q', None)

    if q:
        places = Place.objects.filter(name__icontains=q)
        context = {'query': q, 'places': places}
        template = 'places/list.html'

    return render(request, template, context)