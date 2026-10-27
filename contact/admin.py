from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class contactAdmin(admin.ModelAdmin):
    list_display = 'id','First_name','Last_name','Phone'
    search_fields = 'id', 'First_name', 'Last_name'
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'First_name', 'Last_name'
    list_display_links = 'id', 'Phone'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',