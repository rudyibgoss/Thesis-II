from django.contrib import admin
from .models import *
# Register your models here.

class controlsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(controls, controlsAdmin)
