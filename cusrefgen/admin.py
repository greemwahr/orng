from django.contrib import admin # Default import from django framework
from .models import RefGen

class RefGenAdmin(admin.ModelAdmin):
  list_display = ('date_on_letter', 'date_of_dispatch', 'whom_to', 'subject')

admin.site.register(RefGen, RefGenAdmin)
