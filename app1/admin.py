from django.contrib import admin
from .models import Details
from import_export import resources
from import_export.admin import  ImportExportModelAdmin


# Register your models here.
class DetailsResource(resources.ModelResource):
    class Meta:
        model = Details

class DetailsAdmin(ImportExportModelAdmin):
    resource_class = DetailsResource

admin.site.register(Details, DetailsAdmin)