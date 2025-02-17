from django.contrib import admin
from .models import Truck, Selection, Exit, Admmission
# Register your models here.

class FilterAdmin(admin.ModelAdmin):
    list_filter = ['date', 'officer', 'cab_no']
    search_fields = ['date', 'officer', 'cab_no']

class TruckAdmin(admin.ModelAdmin):
    list_filter = ['officer']
    search_fields = ['officer', 'cab_no']

admin.site.register(Truck, TruckAdmin)
admin.site.register(Selection, FilterAdmin)
admin.site.register(Exit, FilterAdmin)
admin.site.register(Admmission, FilterAdmin)