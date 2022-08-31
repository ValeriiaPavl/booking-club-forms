

from django.contrib import admin

from .models import FormModel, FormData, FormField


class FormModelAdmin(admin.ModelAdmin):
    pass


class FormDataAdmin(admin.ModelAdmin):
    pass


class FormFieldAdmin(admin.ModelAdmin):
    pass


admin.site.register(FormModel, FormModelAdmin)
admin.site.register(FormData, FormDataAdmin)
admin.site.register(FormField, FormFieldAdmin)