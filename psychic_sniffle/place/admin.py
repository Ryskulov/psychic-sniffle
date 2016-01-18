from django.contrib import admin
from place.models import Place, PlaceTag, Feedback


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_picture', 'name', 'slug', 'is_published', 'created')
    list_filter = ('tags', )
    search_fields = ('name', 'slug', )
    readonly_fields = ('created', )
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceTag)
admin.site.register(Feedback)


