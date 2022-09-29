# products/tables.py
import django_tables2 as tables
from models import Emp

class ProductHTMxTable(tables.Table):
    class Meta:
        model = Emp
        template_name = "tables/bootstrap_htmx.html"