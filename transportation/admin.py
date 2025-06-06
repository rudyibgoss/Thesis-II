from django.contrib import admin #importing Django's admin module to customize admin interface
from .models import * #importing all models from the current app's models.py
# Register your models here.

#custom admin class for the 'controls' model
class controlsAdmin(admin.ModelAdmin):

     #disable the ability to add new entries for this model in the admin panel
    def has_add_permission(self, request):
        return False

    #disable the ability to delete entries for this model in the admin panel
    def has_delete_permission(self, request, obj=None):
        return False

#register the 'controls' model with the custom admin class above
admin.site.register(controls, controlsAdmin)
