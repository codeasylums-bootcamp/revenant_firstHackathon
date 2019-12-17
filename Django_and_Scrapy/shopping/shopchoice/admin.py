from django.contrib import admin

# Register your models here.
from .models import flipkart,ajio
from import_export.admin import ImportExportModelAdmin

@admin.register(flipkart,ajio)
class ViewAdmin(ImportExportModelAdmin):
    pass
