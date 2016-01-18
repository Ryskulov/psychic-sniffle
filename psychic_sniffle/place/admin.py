from django.contrib import admin
from place.models import Place, PlaceTag, Feedback

# Register your models here.

class PlaceAdmim(admin.ModelAdmin):
    list_display = ('name', 'created', 'slug')

admin.site.register(Place, PlaceAdmim)
admin.site.register(PlaceTag)
admin.site.register(Feedback)


