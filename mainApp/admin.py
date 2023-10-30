from django.contrib import admin
from .models import *
from .models import *


# admin.site.register(Student)
# admin.site.register(Plan)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "course", "student_number"]
    search_fields = ["name"]
    list_filter = ["course"]
    list_display_links = ["name"]


@admin.register(Plan)
class PlanaAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "detail", "isDone", "student_id"]
    search_fields = ["title"]
    list_filter = ["isDone"]
    list_display_links = ["title"]
    autocomplete_fields = ["student_id"]
