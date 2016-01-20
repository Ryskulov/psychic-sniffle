from django.contrib import admin
from place.models import Place, PlaceTag, PlacePicture, Feedback, Category
from place.widgets import AdvancedFileInput
from django.db import models


class PlacePictureStackable(admin.StackedInline):
    model = PlacePicture
    extra = 0
    formfield_overrides = {models.ImageField: {'widget': AdvancedFileInput}}


class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlacePictureStackable, ]
    list_display = ('place_picture', 'name', 'slug', 'is_published', 'created')
    list_filter = ('category', 'tags', )
    search_fields = ('name', 'slug', )
    readonly_fields = ('created', )
    prepopulated_fields = {"slug": ("name",)}
    formfield_overrides = {models.ImageField: {'widget': AdvancedFileInput}}

admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceTag)
admin.site.register(Feedback)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

admin.site.register(Category, CategoryAdmin)

