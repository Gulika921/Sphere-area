from django.contrib import admin
from universe.models import (
    Galaxy,
    StarSystem,
    Star,
    Planet,
    Moon
)
# Register your models here.


@admin.register(Galaxy)
class GalaxyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "size_x",
        "size_y",
    ]


@admin.register(StarSystem)
class StarSystemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "pos_x",
        "pos_y",
        "galaxy",
    ]


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "color",
        "diameter",
        "star_system",
        "sphere_area",
    ]


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "color",
        "diameter",
        "star_system",
        "live",
        "sphere_area",
    ]


@admin.register(Moon)
class MoonAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "color",
        "diameter",
        "planet",
        "sphere_area",
    ]
