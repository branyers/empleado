from django.contrib import admin
from .models import Persona, Habilidades
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.


class HabilidadesResource(resources.ModelResource):
    class Meta:
        model = Habilidades


class EmpleadoResource(resources.ModelResource):
    class Meta:
        model = Persona


class EmpleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['FirstName']
    list_display = ('FirstName', 'LastName', 'Jobs',)
    list_filter = ('departament','Jobs','habilidades')
    filter_horizontal = ('habilidades',)
    resource_class = EmpleadoResource

    list_display = (
        'id',
        'FirstName',
        'LastName',
        'Jobs',
        'departament',
        'full_name',
    )

    def full_name(self, obj):
        return obj.FirstName + " " + obj.LastName



class HabilidadesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['Habilidades']
    list_display = ('Habilidades',)
    list_filter = ('Habilidades',)
    resource_class = HabilidadesResource


admin.site.register(Persona, EmpleadoAdmin)
admin.site.register(Habilidades, HabilidadesAdmin)

admin.site.site_header = "Sistema de Branyes"
admin.site.site_title = "Branyes Module"
admin.site.index_title = "Bienvenidos al portal de administración"