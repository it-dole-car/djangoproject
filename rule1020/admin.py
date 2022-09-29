from django.contrib import admin
from .models import  Barangay, Emp, Municipality, Province, User_office

from import_export.admin import ImportExportModelAdmin

admin.site.register(Emp)
admin.site.register(Province)

admin.site.register(User_office)

@admin.register(Municipality)
class MunicipalityAdmin(ImportExportModelAdmin):
    list_display = ("name", "province")
    pass

@admin.register(Barangay)
class BarangayAdmin(ImportExportModelAdmin):
    list_display = ("name", "municipality")
    pass

