from django.contrib import admin
from .models import servicios
# Register your models here.

class vista(admin.ModelAdmin):
    readonly_fields = ('created','update')
    list_display = ('title','content','created')
    search_fields = ('title',)
    ordering = ('created',)


admin.site.register(servicios,vista)