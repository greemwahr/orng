from django.contrib import admin # Default import from django framework
from .models import RefGen, RefNo

class RefGenAdmin(admin.ModelAdmin):
  list_display = ('date_on_letter', 'date_of_dispatch', 'whom_to', 'subject')

class RefNoAdmin(admin.ModelAdmin):
  list_display = ('reference_number',)

admin.site.register(RefGen, RefGenAdmin)
admin.site.register(RefNo, RefNoAdmin)
