from django.contrib import admin
from place.models import Place, PlaceTag, Feedback, Category, PlacePicture


class PlacePictureStackable(admin.StackedInline):
    model = PlacePicture
    extra = 2

class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlacePictureStackable, ]
    list_display = ('place_picture', 'name', 'slug', 'is_published', 'created')
    list_filter = ('category', 'tags', )
    search_fields = ('name', 'slug', )
    readonly_fields = ('created', )
    prepopulated_fields = {"slug": ("name",)}
    model = Place

admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceTag)
admin.site.register(Feedback)
admin.site.register(PlacePicture)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

admin.site.register(Category, CategoryAdmin)
