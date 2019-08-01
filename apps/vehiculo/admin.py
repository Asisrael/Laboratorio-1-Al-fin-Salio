from django.contrib import admin

from .models import Vehiculo, Parqueo, Asign
# Register your models here.

class AsignInline(admin.TabularInline):
    """Tabular Inline View for Recipe"""

    model = Asign
    extra = 0


class VehiculoAdmin(admin.ModelAdmin):
    inlines = [AsignInline]
    list_display = ('plate', 'Vehicle_type')



admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Parqueo)