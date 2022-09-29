from import_export import resources
from . models import Barangay, Municipality, Province



class BarangayResource(resources.ModelResource):
    class Meta:
        model= Barangay


class MunicipalityResource(resources.ModelResource):
    class Meta:
        model= Municipality

