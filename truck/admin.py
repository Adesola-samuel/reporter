from django.contrib import admin
from .models import Truck, Selection, Exit, Admmission, Reservation, TrucksInsideWorkshop
# Register your models here.

class FilterAdmin(admin.ModelAdmin):
    list_filter = ['date', 'officer', 'cab_no']
    search_fields = ['date', 'officer', 'cab_no']

class TruckAdmin(admin.ModelAdmin):
    list_filter = ['officer']
    search_fields = ['officer', 'cab_no']

class ReservationAdmin(admin.ModelAdmin):
    list_filter = ['officer', 'fleet', 'notification_date', 'type']
    search_fields = ['officer', 'cab_no', 'notification', 'fleet']

admin.site.register(Truck, TruckAdmin)
admin.site.register(Selection, FilterAdmin)
admin.site.register(Exit, FilterAdmin)
admin.site.register(Admmission, FilterAdmin)
admin.site.register(TrucksInsideWorkshop)
admin.site.register(Reservation, ReservationAdmin)