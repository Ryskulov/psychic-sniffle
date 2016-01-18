from django.shortcuts import render

from .models import Place
# Create your views here.


def show_list(request):
    places = Place.objects.all().order_by('-created')
    return render(request, 'places/list.html', {'places': places})


def search(request):
    context = {}
    q = request.GET.get('q', None)

    if q:
        places = Place.objects.filter(name__icontains=q)
        context = {'query': q, 'places': places}
        template = 'places/list.html'

    return render(request, template, context)